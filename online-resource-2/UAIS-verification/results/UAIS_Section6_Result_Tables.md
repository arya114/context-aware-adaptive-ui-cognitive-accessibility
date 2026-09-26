# Section 6 observed result tables

Counts below are from the final frozen build run, not expected results. Oracle rows overlap because one case can have several oracle tags. The inventory is a bounded expansion, not the complete space of all possible VER-CAT1 inputs.

## Table 10. Verification coverage by oracle

| Oracle | Planned entries | Executed | Pass | Fail | Unresolved | Not run | Coverage notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| O1 | 55 | 54 | 54 | 0 | 0 | 1 | Synthetic input classification; reflow/feature witnesses injected, not measured in a browser. |
| O2 | 643 | 641 | 641 | 0 | 0 | 2 | 252 C→N, 112 N→R, 24 assistance-state edge checks, 144 action-gate branches; additional enum/variant/sequence cases. Predicate extraction and complete effects remain bounded. |
| O3 | 45 | 44 | 44 | 0 | 0 | 1 | Fixed plan/set witnesses, closed composition examples and semantic scopes; full typed canonical domain not run. |
| O4 | 38 | 38 | 38 | 0 | 0 | 0 | Ordered event and transaction/state model; no distributed/browser concurrency experiment. |
| O5 | 43 | 42 | 42 | 0 | 0 | 1 | Model state and reachability checks, plus deliberate rejected-mutation controls; no browser preservation claim. |
| End-to-End | 14 | 14 | 14 | 0 | 0 | 0 | Selected model chains; eight traces additionally checked against required fields, five transaction branches audited separately. |

Unique inventory: 775 entries; 770 executed deterministic cases match their frozen expected objects, 0 mismatches and 0 unresolved executions; 5 explicit gap entries are not run. Agreement on this selected executable inventory is 100%. This is not a framework-wide pass rate. Acceptance audits and checker negative controls are reported separately rather than pooled into that denominator.

## Table 11. Representative resolver cases

| Case | Candidate/plan situation | Relevant criteria | Expected | Observed | Result |
| --- | --- | --- | --- | --- | --- |
| O3/compose/compatible | R1.A2, R3.A1 | Admission, permitted realisation and compatibility | COMBINE | COMBINE | Pass |
| O3/compose/shared | R1.A3, R4.A2 | Admission, permitted realisation and compatibility | TRANSFORM | TRANSFORM | Pass |
| O3/compose/guidance | R1.A1, R2.A1 | Admission, permitted realisation and compatibility | TRANSFORM | TRANSFORM | Pass |
| O3/stage/True | R2.A3, R4.A1 | Admission, permitted realisation and compatibility | TRANSFORM | TRANSFORM | Pass |
| O3/compose/text | R1.A4, R3.A3 | Admission, permitted realisation and compatibility | TRANSFORM | TRANSFORM | Pass |
| O3/compose/review | R3.A4, R4.A4 | Admission, permitted realisation and compatibility | TRANSFORM | TRANSFORM | Pass |
| O3/reduce/narrow | OPT01, error | Admission, permitted realisation and compatibility | TRANSFORM | TRANSFORM | Pass |
| O3/reduce/none | error | Admission, permitted realisation and compatibility | SUPPRESS | SUPPRESS | Pass |
| coverage | Explicit scoped plan witnesses | Six ordered criteria | {'selected': ['a'], 'operation': 'KEEP'} | {'selected': ['a'], 'operation': 'KEEP'} | Pass |
| incomparable | Explicit scoped plan witnesses | Six ordered criteria | {'selected': [], 'operation': 'DEFER'} | {'selected': [], 'operation': 'DEFER'} | Pass |
| lower-after-incomparable | Explicit scoped plan witnesses | Six ordered criteria | {'selected': ['b'], 'operation': 'KEEP'} | {'selected': ['b'], 'operation': 'KEEP'} | Pass |
| tie | Explicit scoped plan witnesses | Six ordered criteria | {'selected': ['a'], 'operation': 'KEEP'} | {'selected': ['a'], 'operation': 'KEEP'} | Pass |
| unknown | Explicit scoped plan witnesses | Six ordered criteria | {'selected': [], 'operation': 'DEFER'} | {'selected': [], 'operation': 'DEFER'} | Pass |

## Table 12. Invariant results

| Invariant | Logged predicate evaluations at admission | Violations on admitted transitions | Evidence and boundary |
| --- | --- | --- | --- |
| INV-01 | 30 | 0 | Admission records in final traces; model state only |
| INV-02 | 30 | 0 | Admission records in final traces; model state only |
| INV-03 | 30 | 0 | Admission records in final traces; model state only |
| INV-04 | 30 | 0 | Admission records in final traces; model state only |
| INV-05 | 30 | 0 | Admission records in final traces; model state only |

The five predicates are recorded together at each listed admission. Their counts are not independent scenario counts. Deliberate corrupt-state/reachability probes are negative oracle controls, not applied changes: expected false predicates are detections rather than observed adaptation-induced violations. These local predicates do not establish complete enforcement of every service constraint or actual DOM/IME preservation.

## Table 13. Transaction branch results

| Branch | Query status evidence | Retry disposition | New retry attempts | Logical identities | Committed effects | Recorded feedback | Acceptance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X-C | completed | SUPPRESS | 0 | 1 | 1 | completed | Pass |
| X-P | pending | DEFER | 0 | 1 | 0 | pending | Pass |
| X-R | safely_retryable | KEEP | 1 | 1 | 1 | pending | Pass |
| X-F | terminal_rejected | SUPPRESS | 0 | 1 | 0 | terminal_rejected | Pass |
| X-U | unknown | DEFER | 0 | 1 | 0 | unknown | Pass |

Each branch has one initial simulated submission attempt and one read-only query. Total submission attempts are two for X-R and one for the other branches. X-C starts with one already committed effect despite response loss; its query adds no effect. X-R commits during the admitted simulated retry, but feedback remains pending until a later completion response. Feedback here is a machine-readable baseline service output, not a rendered UI assessment.

## Table 14. Trace reconstruction acceptance

| Scenario | Required stages | Observed stages | Missing required fields at final audit | Initial strict acceptance | Final strict acceptance |
| --- | --- | --- | --- | --- | --- |
| applied | 10 | 10 | 0 | Fail | Pass |
| combine | 10 | 10 | 0 | Fail | Pass |
| transform | 10 | 10 | 0 | Fail | Pass |
| suppress | 10 | 10 | 0 | Fail | Pass |
| defer-execute | 10 | 10 | 0 | Fail | Pass |
| defer-supersede | 10 | 10 | 0 | Fail | Pass |
| unknown | 10 | 10 | 0 | Fail | Pass |
| transaction | 10 | 10 | 0 | Fail | Pass |

The ten stages are Observation, Context, C→N edge, Need, N→R edge, Rule, Action, Resolver, Admission and Result. The acceptance checker also checks version links, resolver inputs, admission vectors/tokens and deferred supersession. Three negative controls remove a version, a token or a parent reference; all three corruptions are rejected. This establishes the checked trace structure within these model scenarios, not independent validation of every logged semantic assertion.
