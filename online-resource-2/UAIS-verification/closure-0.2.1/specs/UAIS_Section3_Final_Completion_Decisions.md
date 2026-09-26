# UAIS Section 3 Final Completion Decisions

Working title: A Context-Aware Rule-Based Adaptive User Interface Framework for Cognitive Accessibility in Digital Public Services

Decision date: 12 September 2026. Scope: completion of the Section 3 specification; no Section 4 drafting or implementation and no execution of verification cases.

**Decision: SECTION 3 READY TO LOCK.** The explicit user-adopted catalogue refinement and all 24 operational contracts are now integrated as UAIS-CAT-1.0. This consolidated record is UAIS-S3-FINAL-1.0. Read it with [Final Action Catalogue and Contracts](UAIS_Final_Action_Catalogue.md), [Final Verification Delta](UAIS_Final_Verification_Delta.md), and [Exact Section 3 Text Patches](UAIS_Section3_Text_Patches.md). Readiness concerns the research specification; no adaptive-system tests or empirical study were executed for this decision.

## 1 Version evolution

Three provenance classes apply throughout:

- **Historical baseline H:** the recovered dissertation/proposal specification, including its own v1.0 labels. The local alias `H-PROP-20260908` identifies the recovered source; it does not rename the historical source version.
- **Current UAIS specification U:** the manuscript architecture and decisions adopted in this document. `UAIS-S3-FINAL-1.0` is the current consolidated specification record; CD1 is archived as the earlier completion decision. Runtime verification remains to be performed.
- **Refinement:** an explicitly recorded current change or operational clarification of H. Component labels `C13-CD1`, `RES-CD1`, `INV-CD1`, `MAP-CD1`, `TRACE-CD1`, and `VER-DELTA-CD1` identify the corresponding decisions here. `UAIS-CAT-1.0` is the completed current catalogue. TRACE-CAT1 and VER-CAT1 extend the retained CD1 components.

The historical source is LAMPIRAN FINAL REVISI 2.docx, SHA-256 `18d603b150032591509e670e2e39277a61ab23420bee0a65da5e0b791997e9da`. Its recovered text is preserved in [Recovered Historical Specifications](Recovered_Historical_Specifications.md). Exact mappings and the original 35 principal cases are imported separately in [Historical Mapping and Verification Import](UAIS_Historical_Mapping_Verification_Import.md). These records describe specifications, not proof of successful execution.

| Historical mechanism | Limitation motivating refinement | Current mechanism and provenance |
| --- | --- | --- |
| R1–R4 with PR1–PR4 priority/conflict resolution | Four protected objectives do not express the current six comparison criteria | Action Composition & Transition Resolver with the six-criterion policy RES-CD1 |
| Subsequent historical guards, compatibility, candidate actions and five operations | Operations alone do not determine a unique admissible result | Explicit admissibility, feasibility classes and lexicographic filtering |
| Historical minimum-property-change and ID/legal-value tie-break | A tie-break cannot resolve unknown evidence or a substantive incomparability | Typed change representation and canonical key restricted to genuine equality |
| Safe-point application and reevaluation | Need explicit freshness and deferred successor semantics | Coherent current snapshot, fresh full-chain reevaluation and linked lifecycle |
| 24 actions distributed 6–6–6–6 | Current architecture requires 6–5–7–6 | UAIS-CAT-1.0: merge H:R2.A2/H:R2.A6 into R2.A2 and separately formalise R3.A7 |
| Explicit-request C1.3 with Normal/AssistanceNeeded/Recovering/Unknown | Does not define Emerging or the current recovery control semantics | C13-CD1 with four current control states and separate evidence quality |
| Data/progress/function protection in guards and V3 | Not expressed as the present five numbered predicates | INV-CD1, explicitly bound to service state below |
| V1=15, V2=12, V3=8 principal cases | Refinements affect some inputs and expected outcomes | Preserve all historical cases; add versioned child subcases and oracle mappings |

The exact six-criterion policy is a **current refined resolver policy**, not a historical restatement of PR1–PR4. Neither the refinement nor technical verification establishes a cognitive diagnosis or an empirical accessibility benefit.

## 2 Final action catalogue refinement UAIS-CAT-1.0

Historical distribution 6–6–6–6 becomes current 6–5–7–6 by an explicit user-adopted current design decision. The historical catalogue is not rewritten. Historical R2.A6 is merged into R2.A2, never reassigned to R3. R3.A7 separately formalises status-reconciliation behaviour from H:F.5.1, H:V2-07, H:V3-02 and H:V3-05. Exactly 24 current ActionIDs exist.

