# Core closure: observed result tables

Final build: UAIS-CORE-0.2.2. All reported outcomes are read from retained execution records. These tables cover a declared headless semantic model, not browser acquisition, rendering or empirical effectiveness.

## Table 10. Revised coverage by oracle

| Oracle | Planned executable | Executed | Pass | Fail | Unresolved | Not run in declared domain |
| --- | --- | --- | --- | --- | --- | --- |
| O1 | 54 | 54 | 54 | 0 | 0 | 0 |
| O2 | 712 | 712 | 712 | 0 | 0 | 0 |
| O3 | 116 | 116 | 116 | 0 | 0 | 0 |
| O4 | 85 | 85 | 85 | 0 | 0 | 0 |
| O5 | 112 | 112 | 112 | 0 | 0 | 0 |
| End-to-End | 71 | 71 | 71 | 0 | 0 | 0 |

Oracle rows overlap. Unique final instances: 868 = 770 unchanged regression cases + 98 additions. The five old not-run entries remain immutable historical gap placeholders; three are discharged by new evidence and two are explicitly outside the revised domain. They are not five remaining executable failures.

## Table 11. Action-level semantic contract results

| ActionID | Positive case | Transform or attempted unlisted transform | Checked postconditions | Invariants at configuration boundary | Observed property/effect | Result |
| --- | --- | --- | --- | --- | --- | --- |
| R1.A1 | positive: Pass | contextual: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, instruction_content, no_service_side_effect | 5/5 true | G.guidance.visibility = contextual | Pass |
| R1.A2 | positive: Pass | on-demand: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, correct_definition, no_service_side_effect | 5/5 true | G.term.explanation = inline | Pass |
| R1.A3 | positive: Pass | shared-progress: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, actual_step_cue, no_service_side_effect | 5/5 true | G.step.cue = full | Pass |
| R1.A4 | positive: Pass | text-equivalent: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, example_identity, no_service_side_effect | 5/5 true | G.example.visibility = on-demand | Pass |
| R1.A5 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, help_semantics, no_service_side_effect | 5/5 true | G.help.access = contextual | Pass |
| R1.A6 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, error_identity_truth, no_service_side_effect | 5/5 true | G.error.explanation = contextual | Pass |
| R2.A1 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, essential_content, no_service_side_effect | 5/5 true | D.layout.density = reduced | Pass |
| R2.A2 | positive: Pass | narrow-scope: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, independent_scopes, no_service_side_effect | 5/5 true | D.content.reduction[OPT01].state = collapsed | Pass |
| R2.A3 | positive: Pass | within-stage: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, members_dependencies, no_service_side_effect | 5/5 true | D.grouping.mode = semantic | Pass |
| R2.A4 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, valid_control, no_service_side_effect | 5/5 true | D.primary.control.emphasis = emphasized | Pass |
| R2.A5 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, requirements_truth, no_service_side_effect | 5/5 true | D.requirements.view = checklist | Pass |
| R3.A1 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, persisted_accepted_snapshot | 5/5 true | P.draft.autosave = on; separate persist admission/result | Pass |
| R3.A2 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, guarded_same_identity_retry | 5/5 true | P.network.retry = guarded-auto; separate retry admission/result | Pass |
| R3.A3 | positive: Pass | registered-text: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, essential_asset_ids, no_service_side_effect | 5/5 true | P.asset.profile = low-bandwidth | Pass |
| R3.A4 | positive: Pass | shared-review: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, honest_recovery, no_service_side_effect | 5/5 true | P.recovery.panel = visible | Pass |
| R3.A5 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, honest_feedback, no_service_side_effect | 5/5 true | P.submission.feedback = explicit | Pass |
| R3.A6 | positive: Pass | unlisted-conversion, additional restore: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, authorised_lossless_resume | 5/5 true | P.draft.resume = guided; separate resume admission/result | Pass |
| R3.A7 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, readonly_new_evidence | 5/5 true | P.transaction.reconciliation = guarded-query; separate query admission/result | Pass |
| R4.A1 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, logical_stage_binding, no_service_side_effect | 5/5 true | F.flow.mode = staged | Pass |
| R4.A2 | positive: Pass | shared-cue: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, actual_progress, no_service_side_effect | 5/5 true | F.progress.indicator = on | Pass |
| R4.A3 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, existing_validation, no_service_side_effect | 5/5 true | F.validation.timing = step | Pass |
| R4.A4 | positive: Pass | shared-recovery: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, faithful_review, no_service_side_effect | 5/5 true | F.review.summary = on | Pass |
| R4.A5 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, legal_navigation, no_service_side_effect | 5/5 true | F.stage.navigation = back-review | Pass |
| R4.A6 | positive: Pass | unlisted-conversion: Pass | values_preserved, step_progress_preserved, input_preserved, configuration_invariants, command_identity_unchanged, required_routes, dependency_identity, no_service_side_effect | 5/5 true | F.dependency.cue = visible | Pass |

