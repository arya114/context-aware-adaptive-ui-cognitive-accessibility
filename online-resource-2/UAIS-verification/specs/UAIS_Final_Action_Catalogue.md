# Final UAIS Action Catalogue and Contracts

CatalogueVersion: **UAIS-CAT-1.0**. Adopted 12 September 2026 as a current versioned refinement. Distribution: R1=6, R2=5, R3=7, R4=6; total 24. This is an operational specification, not a record of executed tests or empirical effectiveness.

## Version delta and identity

Historical H:R2.A2 Collapse Optional Elements and H:R2.A6 Collapse Secondary Navigation are **merged into current R2.A2 Contextual Secondary/Optional Content Reduction**. H:R2.A6 is not an executable current identifier and is not moved to R3. Its provenance remains attached to R2.A2 and its navigation scope.

Current R3.A7 Transaction Status Reconciliation is the explicit action-level separation of a continuity requirement previously embedded in status-checking, unsafe-retry and recovery requirements. It has no historical ActionID. All other historical action purposes are retained, with explicit current guards and parameters below. The count is 24 historical actions minus one merged identity plus one separately formalised continuity identity = 24 current actions.

The four U dimensions retain their meanings: G Guidance; D Density/Presentation; P Protection/Continuity; F Flow Structure. R3.A7's configurable interaction policy belongs to P. Actual authoritative transaction state belongs to S and does not create a fifth U dimension.

## Common contract clauses

These clauses apply normatively to every complete contract below. An empty transformation list is a closed declaration that no transformation is permitted; it is not an unfinished field.

- **CG-1 Need mediation:** at least one declared NeedCoverage instance must be currently justified by a true current C→N edge and nominate the action's RuleSource through a true imported N→R edge. Match service version and task scope. A timeout, click, device label or action request alone cannot replace that chain. An action cannot activate a need or nominate its own rule. Candidate conditions and NeedCoverage are distinct: a candidate does not automatically establish coverage.
- **CG-2 Scoped coverage:** coverage is the intersection of declared need kinds, currently justified scoped needs, and effects guaranteed by this permitted realisation at the current scope. It describes an available support capability, not successful human comprehension, symptom reduction, task completion or resolution of the need. Recompute it after scope/variant changes. R3.A7 guarantees a safe attempt and honest uncertainty handling, not that the server will return a known result. It must never count unknown transaction truth as established truth. A WAIT target contributes no currently delivered effect; installed support can contribute its actually available capability. An effect available equally in the default condition is not counted as an extra empirical advantage.
- **CG-3 Versioned inputs:** service manifest, relevant observations, snapshot and action parameters are coherent. The manifest identifies every field/control/content/asset/stage/transaction, required function/information set, dependency graph, semantic equivalence map and declared parameter scope. Unsupported/missing witnesses give UNKNOWN, not a guessed positive guard. Concrete identifiers and resource content instantiate this contract; they may not redefine it.
- **CG-4 Admissibility:** INV-01–INV-05 must all be demonstrably true for the proposed transition. False rejects an immediate plan; unknown prevents execution. A separate DEFER plan may preserve current safe state while a temporary blocker remains. No lower comparator can compensate for a failed invariant.
- **CG-5 Realisability:** capability and viewport checks show that required information/controls are reachable, relevant content reflows without loss under the adopted C2.2 procedure, and offered service operations are authorised. Space sufficiency is this functional/reflow check, not a new numeric breakpoint. Known unknown states may be displayed honestly; the absence of evidence of a control's safety is not permission to enable it.
- **CG-6 Exclusions:** a known forbidden value, wrong service/owner, lost essential content, invalid identity, unauthorised effect or lack of any legal implementation in the current service/contract excludes that target. Record SUPPRESS and the reason. 'Permanent' means the current contract/capability cannot realise that target by merely waiting for a declared runtime release event; a new service/capability/need/version can generate a new decision. Absent relevant need means no candidacy or SUPPRESS of an obsolete candidate, not indefinite waiting for that old decision.
- **CG-7 Temporary/unknown blockers:** name the actual release event: scoped input completion, fresh manifest/observation, feature/network recovery, authorised user response, compatible snapshot, request completion or a new transaction permit. Classify known temporary blockers WAIT; missing evidence UNKNOWN. Neither is a ready target. DEFER requires fresh reevaluation and successor links. No guessed delay, polling interval or hidden counter is introduced.
- **CG-8 Compatibility:** different targets may compose only when their joint postconditions hold. Conflicting values for one canonical property require alternatives; duplicate identical effects are deduplicated with all provenance retained. Shared components require reciprocal declared variants. A compatible pair is not labelled a conflict merely because two rules are active. Cross-action effects on required paths, focus, data, stage identity and transaction state are checked jointly.
- **CG-9 Transition safety:** use the current RES-CD1 lexicographic policy, INV-CD1, C13-CD1, C33-GAP-CD1 and MAP-CD1. A changed relevant context/input/service/episode token before commit prohibits stale execution. Relevant changes rerun Context→derived state→Need→Rule→Action→Resolver→admissibility. Never withdraw support simply because its last evidence became unavailable. Safe withdrawal follows current need evidence and recovery guards. Canonical ties require genuine equality at all six criteria; unknown/incomparable survivors are not canonical ties.

## Complete parameter and transformation domain

**Coverage scope binding:** a task scope includes a manifest-declared support-object ID, not only a broad transaction or page ID. In the transaction fixture, `X/status-determination`, `X/status-communication`, `X/permitted-retry`, `X/recovery-controls` and `draft-X/resumption` are different support objects within the same task. The existing C→N edges justify N6/N7 over the affected objects; the action contract must match the need's object and required support effect. Thus R3.A5's honest unknown message covers communication, not status-determination; R3.A7's safe check covers the determination-support operation, not feedback or a promised successful response. R3.A2 does not cover a determination obligation by being blocked. This is scoped operationalisation of existing needs, not new N types or new C→R edges. Object identities and required effects are fixed in the service manifest before verification, never manufactured by a candidate to improve its coverage score. The comparator uses strict set inclusion, not the number of these objects. A requirement already delivered by a baseline function is not credited again as additional coverage.

Each mode enumeration below is closed. Scope values are only identifiers in the current versioned service manifest. Declared multi-element scope can contain any nonempty eligible subset; it is a parameterisation of one action, not a family of new ActionIDs. Multiple instances retain one ActionID and separate scoped provenance. Repeated effects on the same property are counted once.

For actions with a realisation property, `native` is the initial registered rendering and the listed VariantID is the only permitted alternative realisation. Guards for a shared variant must hold reciprocally for the named partner action. The resolver constructs the joint realisation as one plan; it does not wait for each partner to be separately installed. 'No TRANSFORM' forbids synthesising an unlisted conversion, including retry→query or query→submit.