| Current ActionID | Current name | Historical provenance | Delta |
| --- | --- | --- | --- |
| R1.A1 | Contextual Guidance | H:R1.A1 | Retained purpose; current operational contract specified |
| R1.A2 | Term Explanation | H:R1.A2 | Retained purpose; current operational contract specified |
| R1.A3 | Step Cue | H:R1.A3 | Retained purpose; current operational contract specified |
| R1.A4 | Examples | H:R1.A4 | Retained purpose; current operational contract specified |
| R1.A5 | Contextual Help Access | H:R1.A5 | Retained purpose; current operational contract specified |
| R1.A6 | Contextual Error Explanation | H:R1.A6 | Retained purpose; current operational contract specified |
| R2.A1 | Reduce Interface Density | H:R2.A1 | Retained purpose; current operational contract specified |
| R2.A2 | Contextual Secondary/Optional Content Reduction | H:R2.A2 and H:R2.A6 | Merged and renamed; independently parameterised nonessential scopes |
| R2.A3 | Semantic Grouping | H:R2.A3 | Retained purpose; current operational contract specified |
| R2.A4 | Emphasise Primary Control | H:R2.A4 | Retained purpose; current operational contract specified |
| R2.A5 | Checklist Presentation | H:R2.A5 | Retained purpose; current operational contract specified |
| R3.A1 | Draft Autosave | H:R3.A1 | Retained purpose; current operational contract specified |
| R3.A2 | Guarded Retry | H:R3.A2 | Retained purpose; current operational contract specified |
| R3.A3 | Low-Bandwidth Asset Profile | H:R3.A3 | Retained purpose; current operational contract specified |
| R3.A4 | Recovery Panel | H:R3.A4 | Retained purpose; current operational contract specified |
| R3.A5 | Explicit Submission Feedback | H:R3.A5 | Retained purpose; current operational contract specified |
| R3.A6 | Guided Draft Resumption | H:R3.A6 | Retained purpose; current operational contract specified |
| R3.A7 | Transaction Status Reconciliation | Historical retry/status/safety/recovery requirements; no historical ActionID | Separately formalised continuity action |
| R4.A1 | Staged Flow | H:R4.A1 | Retained purpose; current operational contract specified |
| R4.A2 | Progress Indicator | H:R4.A2 | Retained purpose; current operational contract specified |
| R4.A3 | Step Validation | H:R4.A3 | Retained purpose; current operational contract specified |
| R4.A4 | Review Summary | H:R4.A4 | Retained purpose; current operational contract specified |
| R4.A5 | Back/Review Navigation | H:R4.A5 | Retained purpose; current operational contract specified |
| R4.A6 | Dependency Cues | H:R4.A6 | Retained purpose; current operational contract specified |

The complete 20-field schema is populated for each action in [Final Action Catalogue](UAIS_Final_Action_Catalogue.md), with a structured copy in [Action Contracts JSON](UAIS_Final_Action_Contracts.json). CG-1–CG-9, TX-1 and TRACE-CAT1 are normative common clauses, including independently scoped R2.A2 reduction, protected essential routes, closed transformation lists, typed U change atoms and no direct context/action shortcuts. Empty transformation lists explicitly prohibit TRANSFORM.

TX-1 distinguishes configuration commits from subsequently observed server status and authorised draft-resume events. Equal target/current U prohibits redundant layout mutation but does not erase a separately eligible event-triggered command. Every such command still requires current candidacy, a fresh token, admission and trace. Status-checking baseline safety remains active in both UI conditions; baseline checks are labelled as such and are not fabricated adaptive decisions.

NeedCoverage matches manifest-declared support objects within a task. Status-determination and status-communication are different scoped obligations justified through the same existing N6/N7 architecture; showing uncertainty does not discharge status-determination. The fixed contract does not add N types or C→R edges.

## 3 Final C1.3 state machine C13-CD1

This is a current operational refinement. The control states are Stable, Emerging, AssistanceNeeded and Recovering. They describe current interaction-support requirements, not disability or clinical/cognitive status. The arrow in the architecture indicates the ordinary progression; it is not the full transition graph.

### Evidence contract

The minimal current policy uses assistance-related events, not inferred performance thresholds:

- `support.preview_opened`: the user opens a context-specific assistance preview for a declared support kind. This indicates exploration of support, not a confirmed need. It is distinct from opening ordinary navigation, an automatically displayed tooltip, or an automatic guidance panel.
- `assistance.requested`: the user explicitly requests additional help. A context-bound control supplies the support kind, or the user selects it. Kinds map to N1 clarification, N2 step guidance, N3 orientation, N4 reminder, N5 choice explanation, and N6 correction/recovery assistance. A generic request without a kind enters AssistanceNeeded but does not activate all six needs; kind clarification is required for an edge.
- `assistance.closed`: the user confirms that an identified request is resolved or no longer required. Merely rendering help or dismissing a dialog does not establish resolution.
- `support.preview_closed`: the unconfirmed preview is closed or the user explicitly declines further assistance.
- `task.resumed`: a subsequent, user-originated service interaction is accepted at a safe point in the episode's task scope, with no outstanding request or preview. Examples are a completed field edit or legal stage navigation. Autosave, repaint, probe responses and background validation are not resumption evidence.

Events carry event ID, ordered sequence, session ID, service/task scope, service version, support kind if known, and episode/request references. Duplicate events are idempotent. Requests remain pending until an explicit closure event; a reliable lack of new events is not a closure. Multiple requests form a set; new requests add to it and closure removes only named requests. The last closure starts recovery. Historical request kinds are retained as recovery-support provenance until recovery completes. New requests interrupt recovery.

Evidence is fresh when it belongs to the current scope/version and the assistance-event stream is reconciled through the current sequence. A known gap, ambiguous ordering, incompatible scope/version or unavailable snapshot makes quality unknown. No arbitrary expiry duration is introduced. Reconciliation requires a current authoritative request snapshot and an ordered watermark, or a current explicit user status confirmation; it cannot infer that help is no longer required from silence.

### Transition table

`Scope E` means reevaluate C1.3, its six conditional C→N edges, their affected N→R edges, relevant actions and all coupled resolver alternatives; then recheck execution admissibility. It is dependency-based reevaluation, not a direct C1.3→R shortcut.

