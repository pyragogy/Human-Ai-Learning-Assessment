import csv
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analyse import load_rows, report

COLUMNS = ["participant_id", "arm", "stage", "score", "independent"]


class PipelineTests(unittest.TestCase):
    def fixture(self, rows):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=COLUMNS)
                writer.writeheader()
                writer.writerows(rows)
            return load_rows(path)

    def test_excludes_assisted_stage_from_gain(self):
        rows = [
            dict(participant_id="p1", arm="C", stage="T0", score="20", independent="true"),
            dict(participant_id="p1", arm="C", stage="T1", score="100", independent="false"),
            dict(participant_id="p1", arm="C", stage="T2", score="40", independent="true"),
        ]
        records, members = self.fixture(rows)
        self.assertEqual(report(records, members)["arms"]["C"]["paired_T2_minus_T0_mean"], 20)
        self.assertEqual(report(records, members)["arms"]["C"]["stages"]["T1"]["mean"], 100)

    def test_rejects_duplicate(self):
        row = dict(participant_id="p1", arm="A", stage="T0", score="30", independent="true")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.fixture([row, row])

    def test_rejects_false_independence(self):
        with self.assertRaisesRegex(ValueError, "independence"):
            self.fixture([dict(participant_id="p1", arm="B", stage="T2", score="60", independent="false")])

    def test_rejects_out_of_range(self):
        with self.assertRaisesRegex(ValueError, "Out-of-range"):
            self.fixture([dict(participant_id="p1", arm="A", stage="T0", score="101", independent="true")])

    def test_missing_followup_is_not_imputed(self):
        records, members = self.fixture([
            dict(participant_id="p1", arm="A", stage="T0", score="30", independent="true")
        ])
        output = report(records, members)["arms"]["A"]
        self.assertEqual(output["paired_T2_minus_T0_n"], 0)
        self.assertIsNone(output["paired_T2_minus_T0_mean"])
        self.assertEqual(output["stages"]["T2"]["missing_n"], 1)

    def test_inconsistent_arm_rejected(self):
        rows = [
            dict(participant_id="p1", arm="A", stage="T0", score="30", independent="true"),
            dict(participant_id="p1", arm="B", stage="T2", score="50", independent="true"),
        ]
        with self.assertRaisesRegex(ValueError, "Inconsistent arm"):
            self.fixture(rows)


if __name__ == "__main__":
    unittest.main()
