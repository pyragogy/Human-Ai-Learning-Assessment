"""Start HALA's synthetic two-process demo locally with one command.

This is a developer convenience, NOT user/privilege isolation or approved
research deployment. Do not enter real learner or sensitive information.
"""
import os
import secrets
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _wait_for_worker(process, socket_path, timeout=5):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError("Assessor exited before socket became available")
        if socket_path.exists():
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                try:
                    sock.connect(str(socket_path))
                    return
                except OSError:
                    pass
        time.sleep(0.05)
    raise RuntimeError("Assessor failed to start within startup timeout")


def main():
    if os.name != "posix" or not hasattr(socket, "AF_UNIX"):
        raise SystemExit("Local demo requires Unix sockets (Linux/macOS)")
    with tempfile.TemporaryDirectory(prefix="hala-synthetic-") as directory:
        os.chmod(directory, 0o700)
        socket_path = Path(directory) / "assessor.sock"
        env = os.environ.copy()
        env["HALA_ASSESSOR_SOCKET"] = str(socket_path)
        # A fresh, unlogged development credential shared only with child processes.
        env["HALA_ASSESSOR_SECRET"] = secrets.token_urlsafe(48)
        # Do not inherit a deployment group configuration into this fixture.
        env.pop("HALA_ASSESSOR_SOCKET_GROUP", None)
        assessor = subprocess.Popen(
            [sys.executable, "-m", "prototype.separated_assessment.service", str(socket_path)],
            cwd=REPO_ROOT, env=env,
        )
        gateway = None
        try:
            _wait_for_worker(assessor, socket_path)
            gateway = subprocess.Popen(
                [sys.executable, "-m", "prototype.separated_assessment.gateway"],
                cwd=REPO_ROOT, env=env,
            )
            print("HALA SYNTHETIC DEMO: http://127.0.0.1:8766", flush=True)
            print("No real student data. Local demo only; press Ctrl+C to stop.", flush=True)
            status = gateway.wait()
            if status != 0:
                raise RuntimeError(f"Gateway exited with status {status}")
        except KeyboardInterrupt:
            pass
        finally:
            if gateway is not None and gateway.poll() is None:
                gateway.terminate()
                try:
                    gateway.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    gateway.kill()
                    gateway.wait()
            if assessor.poll() is None:
                assessor.terminate()
                try:
                    assessor.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    assessor.kill()
                    assessor.wait()


if __name__ == "__main__":
    main()