| CurrentState | Event/Evidence | Guard | NextState | Persistence requirement | Recovery requirement | Reevaluation scope |
| --- | --- | --- | --- | --- | --- | --- |
| Stable | support.preview_opened | Fresh user-originated preview; no pending request | Emerging | Remains until preview closure or confirmed request | Not applicable | Scope E; preview alone does not activate a C1.3 need |
| Emerging | support.preview_closed | No other active preview and no pending request | Stable | Explicit closure; elapsed time is insufficient | Not applicable | Scope E |
| Emerging | assistance.requested | Fresh explicit request, including a generic request awaiting kind clarification | AssistanceNeeded | Request latched by ID until explicitly closed | Not applicable | Scope E; only known relevant kinds nominate needs |
| Stable | assistance.requested | Same request guard | AssistanceNeeded | Immediate event-based activation; no Emerging delay | Not applicable | Scope E |
| AssistanceNeeded | assistance.closed | Last pending request closed; associated preview closed in the same acknowledged episode | Recovering | Must occupy Recovering until a later task.resumed event | Closure alone cannot prove recovery completion | Scope E; retain scoped recovery-support provenance |
| Recovering | task.resumed | Fresh subsequent user interaction, safe point, no pending request or preview | Stable | Separate later event; cannot reuse closure as resumption | Accepted interaction re-establishes stable task participation | Scope E; remove only resolved C1.3 support evidence |
| Recovering | assistance.requested | Fresh explicit request | AssistanceNeeded | Immediate; recovery completion is cancelled | Restart recovery only after all requests close again | Scope E |

These are the only state-changing edges after initialization. In particular there is no direct AssistanceNeeded→Stable, Stable→Recovering or automatic Recovering→Emerging edge. Further requests in AssistanceNeeded are self-transitions; partial request closures also remain there. Preview events during recovery keep Recovering and block completion until closed. Other events leave the state unchanged. No state transition is inferred from task duration, error count, repeated clicks, demography, device class, or connectivity alone.

**Initialization:** before any adaptation decision, obtain the current assistance snapshot. A known pending request initializes AssistanceNeeded; otherwise an open preview initializes Emerging; otherwise initialize Stable. Recovering is restored only with a compatible persisted episode and its closure/resumption history. If the snapshot is unavailable, the stored initial control value may be Stable but `evidence_quality=unknown` and `initialized=false`; it is not reported as observed Stable and activates no C1.3 edge. A later reconciled snapshot performs initialization, not an invented return edge.

**Unavailable/stale evidence:** retain the last control value as history with quality unknown; do not advance recovery or use its stale need evidence as newly justified. Preserve installed support conservatively until reevaluation can establish that withdrawal is safe and no longer needed. An independently current explicit request may re-establish AssistanceNeeded using the fresh snapshot containing that request. Service changes suspend old-scope evidence and require a new scoped snapshot; they do not assert that an old episode was resolved.

**Abrupt events:** a fresh explicit help request bypasses Emerging. A service/network failure does not itself alter C1.3; it follows its proper context/evidence route, such as C3→N. If a failure also prevents observing assistance status, set evidence quality unknown. Global assistance controls remain reachable while inferred adaptations are deferred.

**Hysteresis:** event-based latching and a distinct post-closure resumption event replace arbitrary time/count thresholds. Emerging is deliberately conservative: support exploration alone never becomes AssistanceNeeded through repeated observations. This minimal policy does not claim passive detection of unexpressed difficulty.

## 4 Final six-comparator policy RES-CD1

### Comparison domain and outputs

An alternative is a complete compatible action-realisation plan for a coupled adaptation component: `(action IDs, variants, parameters, target U, scoped effects, proposed transition, provenance)`. Compare alternatives against the same coherent `(C,N,S,U,versions)` snapshot. Include an unchanged-U plan where it remains safe. Mandatory safety functions are present in all alternatives; they are not traded for Need Coverage. Actions outside a coupled component may proceed only when their joint effects are proven independent and satisfy all invariants.

Every comparator returns better, worse, equal or unknown. A set-based comparator additionally reports `relation=incomparable` when neither set contains the other; its continuation code is `equal`, but `genuine_equal=false`. Equality of cardinalities is never substituted for set equality.

| Criterion | Comparison object and required inputs | Better / worse / equal conditions | Unknown and progression |
| --- | --- | --- | --- |
| 1 Validity & Integrity | Proposed transition and all INV-01–05 predicates; legal catalogue identities/values; service snapshot | Hard admissibility only: all true is admissible; any false is inadmissible. An admissible alternative outranks a false one; two admissible alternatives are equal here. Two false alternatives are both rejected, not tied winners | A required predicate not demonstrably true is unknown and prohibits execution. No lower score can compensate. Remove rejected/unknown proposals from executable plans; log the cause and retain safe handling |
| 2 Feasibility | Declared effects, device/feature checks, display contract, service constraints and current state | READY: effects realisable now. WAIT: a named temporary blocker with a declared release event. BLOCKED: no permitted realisation under the current service/capability/contract, rather than an ordinary wait. READY is better than WAIT; WAIT better than BLOCKED for classification, but only READY proceeds to executable comparison. Equal classes retain their blocker details | Missing capability/constraint evidence gives UNKNOWN. Do not descend for that alternative. WAIT generates DEFER; BLOCKED generates SUPPRESS for this decision. A changed capability/version can cause new candidacy later |
| 3 Need Coverage | Q, the set of currently justified scoped need instances, and contract-declared coverage of effects actually delivered now | Let K(A) be covered members of Q. A is better iff K(A) is a strict superset of K(B); worse iff a strict subset; equal iff identical. Non-nested sets are incomparable and continue without invented weights | Undetermined required membership, scope match or coverage effect gives unknown for that comparison; block lower comparison for that unresolved component. Deferred promises do not count as delivered coverage |
| 4 State Continuity | Post-adaptation logical/interaction state after all invariants hold; residual disruption set D | Prefer a strict subset of D; reverse is worse; identical D is genuine equality; non-nested sets are incomparable. D is defined below, not a count of needs | Unknown state mapping or disruption effect stops lower comparison for the component |
| 5 Transition Stability | Declared transition guards, assistance/connectivity recovery phases and valid decision history; stability disruption set T | Prefer a strict subset of T; reverse is worse; identical T is genuine equality; non-nested sets are incomparable. Hard transition guards must already pass | Unknown required history/phase stops lower comparison. Fewer property changes alone does not imply greater stability |
| 6 Minimal Change | Complete canonical property maps of U now and target U | Smaller number of changed declared property atoms is better; larger is worse; same number is equal for this criterion. No accessibility weights | Unknown initial/target property or undefined normalisation yields unknown; canonical tie-break is then prohibited |

