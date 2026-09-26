# Online Resource 2 — Frozen inputs, code and verification evidence

Companion to **A Context-Aware Rule-Based Adaptive User Interface Framework for Cognitive Accessibility in Digital Public Services**.

The `UAIS-verification/` directory is an exact extraction of the existing `UAIS_Section6_Core_Closure_Evidence.zip` (SHA-256 `f9cc460d81fbaa3bc9e323b98f36dae30999940d32167071dc4044d503dadaed`). All 193 original file entries are preserved, including earlier versions, failures, retests, trace audits and final results. No frozen files were regenerated or corrected during packaging.

## Reproduce the final evaluated build

Use Python 3.12 (standard library only; no pip dependencies). The original manifest records Python 3.12.14 on Windows. From `online-resource-2/UAIS-verification/`, run separately:

```text
python closure-0.2.2/runner.py
python closure-0.2.2/run_closure.py
```

The scripts check frozen hashes before execution and write uniquely named new run directories. Do not run `prepare.py`, `freeze_revision.py` or packaging scripts to reproduce the published inventory: these belong to the historical preparation workflow.

Expected counts: the first script reports 770 Pass, 0 Fail, 0 Unresolved and 5 historical Not run placeholders. The second reports 98 executed, 98 Pass, 0 Fail. The five historical entries are not additional executable failures: three gaps were discharged by closure evidence, while browser reflow and actual DOM/IME preservation remain outside the declared domain. Unique executed instances total 868; oracle-tag rows overlap and must not be summed.

## Evidence map

| Evidence | Relative path under UAIS-verification |
|---|---|
| Governing fingerprints and version lineage | `closure-0.2.2/execution_manifest.json` |
| Frozen regression inputs / expectations | `closure-0.2.2/inventory.json`, `expected.json` |
| Frozen closure inputs / expectations | `closure-0.2.2/closure_inventory.json`, `closure_expected.json` |
| Source and synthetic fixture | `closure-0.2.2/model.py`, `semantic.py`, `service_manifest.json`, `specs/` |
| Original 770-case final run | `closure-0.2.2/runs/20260913T030324Z-075d96fc/` |
| Original 98-case final run | `closure-0.2.2/closure_runs/20260913T030322Z-8f183b76/` |
| Trace acceptance and negative controls | `closure-assessment-022/` |
| Transaction audit | `closure-transaction-audit-0.2.2/` |
| Earlier failures and retests | Earlier version, run and assessment directories, plus `core_results/UAIS_Section6_Core_Defect_Retest_Register.json` |
| Manuscript results and claim limits | `core_results/UAIS_Section6_Core_Closure_Summary.json`, `UAIS_Section6_Exact_Claims_and_Boundaries.md` |

See `UAIS-verification/CORE_CLOSURE_README.md` for detailed lineage. Its remark that an earlier ZIP was unavailable refers to the older pre-closure archive, not the preserved core-closure package used here. `reproduction-check/` contains the separately labelled 26 September 2026 rerun and does not replace original results.

## Interpretation

Matching frozen expectations demonstrates agreement for selected semantic-model scenarios. It does not establish independent oracle validity, exhaustive correctness, browser accessibility, human benefit or production readiness. Implementation and oracle translation share authorship; this remains a limitation. No human or personal evaluation data are included.

Public URL, DOI and license are pending. This is a local supplementary package, not evidence of a published repository.
