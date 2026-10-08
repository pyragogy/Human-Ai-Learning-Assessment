# Scripted synthetic journey — HALA v0.1

A small, reproducible **scripted mock** of the three proposed study arms and the T0–T4 journey. It does not use real learners or a live AI model.

```bash
python prototype/journey.py > synthetic_journey.json
python -m unittest discover -s prototype/tests -v
```

**Demonstrated:** deterministic, version-tagged event records; basic SHA-256 hash-chain integrity; staged A/B/C mock sessions; separate T1 teaching and T0/T2/T3/T4 assessment records; automated tests including deliberately injected answer leakage.

**Not demonstrated:** actual AI collaboration, secure evaluation isolation, learning gains, human validity, causal efficacy, cryptographic authentication, or privacy protection for a real deployment. A party able to rewrite an entire log can recompute its hash chain. This is a teaching fixture, not a trustworthy audit backend.

**Next gate:** isolate secure items into a protected assessment service inaccessible to the intervention model, add policy/consent enforcement and provenance capture, then independent expert review before any participant recruitment.