An immediately unsafe restructuring during active input is not executed and then scored. Its immediate plan fails admission; a separately represented waiting plan preserves the current state, records the target, and receives WAIT. No feasibility rank authorises a known invariant violation. If a candidate is unknown, independently admissible alternatives remain possible; its hypothetical unproven effect is neither credited nor used to claim a proven optimal result over unavailable alternatives.

**Need instances:** identify each required support obligation by `(NeedID, service version, task scope, evidence references)`, deduplicating evidence for the same scoped need while retaining every source. Membership in Q requires a true imported/current mapping predicate. Unknown edges do not establish membership. Multiple N sources combine by logical support, not by votes. NeedCoverage declarations assert a specific supported need/scope/effect; they are design assertions to be verified, not empirical claims of user benefit.

**Residual continuity set D:** record affected scoped anchors for (a) moving a non-editing focus anchor to a different logical control, (b) moving the visible reading anchor to a different logical content anchor, (c) closing an open nonessential help/review disclosure, or (d) discarding a nonessential local presentation choice, such as a user-expanded optional group. Data, valid progress, required access and active input are already protected by invariants. A backend DOM replacement that restores the same logical anchors does not create D. Stage IDs are not presentation-page indices. Empty D is preferred to a nonempty D, all higher criteria permitting. Unknown effects cannot be entered as an empty set.

**Stability set T:** record scoped commitments disturbed by (a) replacing still-justified installed support with a different realisation before its assistance recovery completes, (b) reversing the most recent committed property transition while the support episode justifying it is unresolved, and (c) superseding a still-justified deferred target with a different target before its declared release event. These are preference costs only for alternatives whose changes remain allowed by all hard guards and preserve support purpose. Retaining irrelevant or unsafe support receives no protection. Each entry references the actual episode/property/decision, not a guessed duration. With a complete empty history, T is empty; unavailable history is unknown. This distinguishes stability of an ongoing support transition from visual edit distance.

**Minimal-change representation:** U=[G,D,P,F] has a versioned leaf-property dictionary. A change atom is `(dimension, semantic component ID, property name)`; action IDs are provenance, not extra change units. Each atom appears once even if several actions affect it. Compare typed, normalised values at the same scope: exact enum/boolean/string equality, exact numeric value without arbitrary rounding, order-sensitive equality for sequences and order-insensitive equality only for declared sets. The service instance supplies scope IDs, while the action catalogue fixes the property dictionary before verification. Optional omission means the same manifest default in both maps. No action may improve its score by splitting or merging properties at runtime. Change distance is the cardinality of the unequal atoms. UAIS-CAT-1.0 fixes the property dictionary and independently scoped R2.A2 atoms; actual versioned element IDs instantiate it. No runtime change in atom granularity is permitted.

### Lexicographic processing with incomparability

Apply criteria in the frozen order. After hard gates, at each criterion remove strictly dominated alternatives **simultaneously** from the current survivor set; never use an order-dependent pairwise sorting routine. Retain identical and incomparable alternatives for the next criterion. A later criterion cannot revive an alternative eliminated by an earlier one. This explicitly defines continuation for incomparable coverage sets and avoids arbitrary need weights or cyclic pairwise sorting.

If a lower criterion selects a unique survivor from higher-criterion incomparables, use it and retain the incomparability record. If multiple final survivors remain, canonical selection is permitted only if their comparisons at all six criteria were genuine equalities. Otherwise the component has an unresolved substantive incomparability: keep the currently safe configuration, DEFER the disputed change and record the undelivered needs and relevant reevaluation triggers. This is the adopted abstention policy, not a missing seventh criterion. Basic help and required service functions remain available. No bounded eventual resolution is claimed without evidence or preference changes.

### Canonical equality tie

For a genuine six-criterion tie, normalise each alternative as a sorted sequence of `(catalogue version, ActionID, VariantID, scope ID, typed canonical parameters)` tuples; parameter keys and declared sets are sorted, ordered lists retain order, strings use one specified Unicode normal form (NFC), and numeric values use exact canonical decimal representation. Compare the resulting tuples lexicographically by Unicode code-point order and numeric value for numeric fields, with shorter prefix sequences first. Select the smallest. This key is a **reproducibility mechanism**, not an accessibility priority.

First deduplicate alternatives with identical typed effects and transition effects, retaining all action/need/evidence provenance through COMBINE. Different effects with six genuine equalities may use the canonical key. Unknown is never a tie, and incomparability is never relabelled as genuine equality. The trace retains every tied alternative, all comparator results and the key.

## 5 Final invariant interpretation INV-CD1

### Village-service instantiation contract

