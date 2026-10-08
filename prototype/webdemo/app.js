/* HALA v0.2: illustrative, in-memory research sequence only. */
(() => {
  "use strict";
  let token = null;
  let arm = "A";
  let stage = null;
  const $ = id => document.getElementById(id);
  const stageNames = ["T0","T1","T2","T3","T4"];
  const buttons = [...document.querySelectorAll(".arm")];
  const error = message => {
    $("error").textContent = message || "";
    $("error").classList.toggle("hidden", !message);
  };
  const show = (id, visible) => $(id).classList.toggle("hidden", !visible);
  async function post(route, body) {
    const response = await fetch(route, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      cache: "no-store",
      body: JSON.stringify(body)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Request failed");
    return result;
  }
  const showStage = response => {
    stage = response.stage;
    error("");
    $("status").textContent = response.complete ? "COMPLETED" : response.stage + " / " + response.arm;
    for (const element of $("stages").children) {
      const elementStage = element.textContent.trim().slice(0, 2);
      element.classList.toggle("active", elementStage === stage);
      element.classList.toggle("done", stage === "DONE" ||
        stageNames.indexOf(elementStage) < stageNames.indexOf(stage));
    }
    show("intro", false);
    show("exercise", !response.complete);
    show("complete", response.complete);
    if (response.complete) return;
    $("tasklabel").textContent = stage === "T1" ? "LEARNING SESSION · " + response.step + "/" + response.steps : "INDEPENDENT ASSESSMENT";
    $("tasktitle").textContent = response.title;
    $("scenario").textContent = stage === "T1" ? response.lesson : response.scenario;
    $("question").textContent = stage === "T1" ? "Read this scripted teaching material, then continue." : response.question;
    $("answerlabel").textContent = stage === "T1" ? "Reflection (optional, not analysed)" : "Your illustrative answer (not scored)";
    $("answer").value = "";
    $("answer").placeholder = stage === "T1" ? "Optional reflection…" : "Explain your reasoning…";
    $("tasknotice").textContent = response.notice || (stage === "T1"
      ? "This is a scripted mock, not a connected AI agent."
      : "Independent response. This is a demo; no scores are calculated.");
    $("continue").textContent = response.stage === "T4" ? "Complete journey →" : "Continue →";
  };
  for (const button of buttons) button.addEventListener("click", () => {
    arm = button.dataset.arm;
    buttons.forEach(b => {
      const selected = b === button;
      b.classList.toggle("selected", selected);
      b.setAttribute("aria-pressed", String(selected));
    });
  });
  buttons.forEach(b => b.setAttribute("aria-pressed", String(b.dataset.arm === arm)));
  $("start").addEventListener("click", async () => {
    try {
      $("start").disabled = true;
      const response = await post("/api/start", {arm});
      token = response.token;
      showStage(response);
    } catch (e) { error(e.message); }
    finally { $("start").disabled = false; }
  });
  $("continue").addEventListener("click", async () => {
    try {
      $("continue").disabled = true;
      const response = await post("/api/submit", {token, stage, answer: $("answer").value});
      showStage(response);
    } catch (e) { error(e.message); }
    finally { $("continue").disabled = false; }
  });
  const reset = () => {
    token = null; stage = null;
    $("status").textContent = "NOT STARTED";
    show("intro", true);
    show("exercise", false);
    show("complete", false);
    [...$("stages").children].forEach(e => e.classList.remove("active", "done"));
    error("");
    $("intro").scrollIntoView({behavior: "smooth", block: "center"});
  };
  $("restart").addEventListener("click", reset);
  $("again").addEventListener("click", reset);
})();