R1.A2's ordinary candidate target is inline when its full display check is true. Otherwise the on-demand variant is eligible only if its own guard is true; if both guards fail/are unknown, the target is excluded/deferred accordingly. Other listed adaptive targets are fixed. R1.A1's legal `on` state can occur in a retained/manual full-guidance configuration; the current default adaptive target is contextual. The full→contextual test therefore starts from a legally retained full-guidance state, rather than inventing an extra automatic activation policy.

For R2.A2, each ElementID has one canonical owner and state even if its semantic labels overlap. Its optional-content, secondary-navigation and nonessential-control scopes are independently selectable. Collapsing a group that contains required information/error/status/recovery or the only route to a required function is prohibited; narrowing to a nonempty eligible subset is the only registered transformation. Expanding an element through its preserved user control is a user interaction, not an automatic reversal of the support decision. The next decision starts from that actual state. Historical optional-elements and secondary-navigation properties become the corresponding scoped current properties; existing values are migrated without resetting unrelated scopes.

## Fixed minimal-change dictionary

The canonical atoms are the property paths listed in each contract, qualified by stable semantic component/ElementID and U dimension. Split semicolon-separated properties into distinct atoms. Read-only status output in S is not a U atom. For R2.A2 use one `D.content.reduction[ElementID].state` atom per manifest-owned element, regardless of which former action or category supplied it. A shared cue/progress or recovery/review plan retains the listed semantic properties and both provenance records; it cannot invent extra action-count units.

Modes and realisation values are compared as exact enums. Compound defaults are expanded to the same typed leaf dictionary before comparison. Missing optional values resolve only to the manifest's declared default; genuinely unknown current values remain unknown. Current U contains values, not the literal phrases 'when eligible' or 'unless required'. For autosave the effective default is on only when support and consent are true, otherwise off with the limitation recorded. For the recovery panel the effective default is visible when required by baseline safety, otherwise hidden. Those predicate outcomes are part of the versioned snapshot. Minimum change is the number of distinct unequal atoms; property granularity never changes to favour a candidate.

## TX-1 Transaction and asynchronous service-event contract

### Identity and status quality

A logical transaction has an existing TransactionID/idempotency key, user-authorisation reference, operation and immutable payload reference. A status query is authorised to read that transaction and has **no service-mutating side effect**. A reliable result must come from the service's authorised status facility, match identity and payload/operation binding, and satisfy its monotonic revision or current request-correlation/freshness contract. A local guess, absent response, generic HTTP 404 or navigator connectivity flag does not establish completion or non-execution. If the service cannot supply sufficient evidence, classify the result unknown. No new endpoint or authority is invented by the framework.

| Reconciled result | Required evidence | Retry policy | R3.A5 feedback |
| --- | --- | --- | --- |
| completed | Reliable completion receipt for this logical transaction | SUPPRESS retry; never create a new identity | Completed, with receipt/reference |
| pending | Reliable record that this transaction is still processing | DEFER repeat submission; await relevant status event | Still processing; completion not confirmed |
| safely_retryable | Reliable service attestation that no committed effect requires preservation and the same authorised idempotent request is permitted; includes a current retry permit | R3.A2 may be nominated/applicable only after a new full-chain decision and final permit check | Retry permitted; do not announce success before its result |
| terminal_rejected | Reliable terminal rejection for this request; no same-request retry permitted | SUPPRESS retry; expose valid correction/new-authorisation route through baseline service controls | Rejected with the evidenced reason |
| unknown | Missing, stale, conflicting, unmatched or insufficiently authoritative evidence | Unsafe repeat submission remains blocked; DEFER eligible reconciliation until a new trigger | Status unconfirmed; do not resend |

One guarded query is dispatched per `(TransactionID, ambiguity epoch, trigger token)`. The token is an explicit user status-check request, an independently observed interruption/recovery/status event, or an independently delivered fresh service status revision. Duplicates do not create another query; an in-flight query excludes a second query for that scope. The query's own completion, failure, timeout, or derived C3 change cannot mint a new trigger token or ambiguity epoch for the same unresolved transaction. They can update evidence and feedback but cannot cause another query without an independent trigger. Completion/repaint of the same decision is not a new token. The policy does not start an unbounded polling loop. A newer transaction/status revision invalidates a stale result. Query transport failure becomes a new unknown result, not success or an automatic write retry.

R3.A7 and R3.A2 cannot issue query and retry commands concurrently for the same transaction. R3.A2 consumes at most one current attempt permit, with the same logical identity, operation, payload and user-authorisation. A lost retry result returns to uncertainty; it cannot self-authorise another retry. Server idempotency/authoritative checks remain the ultimate duplicate-effect guard even if status changes between the read and retry. Lack of these guarantees makes guarded retry inapplicable.

### Need mediation and action separation

Ambiguous/timeout evidence is first evaluated through applicable C→N edges, such as the existing C3.1/C3.2→N6/N7 edges for the relevant request chain, and then N6/N7→R3. R3.A7 is a candidate only with those current scoped justifications plus its transaction guard. Its result is published as a new observation and requires a **new full-chain decision** before R3.A2 or adaptive R3.A5 changes. There is no action→action activation shortcut. An accepted terminal result may clear an adaptive need; required baseline status feedback still displays that result without fabricating a continuing need.

R3.A7 determines status; R3.A2 retries an eligible request; R3.A5 communicates status; R3.A4 exposes recovery controls/state; R3.A6 resumes the user's local draft. These effects are not substituted for one another through TRANSFORM.

### Invariants and command boundaries

An adaptation configuration commit and a subsequent service response are different events. Installing `P.transaction.reconciliation=guarded-query` does not itself assert completed/pending truth. Dispatch is logged under a currently admitted action decision; the response updates S only as an independently validated service-evidence event, recording old/new status and cause. INV-02 protects logical service truth against arbitrary UI edits, not against legitimate new server evidence. The query never mutates server transaction state. INV-05 applies to every outgoing service command.

Similarly, guided draft resumption requires a separately recorded explicit user authorisation and lossless, nonconflicting snapshot restoration; merely enabling the guided UI cannot overwrite data or advance progress. Autosave follows accepted edits; step validation exposes existing predicate results without changing authoritative validation rules.

If target U already equals current U, perform no U mutation. A new eligible query/retry/autosave/resume event may still require a separately guarded, idempotent service interaction. Equality of UI configuration is not blanket permission for that command and is not blanket cancellation of it. The execution trace distinguishes `configuration_noop` from `command_dispatched`, with a current token and invariant checks. This clarifies the historical 'same U: no layout mutation' rule without discarding service-interaction actions.

### Equal baseline safety