Use a simulated village administrative application with versioned service selection, requirements/instructions, data entry, document upload, review, authorised simulated submission and status inspection. This is a contract for the research instantiation, not an assertion about a particular village's legally prescribed SOP. The instantiated manifest declares stable service/step/field/document IDs, dependency edges, required functions and information at each logical stage, validation predicates, authorised events and server-status transitions. Specific field names and document types are fixture data; their identities, semantic types and constraints must be fixed per service version.

S records: entered values by FieldID (including temporarily hidden conditional fields), upload content/reference and status, selected service/options, logical current step, completed valid prerequisites, validation truth, focus/selection/composition buffer, reading anchor, open disclosures, draft identity/version, pending request IDs, idempotency keys, transaction status and explicit user authorisation. U remains four-dimensional; S is not a fifth U dimension.

An adaptation-only transition has no user edit, service-version change or independent server-state event inside its snapshot. If such an event races the transition, reject that stale application and reevaluate; do not call the external change an adaptation-induced loss. Concurrency control is an implementation choice, but that boundary is mandatory.

| Invariant | Predicate bound to the service contract | O5 witness and failure example |
| --- | --- | --- |
| INV-01 Preservation of entered data | For every entered FieldID, post-state preserves the same typed semantic value or a declared lossless round-trip representation. Upload references/content identity and draft ownership are preserved. Hidden conditional fields are not deleted by layout adaptation | Compare canonical before/after field maps and upload/draft identities; fail if staged-flow conversion drops a previously entered hidden value |
| INV-02 Preservation of valid task/progress state | Service choice, satisfied prerequisite set, valid completion facts, current logical position and server truth are unchanged by adaptation alone. Presentation stage indices may differ only through a total manifest-defined mapping to the same logical step. Additional display of validation messages may not falsify previously valid data | Compare logical step and completion/validation facts; fail if regrouping marks a completed requirement unfinished or advances past an unmet prerequisite |
| INV-03 Protection of active unfinished input | A change touching an active input scope must preserve control identity, edit buffer, selection/caret and composition state without blur, unmount or reordering of that scope. Otherwise it must wait for an acknowledged user edit completion/cancellation and safe point. Independent changes outside the scope are allowed only with proven noninterference | Start an unfinished text/IME edit; request restructuring; expect no mutation of that scope and DEFER. A passive note outside the scope may proceed if noninterference holds |
| INV-04 Required functionality and information | At each logical stage, every manifest-required function/information object remains reachable through a finite declared UI navigation path whose controls are available under current constraints. An unavailable real service function must retain its status and recovery/alternative explanation. Optional collapse cannot hide the only error, requirement, safe-submit or status route | Traverse the declared reachability graph; fail if a collapsed navigation group removes the sole required route. Restrict submit while unsafe, but expose why and the permitted next action |
| INV-05 No adaptation-induced invalid or unauthorised irreversible state | Post-state satisfies the manifest's service constraints. UI adaptation cannot issue a new submission, delete/replace user data, change eligibility, skip required validation or alter authorisation. A retry may only continue the same previously authorised logical request with the same idempotency identity and a reconciled status permitting retry | Inject timeout with ambiguous server result: no new submission identity and no automatic resend before permitted status reconciliation; server validation and duplicate prevention remain active |

All five predicates are three-valued: true, false or unknown. Any false rejects the immediate alternative; any unknown prevents claiming admission. Preserve a safe snapshot and independently known safety controls. Rollback restores presentation and recoverable local state; it does not pretend to undo an irreversible server transaction. If the current configuration becomes unsafe because the external service changes, maintain data and block unsafe operations rather than merely preserving an invalid UI unchanged.

The semantic predicate definitions are current refinements. Concrete versioned fixture values and graph instances are supplied for O5 testing before execution. They may instantiate these predicates; they may not redefine what preservation or authorised submission means.

## 6 Final TRANSFORM and DEFER semantics

### TRANSFORM

`TRANSFORM(A,v)` is available only when v is explicitly listed in A's versioned contract as a permitted representation, parameterisation or realisation. Its declared guard must hold; its postconditions must preserve A's support purpose, the relevant scoped need provenance and INV-01–05. A variant can reduce a particular optional coverage effect only if its contract declares that effect and the resolver recomputes coverage; it may not conceal the loss or claim equivalent support when it is not equivalent.

Transform output retains the original ActionID plus VariantID, parameter values, source NeedIDs/edge evidence, and variant justification. It creates no new support function or catalogue identity. Components used to combine two existing actions retain both identities. A composed presentation is legal only when the involved contracts declare compatible shared realisation; its data and effects are checked jointly.

No variant listed means **TRANSFORM unavailable**, not permission to synthesise one. Identity realisation is KEEP. Default/off states that remove the support purpose are not automatically valid transformations just because they are legal property values. A lossless format conversion must be a declared variant, not an inferred license to rewrite information.

UAIS-CAT-1.0 now declares the permitted guidance, term, cue/progress, example/media, reduction-scope, grouping and recovery/review variants, with explicit guards and coverage. Other actions have an empty closed transformation list. A transformation cannot create a new action, query, retry or submission function.

### DEFER and reevaluation

DEFER creates a record `(decision ID, component scope, target reference, blocker, source snapshot versions, release triggers, predecessor ID)`. Triggers include relevant context/capability evidence, scoped edit completion, service-state changes, assistance closure/resumption, connectivity recovery events, and a new parameter/catalogue version. No time-based trigger is invented where the contract has no timer. A stale-target record is never directly executed.

On a relevant trigger run:

`current Context → derived states → justified Need → Rule → candidate actions → resolver → current execution admissibility`.

