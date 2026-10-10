# Task-specific analytic rubric

**Version:** HALA-KIT-R0.1.2 · Proposed ordinal anchors  
Use the four dimensions independently. There is no validated total, pass mark, 0–100 conversion or EQI in this kit.

## Rating process

First rate only the submitted response and its source cards. Hide assistance history, arm and proposed case anchors in the first pass where possible. Cite a response excerpt or specific omission for every rating.

Then review provenance separately. Keep the response-quality ratings unchanged unless the scoring evidence itself was mistaken. Change the interpretation of what the ratings warrant when assistance is revealed.

A high-quality answer supplied by AI can have high response-quality ratings. Those ratings do not become evidence that the learner originated or learned that reasoning. Lowering its quality rating simply because AI supplied it would conflate quality with provenance.

For missing or unavailable responses use **NA**, never zero. A submitted response with no relevant reasoning may receive zero. Ambiguous scoring should be flagged for adjudication; do not silently substitute NA for difficult evidence.

## Four dimensions, 0–3 each

| Dimension | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| **Conceptual accuracy** | Dominant conclusion contradicts the design or claims proof of an effect/no effect that the cards cannot support | Contains a relevant concept or concern, but its application is vague or its tentative conclusion unsupported | Applies a relevant design/uncertainty distinction correctly, but omits the observed pattern or a boundary needed for the conclusion | Connects the observed pattern, design/uncertainty and a proportionate conclusion with an explicit relevant boundary |
| **Evidence use** | No relevant evidence, or fundamentally misreads it | Names a card/detail without explaining its relevance | Correctly interprets relevant numerical/design details, but leaves an important link incomplete | Integrates the observed pattern with relevant design or uncertainty evidence and explains why both matter |
| **Justified reasoning** | No inferential chain, or incompatible conclusion | Conclusion has a weak or generic reason | Coherent conclusion with a plausible competing explanation | Explicitly connects evidence, a plausible alternative and a proportionate conclusion |
| **Verification / application** | No relevant check, or proposes an unethical/irrelevant action | Generic “check sources” or “get more data” | Specific relevant comparison, with an incomplete explanation of what it distinguishes | Feasible discriminating comparison plus a result that would strengthen, weaken or revise the conclusion |

The highest verification anchor concerns the quality of a proposed check, not proof that checking occurred. Report an enacted check separately only when a record supports it.

## Task-specific anchor guidance

**L:** the programme group improved more, but voluntary selection, extra sheets and opening hours prevent attribution to quiet seating alone. Equal baseline means do not establish group equivalence. A proposed randomized comparison of quiet versus usual seating with materials/time matched is relevant; a well-justified observational comparison may also be defensible. Pre/post form uncertainty limits interpretation of numerical gains.

**I:** coated buildings show the larger decrease, but simultaneous equipment replacement and self-selection are alternatives. Common milder weather can explain part of both decreases; it does not by itself explain the extra decrease in coated buildings. Comparing coating conditions while holding equipment and relevant exposure constant can discriminate better. Merely collecting more identical uncontrolled records does not resolve confounding.

Reward proportionate conclusions, not blanket skepticism. Lack of randomization does not prove an intervention has no effect. A well-designed randomized result would warrant more causal confidence than these observational cards, while still needing attention to execution and uncertainty.

## Do not reward these shortcuts

- Length, polished style, hedging frequency or use of words such as “confounding”.
- Naming sources without interpreting evidence.
- Unsupported allegations that a source is dishonest.
- Exact arithmetic when a correct verbal comparison suffices.
- Assuming more prompt turns mean deeper learning.
- Knowing a case's authored origin rather than observing its reasoning.

Minor language errors do not lower a rating unless meaning changes. An inaccurate evidence statement affects the dimensions it actually undermines; do not apply an automatic penalty to all four.

## Scoring and disagreement record

Use [review_sheet.csv](review_sheet.csv). Rater IDs refer to future reviewers, not participants. Record ratings before seeing proposed anchors, uncertainty and evidence. Preserve both original ratings when raters disagree; an adjudicated rating is a separate field or record.

