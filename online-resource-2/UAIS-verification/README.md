# UAIS verification execution package

Current assessment: **SECTION 6 NOT YET SUPPORTED** for the complete requested verification scope. This package contains actual bounded model executions, not a complete browser application or a user study.

## Reproduce the final build

Use Python 3 with its standard library. From this package directory run:

```text
python revision-0.1.2/runner.py
```

The runner verifies the frozen file hashes, loads the frozen inventory and expected objects, and creates a new uniquely named directory under revision-0.1.2/runs. It does not overwrite the retained runs. Do not rerun a freeze script in an already frozen build, or edit a frozen file to make a failing case pass. New implementation changes require a new build directory and manifest. Revised/new expected cases require a recorded dataset revision; a normative change requires a new governing specification version.

The code uses synthetic identities and an in-memory simulated ledger. It sends no network requests. The service manifest binds ST01–ST07, FLD01–FLD06, REQ01–REQ03, DOC01, REVIEW01, VAL01–VAL07 and OP01. The model includes a fixture validator but the current inventory does not exercise the complete real service workflow and every validator boundary. Upload and asset content effects remain part of the declared coverage limitations.

## Evidence locations

- execution_manifest.json: first frozen build 0.1.0.
- inventory.json and expected.json: first independent input/expected dataset. prepare.py writes these without importing the implementation.
- runs/20260913T022049Z-e0dd89d1: first run, 764 object matches and 5 not-run entries.
- assessment-1: eight stricter trace acceptance failures and initial defect/coverage findings.
- revision-0.1.1: instrumented retest build and six additional instances; 770 matches and 5 not-run entries.
- assessment-2: eight accepted traces and three rejected corruptions after the trace fix.
- transaction-audit-0.1.1: five failed TX-1 acceptance assessments, including terminal retry disposition and absent feedback evidence.
- revision-0.1.2: final build; inventory and expected objects unchanged from 0.1.1.
- revision-0.1.2/runs/20260913T022729Z-05c9476b: final 770 matches and 5 not-run entries, with records.jsonl, traces.jsonl and run.json.
- assessment-3: final eight trace acceptance checks and three checker negative controls.
- transaction-audit-0.1.2: five final passing TX-1 acceptance checks.
- results: coverage, result tables, defect register, limitations and provisional Section 6 narrative.

Every execution record includes the test/parent ID, oracle tags, input, actual initial state, expected/observed objects, verdict, trace IDs and specification/build identity. Final trace records carry the specification, catalogue, service and build versions. Child-family membership links are retained, but membership does not imply complete family coverage.

## Oracle independence and limits

The expectation generator never calls the implementation to obtain expected outcomes. Mapping expectations come from the locked imported tables; the implementation has separate literal matrices. Resolver expectations are separately declared examples. The same author produced the implementation and oracle translation, so independent-review assurance is limited.

Many predicates are semantic witnesses supplied at the model boundary. Legal enum/variant checks read the versioned registry and primarily verify adapter/data membership. Rule-mask checks project provided masks rather than deriving all masks from fully instantiated need evidence. These narrow checks are retained and labelled; they must not be advertised as complete contract-effect or end-to-end verification. The model's canonical key supports a restricted domain. There is no browser renderer, real IME observation, real capability probe or production backend.

No overall framework pass rate is claimed. The reported 100% is agreement only on the selected executable dataset. Oracle rows overlap. Acceptance audits are separate and earlier failures remain authoritative historical evidence. Missing required trace evidence was treated as failure, not silently filled after a run.

## Remaining work before Section 6 can be locked

Implement and exercise the complete typed canonical comparator domain; replace abstract action witnesses with independently assessed fixture effects and all required concrete scope branches; derive all rule-mask scenarios through their actual scoped need chains; implement the service UI and acquire browser reflow/feature/IME evidence; expand the inventory to include all remaining VER-CAT1 branch obligations. Preserve current sources and expected outcomes while versioning all additions and retests.