Always create or link a successor decision. The predecessor becomes superseded by that decision; the successor may again be DEFER, or may select KEEP/COMBINE/TRANSFORM/SUPPRESS. Superseded is a lifecycle status, not a sixth resolver operation. A candidate no longer justified is SUPPRESS with its reason, or an unchanged valid state is recorded by KEEP as appropriate; the old record does not vanish. A successful application refers to the new decision, never to blind replay of the old target.

Immediately before commit, confirm the decision's relevant context/service/input/episode/version tokens still match. If any relevant token changed, commit no mutation, create a fresh deferred successor and reevaluate. Candidate and execution traces preserve the rejection. Implementation may use transactions, version checks or equivalent mechanisms; the no-stale-commit property is fixed.

**Conditional liveness:** assuming relevant events are delivered and processed, each trigger produces a linked reconsideration outcome; the deferred record cannot be silently abandoned. No unconditional execution guarantee exists if the need clears, admissibility never becomes true, evidence remains unknown, or alternatives remain substantively incomparable. No-feasible handling preserves data, exposes status and blocks risky operations. These execution safeguards do not expand the action catalogue or resolver operation list.

### Required trace delta TRACE-CD1

Import the historical observation/decision/execution schemas. Add component version aliases; scoped need IDs and evidence quality; current/previous C1.3 state and request/episode/event references; variant and canonical property dictionaries; invariant vector; READY/WAIT/BLOCKED/UNKNOWN classification and blocker; K/D/T sets and change atoms; per-criterion result including genuine_equal/incomparable; complete survivor/tie provenance; and predecessor/successor plus commit-token checks. Missing required fields make a verification trace incomplete, not a successful unlogged decision. JSON/SQL layout is implementation detail.

## 7 Mapping import and version delta MAP-CD1

The 84 C→N cells, 51 non-dash edges, 28 N→R cells and 18 non-dash edges are imported from H, not reconstructed. The separate import file retains all historical conditions verbatim. A current runtime mapping is the historical mapping plus the six condition overrides below. There are no new or removed topological edges.

For C1.3→Nk define `A(k)` as fresh, initialized AssistanceNeeded with a pending explicit request of kind k, or fresh Recovering with a retained request-of-kind-k provenance in the unresolved recovery episode. Scope must match the task/information to which the need relates. Stable and Emerging do not activate these edges. Unknown kind or evidence does not activate them, and a generic help request cannot infer all N1–N6.

| Changed edge | Historical condition | Current condition | Delta class | Rationale | Version identity |
| --- | --- | --- | --- | --- | --- |
| C1.3→N1 | Explicit clarification request; AssistanceNeeded or supported Recovering | A(clarification) and identified term/information scope | Modified condition | Bind recovery support to current episode and four-state machine | H F.2.2 → MAP-CD1 / C13-CD1 |
| C1.3→N2 | Explicit request for step guidance | A(step guidance) and identified process scope | Modified condition | Preserve request provenance; preview is insufficient | H F.2.2 → MAP-CD1 / C13-CD1 |
| C1.3→N3 | Explicit orientation/navigation request | A(orientation) and identified logical location scope | Modified condition | Current state and freshness become explicit | H F.2.2 → MAP-CD1 / C13-CD1 |
| C1.3→N4 | Explicit reminder request | A(reminder) and identified information/reference scope | Modified condition | Retain reminder support only within its recovery episode | H F.2.2 → MAP-CD1 / C13-CD1 |
| C1.3→N5 | Explicit choice-support request | A(choice explanation) and identified choice scope | Modified condition | Avoid ungrounded decision-support inference | H F.2.2 → MAP-CD1 / C13-CD1 |
| C1.3→N6 | Explicit correction/recovery-help request | A(correction assistance) and identified correction scope | Modified condition | Help request is distinct from an automatically counted error | H F.2.2 → MAP-CD1 / C13-CD1 |
| Other 45 non-dash C→N edges | Recovered historical conditions | Imported unchanged | Unchanged | No change to their evidence-to-need relationship | H F.2.2 imported into MAP-CD1 |
| All 33 dash C→N cells, including C1.3→N7 and all C2.1 edges | No direct relation | No direct relation | Unchanged | Prevent new need links or device proxies | H F.2.1 imported into MAP-CD1 |
| All 18 non-dash N→R edges | Recovered historical conditions | Imported unchanged | Unchanged | Families retain their purposes; no action-count-driven edge edits | H F.3.2 imported into MAP-CD1 |
| All 10 dash N→R cells | No relation | No relation | Unchanged | Preserve topology | H F.3.1 imported into MAP-CD1 |

Evidence-completeness rule: evaluate the complete conjunction of the source condition and its stated task/evidence requirement; a tick does not remove that requirement. A narrative condition must be backed by a named observation or manifest fact. Unknown is not false evidence of user ability and is not silently replaced by a designer's guess. When a concrete service cannot supply a predicate witness, that edge is unknown for that decision. Existing true edges may still justify the same N. No imported condition is silently converted into a new duration, error or score threshold.

For C3.3 retain the historical derivation. This record additionally resolves unknown gaps operationally: an unknown/misaligned observation breaks a consecutive recovery sequence and cannot complete Normal; preserve the last known risk phase as history. After a known risk episode, the first fresh good aligned observation following such a gap starts/restarts Recovering and only the next good aligned observation completes Normal. A new bad aligned observation selects AtRisk/Disrupted under the historical table. Without a prior risk episode, a fresh good initial observation can establish Normal. This is a current conservative sequence clarification, identified as `C33-GAP-CD1`, not a newly calibrated threshold. It does not add C→N edges.

