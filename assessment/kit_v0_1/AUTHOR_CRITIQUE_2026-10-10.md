# Author critique and proposed revisions

**Examined baseline:** `5fec2e8dedf984e112ec8eb3c41b78d7e187711c`  
**Author:** development AI assistant; same authoring process, not independent review.  
**Owner adjudication:** pending. **Independent verification:** pending.

This is a logical inspection of authored fixtures, not a blind scoring exercise. The author already knew the expected anchors and origins. No rater agreement or learner evidence is reported.

| Finding | Baseline evidence and reproduction | Proposed v0.1.1 revision | Possible falsifier / remaining concern |
| :--- | :--- | :--- | :--- |
| K01 · Coverage favors doubt | Read TASKS L/I: both observational with explicit confounds; no response tests justified causal trust | Add R/U and S07–S09 | A reviewer finds positive control still rewards formulaic language; coverage remains narrow |
| K02 · Accuracy 0/1 overlaps | RUBRIC allows unsupported certainty at 0, causal proof with a concern at 1; compare S04/S05 | Separate dominant contradicted conclusion from vague/tentative application | Reviewers cannot reproduce distinction; simplify anchors |
| K03 · 2/3 boundary unresolved | S03 and S06 give accuracy 2–3 without a decision rule | Require pattern/design/conclusion link for 3; propose S03=3, S06-I=2 | Rule rewards verbosity or disputes over implicit meaning; external challenge needed |
| K04 · Missingness rule unexercised | Rubric says NA, but six cases all have answers | Add S10, missing_reason and response_id fields | Review process still treats absent response as low competence |
| K05 · Review record underspecified | CSV lacks task version and separate identity for later I answer in a case | Add task_version, response_id and response_condition | Provenance/deviation capture still inadequate for a human pilot; this sheet is synthetic-only |
| K06 · Task demands reveal reasoning moves | L/I explicitly ask for alternatives and a check | Retain as prompted task competence; document limitation | Unprompted behavior cannot be inferred from prompted responses |

**K06 remains open.** These tasks assess reasoning when asked to apply it. They cannot show spontaneous vigilance. A future less-cued task would require separate design, response-process review and comparability investigation, not silently removing prompts in one arm.

All proposed fixes remain challengeable. Version 0.1 anchors are retained in Git history. No changes to P01, its outcome hierarchy or the submitted PDF.

## Scope for PI

Review the revised commit with source cards visible but proposed anchors hidden first. Declare prior exposure and model/tool assistance. Look for a counterexample to the new boundaries, especially concise answers, bounded trust and missingness. Post version-pinned findings on PR #23; do not modify the branch during the first pass. PI's AI review cannot substitute for independent human assessment expertise.

**Stop condition for authoring:** the package is ready for critique, not certified for participant use. Further revisions should follow concrete objections, rather than keep polishing around imagined agreement.