Authorisation, server validation, duplicate-effect prevention, honest status feedback, minimum draft protection where supported, and mandatory pre-retry status checking apply in both adaptive and non-adaptive conditions. UAIS R3.A7 makes need-mediated orchestration explicit; it does not make essential transaction safety conditional on adaptation. A baseline safety check is logged with `origin=baseline_safety`, not falsely presented as a C→N→R-selected R3.A7 action. Disabling adaptation never enables an unsafe repeat submission.

## TRACE-CAT1 and verification identity

Extend TRACE-CD1 with CatalogueVersion UAIS-CAT-1.0, merged historical identities, scoped element ownership, variants, change atoms, scoped NeedCoverage witnesses, and TX-1 query/permit/status correlation. Required trace lineage is observation→C→C→N edge→N→N→R edge→R→action→resolver→execution→new observation, with deferred predecessors/successors and any baseline safety origin labelled separately. New status evidence is not counted as a prior decision's assumed result.

The historical 35 principal cases remain unchanged. `CAT1/...` references identify current child specifications in the final verification delta. Every child is **not run**. Catalogue/schema consistency checks are not technical verification passes of the adaptive system.


## Complete contracts for all 24 actions

### R1.A1 Contextual Guidance

| Contract field | Specification |
| --- | --- |
| ActionID | R1.A1 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R1 |
| HistoricalProvenance | H-PROP-20260908 F.4 R1.A1; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Provide instructions at the relevant task location. |
| NeedCoverage | **declared**: {"N1": "Expose the referenced explanation.", "N2": "Expose the referenced process instruction."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R1 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | G.guidance.visibility |
| Legal parameters/values | **mode**: ["off", "on", "contextual"]; **scope**: Declared instruction/task anchor |
| Default/current state | **default**: off; **adaptive_target**: contextual; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and A scoped instruction object and its task anchor exist; the current presentation passes display/reachability checks. |
| Permanent exclusions | CG-6 and No valid instruction for this service/version; effect would replace mandatory instructions with an incomplete alternative. |
| Temporary blockers | CG-7 and Instruction/anchor evidence unknown or affected input not at a safe point. |
| ExpectedEffect | Expose contextual guidance without changing data or service sequence. |
| Postconditions | INV-01–INV-05 and Required instruction content remains accessible; no input values, selection or progress change. |
| Compatibility constraints | CG-8 and R2 reduction cannot remove its only access; guidance and step cues must reference the same logical task. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "contextual", "change": "on → contextual", "guard": "All required instruction IDs remain reachable through the same scoped anchor; no simultaneous-display requirement is lost.", "preserved_effect": "The same instruction content is offered in context."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R1.A1<br>H:V2-04<br>CAT1/V2-04/guidance |

### R1.A2 Term Explanation

| Contract field | Specification |
| --- | --- |
| ActionID | R1.A2 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R1 |
| HistoricalProvenance | H-PROP-20260908 F.4 R1.A2; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Explain service terminology. |
| NeedCoverage | **declared**: {"N1": "Make the scoped term definition accessible."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R1 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | G.term.explanation |
| Legal parameters/values | **mode**: ["hidden", "on-demand", "inline"]; **scope**: TermID with versioned definition |
| Default/current state | **default**: on-demand; **adaptive_target**: inline when display supports it; otherwise declared on-demand variant; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and A version-matched definition exists for the term. |
| Permanent exclusions | CG-6 and No definition or inaccurate/unapproved content. |
| Temporary blockers | CG-7 and Definition version or current display feasibility unknown. |
| ExpectedEffect | Offer the correct term explanation. |
| Postconditions | INV-01–INV-05 and The term meaning and surrounding required instructions are preserved. |
| Compatibility constraints | CG-8 and Compatible with autosave; inline content must respect density/reflow. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "on-demand", "change": "inline → on-demand", "guard": "A labelled reachable control provides exactly the same definition; access does not require unavailable capabilities.", "preserved_effect": "The definition remains available."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R1.A2<br>H:V2-02<br>CAT1/V2-02/compatible |

### R1.A3 Step Cue

| Contract field | Specification |
| --- | --- |
| ActionID | R1.A3 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R1 |
| HistoricalProvenance | H-PROP-20260908 F.4 R1.A3; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Explain current and next logical steps. |
| NeedCoverage | **declared**: {"N2": "Show the next permitted step cue.", "N3": "Show the current logical location when its conditional N3→R1 edge is true."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R1 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | G.step.cue; G.step.cue.realisation |
| Legal parameters/values | **mode**: ["compact", "full"]; **realisation**: ["native", "shared-progress"]; **scope**: Logical StepID |
| Default/current state | **default**: {"mode": "compact", "realisation": "native"}; **adaptive_target**: {"mode": "full", "realisation": "native"}; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Versioned cue text and logical current/next-step identities exist. |
| Permanent exclusions | CG-6 and Cue contradicts prerequisites or invents completed progress. |
| Temporary blockers | CG-7 and Logical stage or affected editing scope unresolved. |
| ExpectedEffect | Present a full step cue bound to true logical progress. |
| Postconditions | INV-01–INV-05 and Current step and progress facts unchanged. |
| Compatibility constraints | CG-8 and May share one control with R4.A2 only under reciprocal shared-progress declarations. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "shared-progress", "change": "realisation native → shared-progress; mode remains full", "guard": "R4.A2 is independently nominated, its indicator is on, and both refer to the same StepID/progress object; all cue text is preserved.", "preserved_effect": "One consistent component retains full cue and progress information."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R1.A3<br>H:V2-03<br>CAT1/V2-03/shared |

### R1.A4 Examples

| Contract field | Specification |
| --- | --- |
| ActionID | R1.A4 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R1 |
| HistoricalProvenance | H-PROP-20260908 F.4 R1.A4; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Provide valid contextual examples. |
| NeedCoverage | **declared**: {"N1": "Provide a comprehension example.", "N5": "Provide an example explaining a choice.", "N6": "Provide an example supporting correct input."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R1 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | G.example.visibility; G.example.realisation |
| Legal parameters/values | **mode**: ["hidden", "on-demand"]; **realisation**: ["native", "text-equivalent"]; **scope**: ExampleID; no generated unapproved example |
| Default/current state | **default**: {"mode": "hidden", "realisation": "native"}; **adaptive_target**: {"mode": "on-demand", "realisation": "native"}; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Example is valid for the current field/choice and service version. |
| Permanent exclusions | CG-6 and Invalid example, or conversion omits a required semantic element. |
| Temporary blockers | CG-7 and Example mapping/reachability or active input scope unknown/unsafe. |
| ExpectedEffect | Expose an on-demand example. |
| Postconditions | INV-01–INV-05 and Example never pre-fills or overwrites user data. |
| Compatibility constraints | CG-8 and May use text-equivalent with low-bandwidth profile; optional collapse must preserve its help control. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "text-equivalent", "change": "native media → registered text-equivalent", "guard": "Versioned ExampleID maps every required instruction/choice/error-prevention content ID to a text element; text is accessible and no indispensable visual-only element is omitted.", "preserved_effect": "Same declared support purpose and scoped coverage; no claim of empirically equal effectiveness."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R1.A4<br>H:V2-06<br>CAT1/V2-06/text |

### R1.A5 Contextual Help Access

| Contract field | Specification |
| --- | --- |
| ActionID | R1.A5 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R1 |
| HistoricalProvenance | H-PROP-20260908 F.4 R1.A5; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Expose task-relevant help access. |
| NeedCoverage | **declared**: {"N1": "Access clarification.", "N2": "Access process guidance.", "N3": "Access orientation help if conditional edge true.", "N5": "Access choice explanation."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R1 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | G.help.access |
| Legal parameters/values | **mode**: ["standard", "contextual"]; **scope**: Task/NeedKind anchor |
| Default/current state | **default**: standard; **adaptive_target**: contextual; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and A help route and appropriate help kind exist. |
| Permanent exclusions | CG-6 and Contextual route unavailable with no valid destination. |
| Temporary blockers | CG-7 and Current help-kind/scope binding unknown. |
| ExpectedEffect | Expose the relevant help request control. |
| Postconditions | INV-01–INV-05 and Standard help remains reachable; opening a preview does not itself confirm a need. |
| Compatibility constraints | CG-8 and Uses C13-CD1 preview/request event distinction; no direct R1 activation by the control. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R1.A5<br>H:V1-03<br>CAT1/V1-03/help |

### R1.A6 Contextual Error Explanation

| Contract field | Specification |
| --- | --- |
| ActionID | R1.A6 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R1 |
| HistoricalProvenance | H-PROP-20260908 F.4 R1.A6; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Explain an observed validation/service error and its correction. |
| NeedCoverage | **declared**: {"N6": "Expose the current error and valid correction instruction."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R1 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | G.error.explanation |
| Legal parameters/values | **mode**: ["standard", "contextual"]; **scope**: ErrorID/FieldID or service error reference |
| Default/current state | **default**: standard; **adaptive_target**: contextual; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and An actual error with a versioned correction reference exists. |
| Permanent exclusions | CG-6 and Fabricated error, changed validation rules or speculative correction. |
| Temporary blockers | CG-7 and Error/field version mismatched or source unknown. |
| ExpectedEffect | Add contextual explanation to baseline error feedback. |
| Postconditions | INV-01–INV-05 and Raw values, validation truth and error identity preserved. |
| Compatibility constraints | CG-8 and Does not retry, reconcile a transaction or suppress required error/status feedback. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R1.A6<br>H:V2-08<br>CAT1/V2-08/protected |

### R2.A1 Reduce Interface Density

| Contract field | Specification |
| --- | --- |
| ActionID | R2.A1 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R2 |
| HistoricalProvenance | H-PROP-20260908 F.4 R2.A1; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Reduce nonessential presentation density. |
| NeedCoverage | **declared**: {"N1": "Expose relevant information with reduced nonessential density.", "N3": "Make current navigation/location content discernible."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R2 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | D.layout.density |
| Legal parameters/values | **mode**: ["standard", "reduced"]; **scope**: Versioned layout region |
| Default/current state | **default**: standard; **adaptive_target**: reduced; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and A registered reduced presentation preserves required content, order and functionality and passes reflow. |
| Permanent exclusions | CG-6 and Reduced form deletes required content, breaks logical order, or has no permitted rendering. |
| Temporary blockers | CG-7 and Space/anchor mapping unknown or active input restructuring blocked. |
| ExpectedEffect | Render the same essential task content in reduced-density form. |
| Postconditions | INV-01–INV-05 and Values, focus during active input and required routes preserved. |
| Compatibility constraints | CG-8 and Full/contextual guidance jointly checked; density does not override help or error requirements. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R2.A1<br>H:V2-04<br>CAT1/V2-04/guidance |

### R2.A2 Contextual Secondary/Optional Content Reduction

| Contract field | Specification |
| --- | --- |
| ActionID | R2.A2 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R2 |
| HistoricalProvenance | H:R2.A2 Collapse Optional Elements + H:R2.A6 Collapse Secondary Navigation → current R2.A2 by explicit user decision of 12 September 2026. Nonessential controls are an explicitly declared scope of this current granularity refinement. H:R2.A6 is merged, not reassigned to R3. |
| PrimaryPurpose | Reduce nonessential interface demand through independently scoped optional/secondary content reduction. |
| NeedCoverage | **declared**: {"N1": "Reduce nonessential content in the scoped comprehension task.", "N3": "Reduce nonessential secondary navigation/control demand in the scoped orientation task."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R2 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | D.content.reduction[ElementID].state |
| Legal parameters/values | **state**: ["shown", "collapsed"]; **scope_kind**: ["optional-content", "secondary-navigation", "nonessential-controls"]; **scope**: Nonempty set of versioned ElementIDs with disjoint canonical ownership; independent state per ElementID |
| Default/current state | **default**: shown for every declared ElementID; **adaptive_target**: collapsed for the eligible declared scope; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Every selected element is explicitly nonessential in this task; required route/feedback/status/recovery descendants are excluded; a labelled expansion control remains available. |
| Permanent exclusions | CG-6 and Element is essential, contains the only required route, hides required feedback/status/recovery, or lacks a safe expansion control. |
| Temporary blockers | CG-7 and Essentiality, descendant graph, focus relationship or viewport result unknown; input active in selected scope. |
| ExpectedEffect | Collapse only the eligible selected elements; other scopes retain their own current states. |
| Postconditions | INV-01–INV-05 and No required information, validation/error feedback, transaction status, required action or recovery route is lost; no selections/data are deleted. |
| Compatibility constraints | CG-8 and R1 help and R3 recovery/status controls are protected; R2.A3 cannot group a protected control into a collapsed ancestor. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "narrow-scope", "change": "Selected scope → nonempty eligible subset; state stays collapsed", "guard": "All excluded elements remain shown/current-safe; every retained element is declared nonessential; scoped coverage is recomputed for the reduced subset.", "preserved_effect": "Nonessential-demand reduction remains delivered in the remaining scope; no new function."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R2.A2<br>H:V2-08<br>CAT1/V2-08/merge<br>CAT1/V2-08/protected |

### R2.A3 Semantic Grouping

| Contract field | Specification |
| --- | --- |
| ActionID | R2.A3 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R2 |
| HistoricalProvenance | H-PROP-20260908 F.4 R2.A3; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Group related content while respecting task structure. |
| NeedCoverage | **declared**: {"N3": "Provide logical content grouping for orientation.", "N4": "Keep related references together if the conditional edge is true."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R2 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | D.grouping.mode; D.grouping.realisation |
| Legal parameters/values | **mode**: ["standard", "semantic"]; **realisation**: ["native", "within-stage"]; **scope**: Registered groups of FieldID/content IDs |
| Default/current state | **default**: {"mode": "standard", "realisation": "native"}; **adaptive_target**: {"mode": "semantic", "realisation": "native"}; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and A versioned grouping maps every member once without changing dependency order. |
| Permanent exclusions | CG-6 and Required field omitted/duplicated, dependency cycle, or inaccessible member. |
| Temporary blockers | CG-7 and Stage/group/focus mapping unknown or active input move pending. |
| ExpectedEffect | Group related content without editing its values. |
| Postconditions | INV-01–INV-05 and All members, dependencies and value identity preserved. |
| Compatibility constraints | CG-8 and With R4.A1 staged flow, groups crossing stages require the declared within-stage partition. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "within-stage", "change": "native grouping → within-stage partition", "guard": "Partition is total/disjoint over original members, preserves dependency order and contextual reference access, and all stage scopes are valid.", "preserved_effect": "Related grouping is retained within legal stage boundaries."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R2.A3<br>H:V2-05<br>CAT1/V2-05/stage |

### R2.A4 Emphasise Primary Control

| Contract field | Specification |
| --- | --- |
| ActionID | R2.A4 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R2 |
| HistoricalProvenance | H-PROP-20260908 F.4 R2.A4; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Visually prioritise the current valid primary action. |
| NeedCoverage | **declared**: {"N3": "Identify the current primary control.", "N5": "Distinguish the relevant next choice/action."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R2 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | D.primary.control.emphasis |
| Legal parameters/values | **mode**: ["standard", "emphasized"]; **scope**: One manifest-declared valid primary ControlID per decision scope |
| Default/current state | **default**: standard; **adaptive_target**: emphasized; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Exactly one primary ControlID is declared valid for the scope. |
| Permanent exclusions | CG-6 and Control is unauthorised/invalid or emphasis hides alternatives/required controls. |
| Temporary blockers | CG-7 and No uniquely known valid primary control. |
| ExpectedEffect | Emphasise the existing control without executing it. |
| Postconditions | INV-01–INV-05 and Action semantics and authorisation unchanged. |
| Compatibility constraints | CG-8 and Must agree with R4 step/dependency model; cannot force submit or replace choice. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R2.A4<br>H:V2-08 |

### R2.A5 Checklist Presentation

| Contract field | Specification |
| --- | --- |
| ActionID | R2.A5 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R2 |
| HistoricalProvenance | H-PROP-20260908 F.4 R2.A5; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Present requirements as a readable checklist. |
| NeedCoverage | **declared**: {"N4": "Keep requirement references/status available if its conditional edge is true.", "N5": "Support requirement comparison and preparation choices."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R2 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | D.requirements.view |
| Legal parameters/values | **mode**: ["full", "checklist"]; **scope**: Versioned requirement list |
| Default/current state | **default**: full; **adaptive_target**: checklist; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Complete requirement IDs, descriptions and known/unknown fulfilment states are available for display. |
| Permanent exclusions | CG-6 and Checklist omits requirements, fabricates fulfilment or removes full descriptions. |
| Temporary blockers | CG-7 and Requirement list version or mapping unknown. |
| ExpectedEffect | Show checklist entries with accurate state and access to full requirement detail. |
| Postconditions | INV-01–INV-05 and No requirement becomes fulfilled through a UI change; unknown status remains unknown. |
| Compatibility constraints | CG-8 and May coexist with autosave/resume; does not itself persist, restore or reconcile progress. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R2.A5<br>H:V3-01 |

### R3.A1 Draft Autosave

| Contract field | Specification |
| --- | --- |
| ActionID | R3.A1 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R3 |
| HistoricalProvenance | H-PROP-20260908 F.4 R3.A1; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Persist eligible current draft data for continuity. |
| NeedCoverage | **declared**: {"N4": "Preserve task references if N4→R3 is true.", "N6": "Support recovery of entered data.", "N7": "Maintain draft continuity."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R3 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | P.draft.autosave |
| Legal parameters/values | **mode**: ["off", "on"]; **scope**: Authorised draft ID and version |
| Default/current state | **default**: on if supported and consent policy permits; otherwise effective off; **adaptive_target**: on when eligible; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Storage is supported, consent/policy permits, and snapshot has the correct draft/session identity. |
| Permanent exclusions | CG-6 and Storage prohibited/unsupported for this contract; snapshot belongs to another draft/user. |
| Temporary blockers | CG-7 and Storage state unknown, write in progress or newer draft revision unresolved. |
| ExpectedEffect | Persist a versioned draft snapshot after an accepted input event. |
| Postconditions | INV-01–INV-05 and No source data deleted or replaced by an older snapshot; persist result is recorded honestly. |
| Compatibility constraints | CG-8 and Compatible with guidance; resume and save serialised by draft version; baseline minimum persistence applies equally to both UI conditions. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Also request/transaction identity, authorisation and payload references, ambiguity epoch, permit/status revision, query/retry token, result quality and baseline/adaptive origin; do not copy sensitive payloads. |
| Verification references | H:V2-01<br>CAT1/V2-01/R3.A1<br>H:V3-01<br>H:V3-05 |

### R3.A2 Guarded Retry

| Contract field | Specification |
| --- | --- |
| ActionID | R3.A2 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R3 |
| HistoricalProvenance | H-PROP-20260908 F.4 R3.A2; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Continue a previously authorised logical request only under a current safe retry permit. |
| NeedCoverage | **declared**: {"N6": "Prevent unsafe duplication while allowing a permitted retry.", "N7": "Continue an eligible interrupted request."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R3 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | P.network.retry |
| Legal parameters/values | **mode**: ["manual", "guarded-auto"]; **scope**: Same TransactionID, idempotency key, operation, authorisation and payload reference; one attempt per permit token |
| Default/current state | **default**: manual; **adaptive_target**: guarded-auto; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and TX-1 retry permit is current; authoritative result is safely_retryable; same payload/identity and prior user authorisation remain valid. |
| Permanent exclusions | CG-6 and Transaction completed or terminally rejected; non-idempotent/unauthorised operation; changed payload/identity or service forbids retries. |
| Temporary blockers | CG-7 and Status pending/unknown, query or original mutation in flight, permit stale, or safe-point/token check unresolved. |
| ExpectedEffect | Issue at most one permitted retry for the same logical transaction; never generate a new submission identity. |
| Postconditions | INV-01–INV-05 and No duplicate transaction and no assumption that a timed-out retry failed; consume the attempt permit. |
| Compatibility constraints | CG-8 and Mutually exclusive with R3.A7 command on the same transaction snapshot; feedback follows result evidence, not predicted success. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point. Read/query/retry/resume commands additionally obey TX-1; a policy change is not a command authorisation. |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Also request/transaction identity, authorisation and payload references, ambiguity epoch, permit/status revision, query/retry token, result quality and baseline/adaptive origin; do not copy sensitive payloads. |
| Verification references | H:V2-01<br>CAT1/V2-01/R3.A2<br>H:V2-07<br>H:V3-02<br>CAT1/V2-07/status<br>CAT1/V3-02/branches |

### R3.A3 Low-Bandwidth Asset Profile

| Contract field | Specification |
| --- | --- |
| ActionID | R3.A3 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R3 |
| HistoricalProvenance | H-PROP-20260908 F.4 R3.A3; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Use declared lighter resources while preserving essential support. |
| NeedCoverage | **declared**: {"N7": "Keep essential service content available under the justified continuity need."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R3 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | P.asset.profile; P.asset.realisation |
| Legal parameters/values | **profile**: ["standard", "low-bandwidth"]; **realisation**: ["native", "registered-text"]; **scope**: Versioned asset bundle with required semantic content IDs |
| Default/current state | **default**: {"profile": "standard", "realisation": "native"}; **adaptive_target**: {"profile": "low-bandwidth", "realisation": "native"}; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and A registered low-bandwidth bundle preserves every required content/function ID. |
| Permanent exclusions | CG-6 and No equivalent permitted resources; suppressing an essential asset loses required meaning. |
| Temporary blockers | CG-7 and Resource equivalence/version or feature availability unknown; replacement would interrupt active input. |
| ExpectedEffect | Use declared low-bandwidth assets without silently dropping essential information. |
| Postconditions | INV-01–INV-05 and Required content coverage and functionality remain accessible. |
| Compatibility constraints | CG-8 and R1.A4 media alternatives require reciprocal registered equivalence; bandwidth never overrides INV-04. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "registered-text", "change": "low-bandwidth native → registered-text", "guard": "Versioned per-asset map covers every required semantic ID; no indispensable visual-only content is lost; the text bundle is permitted for the current task.", "preserved_effect": "Essential continuity-supporting content remains available."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Also request/transaction identity, authorisation and payload references, ambiguity epoch, permit/status revision, query/retry token, result quality and baseline/adaptive origin; do not copy sensitive payloads. |
| Verification references | H:V2-01<br>CAT1/V2-01/R3.A3<br>H:V2-06<br>CAT1/V2-06/text |

### R3.A4 Recovery Panel

| Contract field | Specification |
| --- | --- |
| ActionID | R3.A4 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R3 |
| HistoricalProvenance | H-PROP-20260908 F.4 R3.A4; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Expose interruption state and permitted recovery controls. |
| NeedCoverage | **declared**: {"N6": "Expose safe recovery options.", "N7": "Explain how the interrupted task may continue."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R3 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | P.recovery.panel; P.recovery.realisation |
| Legal parameters/values | **visibility**: ["hidden", "visible"]; **realisation**: ["native", "shared-review"]; **scope**: Current interruption/task ID |
| Default/current state | **default**: {"visibility": "hidden unless baseline safety requires visible", "realisation": "native"}; **adaptive_target**: {"visibility": "visible", "realisation": "native"}; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and An actual pending/error/interruption state exists and each enabled recovery control has a current guard. |
| Permanent exclusions | CG-6 and Fabricated status or a recovery control that enables an unsafe operation. |
| Temporary blockers | CG-7 and Control permissions/status evidence unknown; show known uncertainty through baseline feedback while guarded controls remain disabled. |
| ExpectedEffect | Show accurate interruption state and safe next controls. |
| Postconditions | INV-01–INV-05 and Does not itself retry, restore a draft or determine authoritative transaction state. |
| Compatibility constraints | CG-8 and Can share presentation with R4.A4; status and review data must remain distinguishable. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "shared-review", "change": "native → shared-review", "guard": "R4.A4 independently nominated; review data and recovery state have separate labelled regions and preserved controls/IDs.", "preserved_effect": "Both recovery and review purposes retained."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Also request/transaction identity, authorisation and payload references, ambiguity epoch, permit/status revision, query/retry token, result quality and baseline/adaptive origin; do not copy sensitive payloads. |
| Verification references | H:V2-01<br>CAT1/V2-01/R3.A4<br>H:V2-09<br>CAT1/V2-09/shared |

### R3.A5 Explicit Submission Feedback

| Contract field | Specification |
| --- | --- |
| ActionID | R3.A5 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R3 |
| HistoricalProvenance | H-PROP-20260908 F.4 R3.A5; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Communicate the evidenced current transaction status. |
| NeedCoverage | **declared**: {"N6": "Explain success, rejection or uncertainty without misleading repeat actions.", "N7": "Make continuation/pending state understandable."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R3 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | P.submission.feedback |
| Legal parameters/values | **mode**: ["standard", "explicit"]; **scope**: TransactionID; status is read from S, not assigned by this action |
| Default/current state | **default**: standard; **adaptive_target**: explicit; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Current transaction identity is known; status quality and evidence reference are available, including explicit unknown. |
| Permanent exclusions | CG-6 and Status belongs to another transaction or proposed message fabricates success. |
| Temporary blockers | CG-7 and Correlated status record is stale/missing; use baseline unknown feedback until fresh reevaluation. |
| ExpectedEffect | Render completed, pending, safely_retryable, terminal_rejected or unknown using TX-1 message semantics. |
| Postconditions | INV-01–INV-05 and No transaction mutation, query or retry; unknown remains unknown. |
| Compatibility constraints | CG-8 and Consumes R3.A7 or other authoritative result only through a new observation/decision; R3.A4 controls remain distinct. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Also request/transaction identity, authorisation and payload references, ambiguity epoch, permit/status revision, query/retry token, result quality and baseline/adaptive origin; do not copy sensitive payloads. |
| Verification references | H:V2-01<br>CAT1/V2-01/R3.A5<br>H:V2-07<br>H:V3-06<br>CAT1/V3-06/chain |

### R3.A6 Guided Draft Resumption

| Contract field | Specification |
| --- | --- |
| ActionID | R3.A6 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R3 |
| HistoricalProvenance | H-PROP-20260908 F.4 R3.A6; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Guide restoration of a compatible persisted user task. |
| NeedCoverage | **declared**: {"N4": "Re-establish saved task references when conditional N4→R3 holds.", "N7": "Resume the same draft and valid progress."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R3 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | P.draft.resume |
| Legal parameters/values | **mode**: ["manual", "guided"]; **scope**: Authorised compatible draft ID/version; explicit resume authorisation token |
| Default/current state | **default**: manual; **adaptive_target**: guided; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Snapshot belongs to the same user/service, is version-compatible, and user explicitly agrees to resume; no entered current value conflicts. |
| Permanent exclusions | CG-6 and Different owner/service, invalid snapshot, destructive overwrite, or incompatible schema with no declared lossless mapping. |
| Temporary blockers | CG-7 and Draft verification/merge safety unknown, user confirmation pending, current edit unfinished or write in flight. |
| ExpectedEffect | Guide a separate authorised resume event that restores the correct snapshot. |
| Postconditions | INV-01–INV-05 and Preserve all current entered values; restoration records source/destination versions and logical progress. A conflicting nonempty current value prevents restoration. |
| Compatibility constraints | CG-8 and Serialised with autosave; does not reconcile server transaction truth or imply a resubmission. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point. Read/query/retry/resume commands additionally obey TX-1; a policy change is not a command authorisation. |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Also request/transaction identity, authorisation and payload references, ambiguity epoch, permit/status revision, query/retry token, result quality and baseline/adaptive origin; do not copy sensitive payloads. |
| Verification references | H:V2-01<br>CAT1/V2-01/R3.A6<br>H:V3-05<br>CAT1/V3-05/resume |

### R3.A7 Transaction Status Reconciliation

| Contract field | Specification |
| --- | --- |
| ActionID | R3.A7 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R3 |
| HistoricalProvenance | No historical ActionID. Current separation of transaction-status checking already required across H:F.5.1, H:V2-07, H:V3-02 and H:V3-05, explicitly adopted by the user on 12 September 2026. It is not H:R2.A6 moved to R3 and not an unchanged historical action. |
| PrimaryPurpose | Determine the reliable status of an in-flight or ambiguously completed logical service transaction before a potentially unsafe continuation. |
| NeedCoverage | **declared**: {"N6": "Provide a guarded read-only status-determination attempt and preserve uncertainty to prevent unsafe repeat effects.", "N7": "Provide reliable status evidence, or an explicit unresolved result, for continuity decisions."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R3 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | P.transaction.reconciliation; read-only interaction returns status evidence to S |
| Legal parameters/values | **mode**: ["manual", "guarded-query"]; **scope**: Existing TransactionID/idempotency key; ambiguity epoch and trigger token; one query per token; no arbitrary operation/payload |
| Default/current state | **default**: manual; mandatory baseline pre-retry status checks remain active in both UI conditions; **adaptive_target**: guarded-query; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and N6 and/or N7 is justified in the same scope and nominates R3; transaction is in-flight/ambiguous; current authorised read-only status facility and transaction identity exist; trigger token not consumed. |
| Permanent exclusions | CG-6 and No scoped need/R3 nomination; no existing transaction; unauthorised status access; endpoint has service-mutating semantics; transaction terminally known with no newer ambiguity. |
| Temporary blockers | CG-7 and Network/status facility temporarily unavailable, query already in flight, evidence/identity ambiguous or trigger token already consumed; await a new declared trigger. |
| ExpectedEffect | Dispatch one read-only reconciliation query; accept only TX-1 matched reliable status, otherwise retain explicit unknown/pending. Publish its result as a new observation. |
| Postconditions | INV-01–INV-05 and No submission, resend, invented success, altered authorisation or idempotency key. A status result is evidence for a later full-chain decision, not an inline retry. |
| Compatibility constraints | CG-8 and R3.A2 cannot execute in the same snapshot; R3.A5 displays the next evidenced status; R3.A4 exposes controls and R3.A6 handles local draft resumption separately. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point. Read/query/retry/resume commands additionally obey TX-1; a policy change is not a command authorisation. |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Also request/transaction identity, authorisation and payload references, ambiguity epoch, permit/status revision, query/retry token, result quality and baseline/adaptive origin; do not copy sensitive payloads. |
| Verification references | H:V2-01<br>CAT1/V2-01/R3.A7<br>H:V2-07<br>H:V3-02<br>H:V3-05<br>CAT1/V2-07/status<br>CAT1/V3-02/branches<br>CAT1/V3-06/chain |

### R4.A1 Staged Flow

| Contract field | Specification |
| --- | --- |
| ActionID | R4.A1 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R4 |
| HistoricalProvenance | H-PROP-20260908 F.4 R4.A1; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Present the task in legal logical stages. |
| NeedCoverage | **declared**: {"N2": "Expose the service sequence.", "N3": "Maintain logical stage orientation.", "N4": "Retain references across stages if its conditional edge holds."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R4 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | F.flow.mode |
| Legal parameters/values | **mode**: ["single-page", "staged"]; **scope**: Versioned stage/dependency graph |
| Default/current state | **default**: single-page; **adaptive_target**: staged; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Total field/control-to-stage mapping preserves dependency order and current logical position. |
| Permanent exclusions | CG-6 and Missing/cyclic dependency or stage mapping loses values/required controls. |
| Temporary blockers | CG-7 and Unfinished input or ambiguous upload/submission affecting restructuring; snapshot mapping unknown. |
| ExpectedEffect | Render stages without changing the logical service facts. |
| Postconditions | INV-01–INV-05 and Preserve values, valid progress and current logical StepID. |
| Compatibility constraints | CG-8 and Grouping must fit stage boundaries; cue/progress share the same logical graph. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R4.A1<br>H:V2-05<br>H:V3-03<br>CAT1/V2-05/stage |

### R4.A2 Progress Indicator

| Contract field | Specification |
| --- | --- |
| ActionID | R4.A2 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R4 |
| HistoricalProvenance | H-PROP-20260908 F.4 R4.A2; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Display evidenced logical task progress. |
| NeedCoverage | **declared**: {"N2": "Show position in the task sequence.", "N3": "Show current stage orientation.", "N7": "Retain continuity cues when conditional N7→R4 holds."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R4 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | F.progress.indicator; F.progress.realisation |
| Legal parameters/values | **mode**: ["off", "on"]; **realisation**: ["native", "shared-cue"]; **scope**: Logical stage/progress object |
| Default/current state | **default**: {"mode": "off", "realisation": "native"}; **adaptive_target**: {"mode": "on", "realisation": "native"}; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Versioned progress object and logical stage are known. |
| Permanent exclusions | CG-6 and Invented completion or progress label contradicts prerequisites. |
| Temporary blockers | CG-7 and Progress snapshot unknown/mismatched. |
| ExpectedEffect | Display actual logical progress. |
| Postconditions | INV-01–INV-05 and No advancement, completion or validation is performed. |
| Compatibility constraints | CG-8 and Can share a control with R1.A3 when identities and cue data match. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "shared-cue", "change": "native → shared-cue; mode remains on", "guard": "R1.A3 independently nominated, mode full, same logical progress identity and preserved full cue.", "preserved_effect": "Joint progress/cue representation retains both sources."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R4.A2<br>H:V2-03<br>CAT1/V2-03/shared |

### R4.A3 Step Validation

| Contract field | Specification |
| --- | --- |
| ActionID | R4.A3 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R4 |
| HistoricalProvenance | H-PROP-20260908 F.4 R4.A3; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Expose validation at the appropriate task stage. |
| NeedCoverage | **declared**: {"N6": "Expose existing validation results and correction opportunities before continuation."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R4 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | F.validation.timing |
| Legal parameters/values | **mode**: ["submit", "step"]; **scope**: Manifest validation rules and stage |
| Default/current state | **default**: submit; **adaptive_target**: step; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and Existing validation predicates can be evaluated without destructive side effects; authoritative server checks remain. |
| Permanent exclusions | CG-6 and Changes validation rules, eligibility or server acceptance; destructive normalisation of user input. |
| Temporary blockers | CG-7 and Input composition incomplete or validation service/evidence unavailable. |
| ExpectedEffect | Evaluate existing rules at the step boundary and display results. |
| Postconditions | INV-01–INV-05 and Validation truth is unchanged by presentation; newly observed results are evidence events, not fabricated progress. |
| Compatibility constraints | CG-8 and R1.A6 may explain errors; step cues must not imply invalid steps completed. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R4.A3<br>H:V3-01<br>H:V3-08 |

### R4.A4 Review Summary

| Contract field | Specification |
| --- | --- |
| ActionID | R4.A4 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R4 |
| HistoricalProvenance | H-PROP-20260908 F.4 R4.A4; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Expose a faithful review of entered data and requirements. |
| NeedCoverage | **declared**: {"N4": "Provide persistent review references if its conditional edge holds.", "N5": "Support a declared review-stage decision if conditional N5→R4 holds.", "N6": "Support checking before authorised submission."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R4 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | F.review.summary; F.review.realisation |
| Legal parameters/values | **mode**: ["off", "on"]; **realisation**: ["native", "shared-recovery"]; **scope**: Versioned data/requirement snapshot |
| Default/current state | **default**: {"mode": "off", "realisation": "native"}; **adaptive_target**: {"mode": "on", "realisation": "native"}; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and A complete faithful summary mapping exists for the current version and authorised display scope. |
| Permanent exclusions | CG-6 and Summary omits required review data, exposes unauthorised content or changes values. |
| Temporary blockers | CG-7 and Snapshot/field mapping unknown or update in flight. |
| ExpectedEffect | Display a review summary with a legal correction route. |
| Postconditions | INV-01–INV-05 and Review never submits or changes data; status labels separate from review values. |
| Compatibility constraints | CG-8 and Can share presentation with R3.A4 while preserving separate semantics. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | {"VariantID": "shared-recovery", "change": "native → shared-recovery; mode remains on", "guard": "R3.A4 independently nominated/visible; separately labelled review/status regions preserve all controls and data.", "preserved_effect": "Faithful review remains available alongside recovery."} |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R4.A4<br>H:V2-09<br>CAT1/V2-09/shared |

### R4.A5 Back/Review Navigation

| Contract field | Specification |
| --- | --- |
| ActionID | R4.A5 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R4 |
| HistoricalProvenance | H-PROP-20260908 F.4 R4.A5; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Offer legal navigation to prior stages and review. |
| NeedCoverage | **declared**: {"N2": "Offer legal process navigation.", "N3": "Retain orientation through stage navigation.", "N4": "Provide access to prior references if its conditional edge holds."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R4 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | F.stage.navigation |
| Legal parameters/values | **mode**: ["basic", "back-review"]; **scope**: Allowed edges of the service stage graph |
| Default/current state | **default**: basic; **adaptive_target**: back-review; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and The service graph permits the offered return/review edges. |
| Permanent exclusions | CG-6 and Navigation bypasses authorisation/validation or has no safe state mapping. |
| Temporary blockers | CG-7 and Current edit/transaction blocks the offered transition or edge status unknown. |
| ExpectedEffect | Expose valid back/review controls without navigating automatically. |
| Postconditions | INV-01–INV-05 and Data and validation facts survive any later separately authorised navigation. |
| Compatibility constraints | CG-8 and R2 secondary reduction cannot remove its only required route. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R4.A5<br>H:V2-08<br>H:V3-03 |

### R4.A6 Dependency Cues

| Contract field | Specification |
| --- | --- |
| ActionID | R4.A6 |
| CatalogueVersion | UAIS-CAT-1.0 |
| RuleSource | R4 |
| HistoricalProvenance | H-PROP-20260908 F.4 R4.A6; purpose retained, operational contract made explicit in UAIS-CAT-1.0. |
| PrimaryPurpose | Explain task and field prerequisites. |
| NeedCoverage | **declared**: {"N2": "Explain required sequence/dependencies.", "N5": "Explain prerequisite choice implications when its conditional edge holds.", "N6": "Expose prerequisite/correction information."}; **gate**: CG-1: only currently justified scoped needs with a TRUE existing Nk→R4 edge; union with provenance, never activate a need from this action. Coverage denotes delivered support capability, not empirical effectiveness or resolution of the need. |
| Target/UI or service-interaction property | F.dependency.cue |
| Legal parameters/values | **mode**: ["hidden", "visible"]; **scope**: Manifest prerequisite/dependency IDs |
| Default/current state | **default**: hidden; **adaptive_target**: visible; **current**: Read the typed current property map at the decision snapshot; never substitute the default for a known current value. |
| Preconditions | CG-1–CG-5 and The relevant dependency/prerequisite exists in versioned metadata. |
| Permanent exclusions | CG-6 and Invented dependency or cue contradicts authoritative requirements. |
| Temporary blockers | CG-7 and Metadata version or scoped relevance unknown. |
| ExpectedEffect | Show relevant dependency cues. |
| Postconditions | INV-01–INV-05 and No requirement, choice or eligibility is changed. |
| Compatibility constraints | CG-8 and Must agree with staged flow, current validation truth and step guidance. |
| Transition constraints | CG-9: apply only within a coherent scope/version snapshot; protect active input; retain support during unresolved recovery; withdraw no longer justified optional support only at a safe point.  |
| PermittedTransformations | None. No TRANSFORM is legal for this action. |
| Relevant invariants | INV-01<br>INV-02<br>INV-03<br>INV-04<br>INV-05 |
| Logging requirements | TRACE-CAT1: action/variant/parameters, historical predecessor(s), scope and need/edge evidence, guard/invariant results, target and current change atoms, operation/result, versions and predecessor/successor IDs. Record affected content/control/field IDs and reachability/state witnesses. |
| Verification references | H:V2-01<br>CAT1/V2-01/R4.A6<br>H:V2-10<br>H:V3-08 |