## 8 Verification Delta Matrix VER-DELTA-CD1

The original 35 principal cases are imported unchanged into the historical record. Their input and expected-behavior text are preserved in the separate import. The matrix below describes current child expectations, not edits to historical test history and not execution results.

Oracle labels: O1 context/instrument classification; O2 need/rule/candidate decision; O3 resolver/admissibility/comparison; O4 temporal sequence and reevaluation; O5 invariant/service-state predicates; End-to-End spans the complete chain. O3 may test the invariant gate while O5 checks the actual predicate and state preservation. One case can map to several oracles.

Use child IDs such as `UAIS-S3-CD1/V1-03/a`, with `parent=H:V1-03`. All new child subcases are **not run**. The current total of child subcases is not fixed by this decision record. Catalogue-specific child expectations are completed in VER-CAT1. All child cases remain not run; concrete fixture IDs/builds instantiate the fixed contracts before execution.

| Original CaseID | Original purpose | Affected by refinement? | Reason | Current oracle mapping | Expected outcome unchanged / revised | Additional subcase required? |
| --- | --- | --- | --- | --- | --- | --- |
| V1-01 | Experience categories and boundaries | No | Experience rule unchanged | O1 | Unchanged | No refinement-specific addition |
| V1-02 | ISS scoring/reversal/missing | No | Continuous dimensions and missing policy retained | O1 | Unchanged | No refinement-specific addition |
| V1-03 | Assistance state sequence | Yes | New C13-CD1 events, initialization and quality metadata | O1, O2, O4 | Revised in current children | Yes: all seven legal edges, self-events, help-kind unknown, duplicate/gap/scope change, and excluded duration/error triggers |
| V1-04 | Device descriptor does not activate needs | No | All seven C2.1 dash cells retained | O1, O2 | Unchanged | No refinement-specific addition |
| V1-05 | Reflow and unavailable evidence | No | 320 CSS px test is not a direct activation breakpoint | O1, O2 | Unchanged | No refinement-specific addition |
| V1-06 | Required-feature classification | No at classification level | Supported/Limited/Unknown unchanged; feasibility consumers tested elsewhere | O1 | Unchanged | No refinement-specific addition |
| V1-07 | 2/4-second boundaries | No | Exact intervals and no rounding preserved | O1 | Unchanged | No refinement-specific addition |
| V1-08 | Timeout/unknown/validation error | No | Connectivity evidence distinction preserved | O1 | Unchanged | No refinement-specific addition |
| V1-09 | Logical-chain stability events | No | Stable/Unstable/Unknown unchanged | O1 | Unchanged | No refinement-specific addition |
| V1-10 | C3.3 risk derivation | No for original aligned pairs | Historical risk table retained | O1 | Unchanged | No new pair classification required |
| V1-11 | Connectivity recovery | Yes | C33-GAP-CD1 resolves interrupted recovery sequence | O1, O4 | Original clean sequence unchanged; gap expectations refined | Yes: unknown between good observations, restarted recovery and relapse |
| V1-12 | Service vectors and null/empty | No | No aggregate complexity thresholds introduced | O1 | Unchanged | No refinement-specific addition |
| V1-13 | Full C→N matrix and conditions | Yes | Six C1.3 conditions revised; topology unchanged | O2 | Revised only for changed conditions | Yes: six edge overrides with true/false/unknown and all other cells regression-tested |
| V1-14 | ISS/device alone cannot activate N/R | No | Current C1.3 policy introduces no score proxy | O2 | Unchanged | No refinement-specific addition |
| V1-15 | Full N→R matrix | No topological/condition change | Imported 18 non-dash conditions | O2 | Unchanged for fixed N inputs | No new relation; rerun original conditional combinations |
| V2-01 | 24-action legal values and guards | Yes | Final merged R2.A2, separate R3.A7 and complete UAIS-CAT-1.0 contracts | O2, O3, O5 | Revised under UAIS-CAT-1.0 | Yes: current 24 contracts, coverage, variants and READY/WAIT/BLOCKED/UNKNOWN |
| V2-02 | Compatible term help plus autosave | Yes, additional precision | Same compatibility intent; scoped effects and joint invariants | O3, O5 | Original KEEP/COMBINE intent unchanged | Yes: shared provenance, independent vs coupled scope |
| V2-03 | Cue/progress composition | Yes | Shared realisation must be declared, not assumed | O3, O5 | Revised to contract-specific result | Yes: legal composition and undeclared-variant rejection |
| V2-04 | Density versus full guidance | Yes | Six criteria, declared variant and current feasibility | O3, O4 | Revised under UAIS-CAT-1.0 | Yes: ready, temporary block, unknown and absent legal transform |
| V2-05 | Grouping inside staged flow | Yes | Final R2.A3 within-stage variant and shared state mapping | O3, O5 | Revised under UAIS-CAT-1.0 | Yes: legal scope mapping and illegal cross-stage transformation |
| V2-06 | Media/text equivalence under bandwidth limits | Yes | Text variant must have a declared support-preserving contract | O3, O5 | Revised to explicit variant/coverage result | Yes: legal equivalent, unsupported conversion and missing equivalence evidence |
| V2-07 | Unsafe retry | Yes | INV-05 and temporary versus contract-infeasible distinction | O3, O4, O5 | Safety intent unchanged; exact SUPPRESS/DEFER refined | Yes: unresolved status WAIT, forbidden retry BLOCKED, changed version before commit |
| V2-08 | Essential functions survive simplification | Yes | Final R2.A2 merged scopes; INV-04 reachability is explicit | O3, O5 | Safety intent unchanged; action-specific result revised | Yes: required route reachability and catalogue delta regression |
| V2-09 | Recovery panel plus review | Yes, additional precision | Joint postconditions and retained status distinctions | O3, O5 | Original COMBINE intent unchanged | Yes: permitted combined realisation and ambiguous status rejection |
| V2-10 | All rule combinations | Yes | Same 15 nonempty combinations plus none; current candidate/resolver policy differs | O2, O3, End-to-End | Revised at action/resolver level | Yes: fixed needs for all combinations, unknown guards and UAIS-CAT-1.0 outcomes |
| V2-11 | Minimum-change and tie-break | Yes | Six criteria, typed changes, genuine equality restriction | O3 | Revised | Yes: strict-superset coverage, incomparables, all criteria, unknown, equal keys, permutation independence |
| V2-12 | No feasible configuration | Yes | WAIT/BLOCKED/UNKNOWN and incomparable abstention separated | O3, O4, O5 | Safety intent unchanged; outcome classification refined | Yes: each infeasibility class and safe hold after unresolved incomparability |
| V3-01 | Data preservation | Yes, predicate precision | INV-01/02 bound to field/upload/logical-stage identity | O5 | Preservation intent unchanged | Yes: conditional hidden values, uploads and lossless representation |
| V3-02 | Duplicate submission prevention | Yes, predicate precision | Same authorised request identity and status reconciliation | O4, O5 | No-duplicate intent unchanged | Yes: unknown result, replay and new unauthorised request rejection |
| V3-03 | Safe, same-target and unsafe transition | Yes | Active input, fresh commit and no-op semantics | O3, O4, O5 | Refined | Yes: unfinished composition, independent scope, target no-op and stale snapshot |
| V3-04 | Rollback | Yes, boundary precision | Local rollback is not reversal of server transactions | O4, O5 | Local restoration intent unchanged | Yes: partial apply, restore failure, external event race and preserved server truth |
| V3-05 | Recovery continuity | Yes | C13-CD1, C33-GAP-CD1 and fresh deferred targets | O4, O5 | Refined | Yes: assistance/network recovery separation, relapse and obsolete deferred target |
| V3-06 | Full traceability | Yes | TRACE-CD1 adds comparison/variant/episode/successor evidence | O2, O3, O4, O5, End-to-End | Revised trace requirements | Yes: full applied, deferred, superseded and suppressed chains |
| V3-07 | Version integrity and repeatability | Yes | Current component versions, canonicalisation and source tokens | O3, O4, O5 | Revised manifest/trace requirements | Yes: identical snapshots, mismatched versions and input-order permutation |
| V3-08 | Invariants shared by adaptive and non-adaptive conditions | Yes, explicit predicates | Basic safety must not be made exclusive to adaptation | O5, End-to-End | Equal baseline protection unchanged | Yes: same service manifest and INV-01–05 across both conditions |