Use the synthetic anchors to discuss the rubric, not to compute empirical rater reliability or train a validated scorer. Future reliability analysis needs real independently obtained ratings, an appropriate sampling design and uncertainty estimates. Agreement alone would not establish validity, fairness or form comparability.

**Abstention boundary:** response quality may be rateable while learner-originated competence remains indeterminate.


## Decision rules for overlapping anchors

Use the dominant conclusion, not a single qualifying word, to distinguish accuracy 0 from 1. “No randomization proves no effect” is 0. A tentative causal suggestion with a relevant but unapplied concern can be 1. Quote the deciding phrase.

Accuracy 3 does not require listing every limitation. For L/I, a correct between-group pattern plus an explicit causal limit and relevant design reason suffices. Accuracy 2 describes a correct partial application missing one of those links. S03 therefore proposes 3; S06's I response proposes 2 because it does not clearly state the between-group pattern. An external reviewer may reject these boundaries; preserve the disagreement.

For R, randomization with the stipulated implementation and positive uncertainty range supports a bounded causal conclusion. Do not require a confound explanation where none is evidenced. For U, an estimate near zero with a wide range supports uncertainty, not evidence of equivalence.

A justified replication, generalization check or precision-improving study can meet verification 3 if it states a discriminating result. Asking for randomization again is not automatically the best check.

## Missingness rehearsal

S10 has no submitted response: all four dimensions are NA, with reason “no response submitted”. This is different from an actual submitted answer such as “I do not know”, which can be rated for the evidence it displays. Never infer lack of competence from missingness.

## Clarifications following PI review — v0.1.2

### Illustrations are not checklists

Task-specific guidance describes possible reasoning, not a required list of every limitation. Apply the dimension definition. For accuracy 3, identify the observed pattern, relevant design/uncertainty reason and proportionate conclusion. Do not demand extra limitations merely because a longer example names them.

S01 and S03 can both meet accuracy/evidence/reasoning 3 while differing on verification (3 versus 2). Equal treatment of concise reasoning does not require identical full profiles.

### Partial responses and unavailable material

Rate each dimension using the entire available response, regardless of which numbered question contains the evidence. A skipped question is not an automatic zero: the relevant reasoning or check may appear elsewhere.

Use zero when a submitted, assessable response displays none of the relevant evidence for a dimension or meets that dimension's zero anchor. Use NA when the material needed to rate is unavailable or genuinely unassessable; record the reason. Partial technical loss can make a dimension unassessable even when some text survives. A blank submission is NA; an assessable “I do not know” with no demonstrated reasoning receives zero, not NA.

Example: “The programme group improved more but they volunteered. The forms might not be comparable.” This contains evidence and a partial inferential link. Do not assign reasoning zero merely because an alternative explanation was not separately listed. Apply anchors and document whether the implicit link supports 1 or 2; this example is not a locked reference rating. With no check anywhere, verification is zero.

Do not interpret any zero as proof that the person lacks the capacity generally.

### A specific check must address the question

Verification 2 requires a comparison or check that addresses a relevant alternative or uncertainty, even if its discriminatory explanation is incomplete. Specificity alone is insufficient. Verification 3 additionally requires a defensible account of what the result would change. A check need not settle every uncertainty, but conclusions must respect what remains uncontrolled.

For L, “compare programme scores before and after” repeats evidence already provided and does not distinguish quiet seating from selection or extra practice. It cannot receive 2 merely for naming a comparison; distinguish a generic relevant wish for further checking (1) from an irrelevant or ineffective proposed check (0), explaining the task-specific judgment.

Matching practice sheets and hours can address those co-interventions but does not automatically eliminate motivation or selection differences. A response claiming otherwise cannot receive verification 3 on that basis. Randomization, defensible adjustment or other designs require their own justification; no method name automatically earns a score.

### Provenance is stipulated, not detected

Origins in synthetic fixtures are author-supplied scenario facts. Revealing them is an interpretive exercise, not a text-based detection test. No kit response demonstrates that a blinded reviewer can identify AI assistance. Actual assistance conditions need procedural records and uncertainty reporting. Group-level classification accuracy, even if later measured, would not certify any individual response's origin.

S10 remains the no-response case. The earlier missingness rehearsal's contrast with submitted answers applies to assessable available material; the partial-loss exception above takes precedence.