Each positive record retains its scope, mediated need, RuleSource, property anchor, content/state witnesses, invariant vector and trace IDs. Transform checks retain purpose and justified scoped coverage; R2.A2 retains only the eligible optional scope and preserves the protected error route. Empty transformation lists are tested with an unlisted conversion and leave U/S unchanged. This is representative effect coverage, not exhaustive parameter/negative-branch coverage.

## Table 12. Canonical key and deterministic resolver results

| Test | Expected | Observed | Result |
| --- | --- | --- | --- |
| CORE/KEY/decimal-equivalent | 0 | 0 | Pass |
| CORE/KEY/decimal-exact | -1 | -1 | Pass |
| CORE/KEY/decimal-numeric-order | -1 | -1 | Pass |
| CORE/KEY/signed-zero | 0 | 0 | Pass |
| CORE/KEY/unicode-nfc | 0 | 0 | Pass |
| CORE/KEY/unicode-distinct | -1 | -1 | Pass |
| CORE/KEY/boolean | -1 | -1 | Pass |
| CORE/KEY/enum | 0 | 0 | Pass |
| CORE/KEY/sequence-equal | 0 | 0 | Pass |
| CORE/KEY/sequence-order | -1 | -1 | Pass |
| CORE/KEY/set-order | 0 | 0 | Pass |
| CORE/KEY/nested | 0 | 0 | Pass |
| CORE/KEY/multi-action-order | 0 | 0 | Pass |
| CORE/KEY/shorter-prefix | -1 | -1 | Pass |
| CORE/RESOLVE/tie/False | {'selected': ['two'], 'operation': 'KEEP', 'canonical_used': True} | {'selected': ['two'], 'operation': 'KEEP', 'canonical_used': True} | Pass |
| CORE/RESOLVE/unknown/False | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | Pass |
| CORE/RESOLVE/incomparable/False | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | Pass |
| CORE/RESOLVE/lower/False | {'selected': ['ten'], 'operation': 'KEEP', 'canonical_used': False} | {'selected': ['ten'], 'operation': 'KEEP', 'canonical_used': False} | Pass |
| CORE/RESOLVE/tie/True | {'selected': ['two'], 'operation': 'KEEP', 'canonical_used': True} | {'selected': ['two'], 'operation': 'KEEP', 'canonical_used': True} | Pass |
| CORE/RESOLVE/unknown/True | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | Pass |
| CORE/RESOLVE/incomparable/True | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | {'selected': [], 'operation': 'DEFER', 'canonical_used': False} | Pass |
| CORE/RESOLVE/lower/True | {'selected': ['ten'], 'operation': 'KEEP', 'canonical_used': False} | {'selected': ['ten'], 'operation': 'KEEP', 'canonical_used': False} | Pass |
| CORE/KEY/binary-float | REJECT_UNKNOWN | REJECT_UNKNOWN | Pass |
| CORE/KEY/unknown-value | REJECT_UNKNOWN | REJECT_UNKNOWN | Pass |
| CORE/KEY/nonfinite | REJECT_UNKNOWN | REJECT_UNKNOWN | Pass |
| CORE/DEDUP/False | {'operation': 'COMBINE', 'selected': ['a'], 'sources': ['a', 'b']} | {'operation': 'COMBINE', 'selected': ['a'], 'sources': ['a', 'b']} | Pass |
| CORE/DEDUP/True | {'operation': 'COMBINE', 'selected': ['a'], 'sources': ['a', 'b']} | {'operation': 'COMBINE', 'selected': ['a'], 'sources': ['a', 'b']} | Pass |

Pairwise key relations use −1, 0 and +1 for less than, equal and greater than. Binary-float/unknown/nonfinite decimal inputs are rejected as unavailable exact parameters. Equivalent canonical plans retain both provenance aliases and produce one selected semantic execution record through COMBINE; the representative alias is a record identifier, not an extra accessibility preference.

## Table 13. Independently scoped multi-rule scenarios