Concrete child expectations follow the fixed policies: unknown higher evidence never becomes a tie; strict-superset coverage wins before lower criteria; incomparable coverage is retained for declared lower comparisons; incomparable final survivors do not use the canonical key; a stale decision makes no mutation; a missing transform declaration forbids transformation; closing help alone cannot exit Recovering; and a C3 unknown gap cannot complete Normal. No historical pass count is imported as evidence for these refined expectations.

## 9 Final consistency audit and remaining work

The catalogue decision closes the remaining behavioural gap. The final catalogue, current mapping delta, comparator policy, invariant predicates, transform closure, event-based assistance/recovery rules and TX-1 service-event boundaries define the specified outcomes. No remaining action identity, coverage domain, comparator weight, transform permission or retry/status policy is left for an implementer to invent.

| Component | Final consistency finding |
| --- | --- |
| C→N | Historical 84-cell matrix and 51 non-dash edges preserved, with only the six recorded C1.3 condition overrides |
| N→R | Historical 28-cell matrix and 18 non-dash edges preserved; every declared action NeedCoverage has an existing edge to its family |
| Catalogue | 24 unique current IDs; 6–5–7–6; H:R2.A6 retained as merge provenance, not an executable current action |
| R3.A7 | Scoped N6/N7→R3 nomination required; read-only status attempt; no inline retry or fabricated completion |
| Resolver | Six frozen-order lexicographic criteria; unknown and incomparability distinct from genuine equality; fixed typed change atoms |
| Invariants | Entered values, valid logical state, active input, required routes and authorised effects protected; server responses treated as evidenced external events |
| TRANSFORM | Explicit finite variant identities with closed scoped parameters; empty lists are prohibitions, not missing definitions |
| DEFER | Fresh full-chain reevaluation, current commit tokens and predecessor/successor trace; no stale-target replay |
| Traceability | TRACE-CD1 extended by TRACE-CAT1, including merged identity, support object, query/permit/result and baseline-safety origin |
| Verification | Original 35 parents preserved verbatim; current catalogue/transaction child expectations added under VER-CAT1 and marked not run |

Remaining work is implementation and evidence production: instantiate service IDs/resources/fixtures under the declared manifest, implement the system, execute the child cases, report results, and format the manuscript. A missing witness yields the specified UNKNOWN/DEFER behaviour; it does not authorise a guessed guard or constitute an unresolved threshold. User-study effectiveness has not been established by specification closure.

## 10 Final recommendation

**SECTION 3 READY TO LOCK**

The current versioned action-catalogue refinement is integrated and its behavioural contracts are complete. This decision locks the research specification, not empirical findings or test success. Apply the exact manuscript patches supplied with this package. No Section 4 text or implementation is produced in this response.