| Scenario | Concrete scoped support inputs | Nominated rules | Candidate actions | Compatibility/conflict and resolver outcome | Execution result |
| --- | --- | --- | --- | --- | --- |
| CORE/MULTI/S00 | No added support request/demand | Empty | None; baseline safety retained | compatible: {} | Pass; semantic state preserved |
| CORE/MULTI/S01 | N1@TERM01 | R1 | R1.A2 | compatible: {'R1.A2': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S02 | N4@GROUP-ST04 | R2 | R2.A3 | compatible: {'R2.A3': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S03 | N4@d1/persistence | R3 | R3.A1 | compatible: {'R3.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S04 | N4@ST04 | R4 | R4.A1 | compatible: {'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S05 | N1@TERM01, N4@GROUP-ST04 | R1, R2 | R1.A2, R2.A3 | compatible: {'R1.A2': 'KEEP', 'R2.A3': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S06 | N1@TERM01, N4@d1/persistence | R1, R3 | R1.A2, R3.A1 | compatible: {'R1.A2': 'KEEP', 'R3.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S07 | N1@TERM01, N4@ST04 | R1, R4 | R1.A2, R4.A1 | compatible: {'R1.A2': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S08 | N4@GROUP-ST04, N4@d1/persistence | R2, R3 | R2.A3, R3.A1 | compatible: {'R2.A3': 'KEEP', 'R3.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S09 | N4@GROUP-ST04, N4@ST04 | R2, R4 | R2.A3, R4.A1 | compatible: {'R2.A3': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S10 | N4@d1/persistence, N4@ST04 | R3, R4 | R3.A1, R4.A1 | compatible: {'R3.A1': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S11 | N1@TERM01, N4@GROUP-ST04, N4@d1/persistence | R1, R2, R3 | R1.A2, R2.A3, R3.A1 | compatible: {'R1.A2': 'KEEP', 'R2.A3': 'KEEP', 'R3.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S12 | N1@TERM01, N4@GROUP-ST04, N4@ST04 | R1, R2, R4 | R1.A2, R2.A3, R4.A1 | compatible: {'R1.A2': 'KEEP', 'R2.A3': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S13 | N1@TERM01, N4@d1/persistence, N4@ST04 | R1, R3, R4 | R1.A2, R3.A1, R4.A1 | compatible: {'R1.A2': 'KEEP', 'R3.A1': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S14 | N4@GROUP-ST04, N4@d1/persistence, N4@ST04 | R2, R3, R4 | R2.A3, R3.A1, R4.A1 | compatible: {'R2.A3': 'KEEP', 'R3.A1': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/S15 | N1@TERM01, N4@GROUP-ST04, N4@d1/persistence, N4@ST04 | R1, R2, R3, R4 | R1.A2, R2.A3, R3.A1, R4.A1 | compatible: {'R1.A2': 'KEEP', 'R2.A3': 'KEEP', 'R3.A1': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/suppressed | N1@TERM01, N4@GROUP-ST04, N4@d1/persistence, N4@ST04 | R1, R2, R3, R4 | R1.A2, R2.A3, R3.A1, R4.A1 | suppressed: {'R1.A2': 'KEEP', 'R2.A3': 'SUPPRESS', 'R3.A1': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/transformed | N1@TERM01, N4@GROUP-ST04, N4@d1/persistence, N4@ST04 | R1, R2, R3, R4 | R1.A2, R2.A3, R3.A1, R4.A1 | transformed: {'R1.A2': 'KEEP', 'R2.A3': 'TRANSFORM', 'R3.A1': 'KEEP', 'R4.A1': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/deferred | N1@TERM01, N4@GROUP-ST04, N4@d1/persistence, N4@ST04 | R1, R2, R3, R4 | R1.A2, R2.A3, R3.A1, R4.A1 | deferred: {'R1.A2': 'KEEP', 'R2.A3': 'KEEP', 'R3.A1': 'KEEP', 'R4.A1': 'DEFER'} | Pass; semantic state preserved |
| CORE/MULTI/lower | N1@TERM01, N4@GROUP-ST04 | R1, R2 | R1.A2, R2.A3 | lower: {'selected': ['R1.A2'], 'operation': 'KEEP'} | Pass; semantic state preserved |
| CORE/MULTI/final-incomparable | N1@TERM01, N4@GROUP-ST04 | R1, R2 | R1.A2, R2.A3 | final-incomparable: {'selected': [], 'operation': 'DEFER'} | Pass; semantic state preserved |

The term request justifies N1→R1 with its N1→R2 condition false. Independent N4 reminder scopes justify R2 through retained grouping references, R3 through interrupted draft-reference continuity, or R4 through staged references with preserved back/review access. Each conditional edge has separate frozen object-level facts. Their unions generate all sixteen subsets, so no requested subset was unreachable in this fixture. The two competing-plan scenarios use a controlled exclusive-support-region feasibility witness; they do not assert that all action pairs inherently conflict. The complete context/condition/edge records are in the JSON inventory and traces.

## Table 14. Regression and acceptance history

| Package/check | Executed | Pass | Fail | Notes |
| --- | --- | --- | --- | --- |
| Prior selected baseline | 770 | 770 | 0 | Preserved, not replaced |
| Final regression of same IDs/oracles | 770 | 770 | 0 | No old executable case disappeared |
| Final closure additions | 98 | 98 | 0 | 49 action/transform checks; 27 canonical checks; 21 multi-rule cases; one query provenance check |
| Final unique executable inventory | 868 | 868 | 0 | Zero unresolved and zero not-run executable cases inside declared domain |
| Initial stricter trace acceptance | 8 | 0 | 8 | Retained earlier failures |
| Intermediate transaction acceptance | 5 | 0 | 5 | Retained earlier failures |
| Equivalent-plan audit on 0.2.0 | 2 | 0 | 2 | IMPL-003, retained |
| Equivalent-plan retest | 2 | 2 | 0 | Included in 98, not added again |
| Final independent trace acceptance | 8 | 8 | 0 | Separate audit of representative regression traces |
| Final transaction acceptance | 5 | 5 | 0 | Same TX-1 criteria |
| Final trace-checker negative controls | 3 | 3 | 0 | Missing version/token/parent rejected |
