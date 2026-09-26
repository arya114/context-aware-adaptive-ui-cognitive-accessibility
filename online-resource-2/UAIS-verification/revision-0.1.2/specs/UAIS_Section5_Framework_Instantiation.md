# 5 Framework Instantiation

## 5.1 Application Context

The framework is instantiated as a specification for a single simulated village administrative service: an application for a residence statement. The fixture has ServiceID `VILLAGE-RESIDENCE-DEMO`, ServiceVersion `1.0.0`, and fixture identifier `UAIS-VRI-1.0`. These identifiers bind the workflow, content, observations and transaction branches described below. They identify a research fixture rather than an official service standard. The selected fields and document requirements are fixture choices and do not represent the legal requirements of a particular village.

The workflow comprises service selection, requirements, applicant information, supporting information and documents, review, authorised submission, and transaction-status handling. This sequence supplies dependencies, cross-step references, uploads and an ambiguous-submission branch within one application. Village administration provides a concrete setting in which the general decision mechanism can be instantiated; it is not the framework's scientific contribution.

The backend is specified as a simulated service with a controlled transaction ledger. No connection to a production government backend, official certificate issuance, or legal equivalence to a government transaction is asserted. The bindings in this section define the prototype configuration and its subsequent verification inputs. They are not presented as observations from an implemented or deployed system.

## 5.2 Service Manifest and Logical State

The versioned manifest supplies semantic identities for steps, fields, requirements, documents, content and operations. These identities persist when presentation changes. A renderer may associate them with components, but component or DOM identifiers do not determine service identity. Table 6 summarises the workflow; the complete fixture declaration accompanies the supplementary specification.

**Table 6. Versioned service manifest and logical workflow.**

| StepID | Service stage | Manifest objects and prerequisites | Permitted continuation |
| --- | --- | --- | --- |
| ST01 | Service selection | Select VILLAGE-RESIDENCE-DEMO, version 1.0.0 | ST02 |
| ST02 | Requirements and instructions | REQ01 applicant data; REQ02 address evidence; REQ03 declaration; required instruction INFO01 | ST03; back to ST01 |
| ST03 | Applicant information | FLD01 applicant name; FLD02 fixture resident reference; FLD03 address; VAL01–VAL03 | ST04 when valid; back to ST02 |
| ST04 | Supporting information/documents | FLD04 purpose; conditional FLD05 purpose detail; DOC01 address evidence with UploadID; VAL04–VAL06 | ST05 when applicable values and upload are accepted; back to ST03 |
| ST05 | Review | Versioned REVIEW01 of accepted values and DOC01 reference; FLD06 declaration; VAL07 | ST06 after an explicit submission request; edit via ST03 or ST04 |
| ST06 | Authorised submission | OP01 and immutable payload reference; TransactionID and idempotency key; current authorisation | ST07 after dispatch; no second independent submission for an unresolved transaction |
| ST07 | Transaction/status handling | Evidenced status, receipt or rejection; separate status-determination and status-communication scopes | Read-only review; guarded same-transaction continuation or declared correction route |

REQ01 is satisfied by valid FLD01–FLD03. REQ02 requires an accepted DOC01 reference. REQ03 requires the review declaration to refer to the current payload revision. FLD04 selects either the fixture's administrative purpose or an “other” option; the latter makes FLD05 required. A hidden FLD05 retains its entered value, while its applicability is evaluated separately. Changing a payload-bearing value invalidates the previous review acceptance. The review therefore cannot authorise submission of values different from those displayed.

Validation predicates distinguish nonempty text, fixture-reference syntax, conditional completeness, document acceptance and current review agreement. These are service constraints, not adaptive decisions. Required instructions, validation messages, review access, safe submission controls, and status/recovery information remain reachable under every eligible presentation. A disabled operation retains its explanation and permitted next action.

For this instantiation, S(t) contains the current StepID, accepted field-value map and revisions, active FieldID with unfinished buffer, caret/selection and composition state, draft ownership/version, and upload state. It also contains the authorised payload reference, pending operation, transaction identity, latest accepted status evidence, assistance/recovery episodes, and deferred-decision links. An illustrative editing snapshot has current step ST04, an accepted FLD04 value of “other”, unfinished FLD05 text, draft revision d3 and DOC01 upload u1 pending. Transaction state is then not-started, not an invented pending submission. A later snapshot after OP01 dispatch has a TransactionID and a pending operation; response loss makes the client's knowledge unknown without implying that the simulator rolled back its ledger.

Before submission, legal back/edit navigation preserves values and rechecks affected dependencies. After an ambiguous dispatch, local recovery cannot replace the frozen transaction payload or create a new submission identity. A terminal rejection can expose a correction route; a revised payload requires new review and explicit authorisation after the preceding transaction is terminal. A completed ledger effect is not undone by presentation rollback or local draft restoration. These facts remain in S(t), separate from U(t).

## 5.3 Instantiated Context Acquisition

Observers bind the existing twelve context parameters to fixture events and evidence. Each record carries the service version, scope, observation identity and evidence quality. Table 7 specifies the acquisition boundary. Sources are defined for the prototype; their availability is checked rather than assumed.

**Table 7. Context acquisition in UAIS-VRI-1.0.**

| Parameter | Concrete source | Representation | Update event | Missing/unknown handling |
| --- | --- | --- | --- | --- |
| C1.1 | Explicit service-experience response and reference date | Recent Experience within the locked 12-month interval; No Recent Experience for never-used response | Response confirmed or corrected | Missing, ambiguous or older-only history remains unresolved under the locked rule |
| C1.2 | Versioned ISS-20 response record | Continuous operational, information-navigation, social and creative dimension means | Complete response or correction | An incomplete dimension is unavailable; no imputation or categorical cut-off |
| C1.3 | Scoped help preview, typed assistance request, closure and accepted task interaction | Stable / Emerging / AssistanceNeeded / Recovering, with separate quality | support.preview_opened; support.preview_closed; assistance.requested; assistance.closed; task.resumed | Unavailable event history is not observed Stable |
| C2.1 | Device/form-factor descriptor supplied by the session | Mobile / Tablet / Desktop | Session descriptor change | Unknown descriptor; no independent need activation |
| C2.2 | Fixture reflow inspection at 320 CSS pixels and functional inspection at the current viewport | ReflowOK / Constrained / Unknown with affected semantic anchors | Viewport/zoom or relevant rendering change and refreshed inspection | Width alone is insufficient; absent functional evidence is Unknown |
| C2.3 | Feature probes against the fixture capability manifest | Supported / Limited / Unknown with per-feature witnesses | Initial probe, permission/capability change or operation failure | An unobserved capability is not presumed available |
| C3.1 | Timed requests to the simulated submission, status or upload operation, identified by attempt | Preferred / Acceptable / Poor / Unknown | Matching response or adapter timeout | Unavailable measurement is Unknown; classify before rounding |
| C3.2 | Event history of one logical request including its attempts | Stable / Unstable / Unknown | Attempt/response, failure, timeout, authorised retry or chain completion | Insufficient chain history is Unknown |
| C3.3 | Aligned C3.1/C3.2 evidence and prior connectivity phase | Normal / AtRisk / Disrupted / Recovering | New aligned evidence pair or evidence gap | Gap retains uncertainty and breaks the consecutive recovery sequence |
| C4.1 | Manifest step and navigation/dependency graph | Seven steps; branch edges, dependencies and declared rollback boundaries | Manifest/version or applicable path change | Missing graph facts remain unknown; no process-length category |
| C4.2 | REQ01–REQ03 with types, dependencies and document formats | Three requirements and their factual attributes | Manifest or applicability change | Absent requirement differs from unavailable requirement metadata |
| C4.3 | FLD01–FLD06, predicates, DOC01 and REVIEW01 | Six declared fields, one conditional field, validation, upload and review descriptors | Manifest or field-applicability change | Unknown attributes are retained; no aggregate complexity score |

C1.1 records experience rather than competence. The fixture does not silently classify a response describing only use outside the recency interval as “never used”. C1.2 retains the instrument's locked item allocation and scoring, including 6−x reversal for information-navigation items. The vector supplies supporting context; a dimension score alone does not activate a need.

In the interface, opening a contextual help preview emits support.preview_opened, and closing that preview emits support.preview_closed. Choosing “explain this term” or “guide the next step” confirms assistance.requested with its support kind and TermID or StepID. Explicitly closing an outstanding request emits assistance.closed. An accepted user interaction at a safe point, with no outstanding request or preview, supplies task.resumed for the locked recovery transition. Merely closing a popup, a background draft write, a long task duration or repeated errors is not substituted for that transition. A generic request with unknown kind does not establish all needs.

Required capabilities are tied to the fixture's realisation: field input and composition-event support, file selection and transfer for DOC01, a writable versioned draft store for persistence, and an authenticated simulated request/status adapter. Their unavailability limits the corresponding effect; it does not justify fabricated upload, draft or transaction success. A reflow record identifies the affected instruction, field or navigation anchor, so an evidenced orientation problem can be distinguished from a narrow viewport descriptor.

For C3.1, elapsed time is measured from adapter dispatch to receipt of the matching complete application response using the same monotonic clock. It excludes time spent completing the form and unrelated asset traffic. Preferred is below 2.000 s; Acceptable is 2.000–<4.000 s; Poor is at least 4.000 s or an observed timeout. The scenario supplies an explicit timeout event rather than adding an adaptation-delay threshold. A valid validation-rejection response remains a measured response: rejection alone does not establish network instability. Retries, transport failures and timeouts belong to the associated C3.2 chain. Status-query attempts retain their origin, preventing their own failures from authorising further queries.

C3.3 uses aligned pairs: Poor with Stable, or Preferred/Acceptable with Unstable, yields AtRisk; Poor with Unstable yields Disrupted. Following risk, the first good Stable pair enters Recovering and the next consecutive good Stable pair establishes Normal. An unknown gap interrupts that sequence, so a subsequent good pair restarts Recovering. The application binding introduces no alternative state or recovery timer.

## 5.4 Instantiated C→N→R Decision Path

Table 8 follows representative fixture evidence through the locked mappings. Need instances retain ServiceVersion, task/support-object scope and evidence references. Each row shows the relevant path rather than asserting that all other mapping conditions are false. The complete mapping remains authoritative.

**Table 8. Representative fixture evidence and mediated decision paths.**

| Situation and concrete evidence | Context classification and true C→N condition | Scoped need | N→R edge and candidate family |
| --- | --- | --- | --- |
| Explicit request to explain TERM01 at ST02 | C1.3 AssistanceNeeded; C1.3→N1 requires the recorded clarification request | N1 at TERM01 | N1→R1; conditional R2 only if eligible density reduction preserves essential information |
| Explicit next-step guidance request at ST04 | C1.3 AssistanceNeeded; C1.3→N2 requires the typed step-guidance request | N2 at ST04/next-action | N2→R1 and N2→R4 |
| Current reflow fragments access to NAV01 | C2.2 Constrained; C2.2→N3 requires actual navigation/position obstruction | N3 at NAV01 | N3→R2 and N3→R4; R1 only under its additional cue/non-overload condition |
| OP01 response times out, threatening safe continuation | C3.1 Poor and C3.2 Unstable; existing N6/N7 edges require repetition-prevention and continuity relevance | N6 and N7 at transaction support objects | N6→R1/R3/R4; N7→R3, with R4 conditional on preserved resumable progress |
| ST04 depends on accepted applicant data and feeds REVIEW01 | C4.1 vector; C4.1→N2 for sequence, →N3 for step transitions, →N4 for cross-step references | N2/N3/N4 at the relevant step/reference | N2→R1/R4; N3→R2/R4; N4→R4 only when stages retain values and back/review access; other conditional edges remain subject to their conditions |
| DOC01 is rejected for a fixture format mismatch | C4.3 includes upload/validation requiring correction; C4.3→N6 condition holds | N6 at DOC01/VAL06 | N6→R1/R3/R4; action guards subsequently determine applicable correction support |
| FLD04 offers a purpose choice that changes the FLD05 prerequisite | C4.3 choice/conditional-field structure; C4.3→N5 requires a decision about the applicable option | N5 at FLD04/purpose-choice | N5→R1 and N5→R2; R4 only when the decision aligns with a stage and comparison information remains available |

For example, an upload format rejection can justify a contextual error explanation or stage-level correction, but does not establish that a network retry will repair the document. Likewise, a nominated R3 family does not make transaction reconciliation applicable when no submitted transaction exists. The binding preserves the separation between evidence, need justification, rule nomination and action admissibility.

## 5.5 UI Instantiation and Action Binding

The instantiation specifies one interface with reusable instruction, field, navigation, review and status regions. U(t) configures properties of these regions and their eligible service interactions. Four rule families do not imply sixteen separately implemented applications, and the twenty-four actions do not correspond to twenty-four independent pages. Table 9 binds every catalogue action without changing its contract.

**Table 9. Complete catalogue-to-fixture binding.**

| ActionID | Concrete instantiated element/effect | U dimension | Service scope |
| --- | --- | --- | --- |
| R1.A1 | Contextual instruction block bound to INFO01 and stage instructions | G | Current StepID/instruction |
| R1.A2 | Versioned explanation of TERM01, the fixture's address-evidence term | G | TERM01 at ST02/ST04 |
| R1.A3 | Current and next permitted step cue | G | Current StepID and legal successor |
| R1.A4 | Clearly labelled synthetic field/document examples | G | FLD03, FLD05 or DOC01 instruction |
| R1.A5 | Context-specific help access with typed request choices | G | Current field, term or step |
| R1.A6 | Explanation referencing the actual validation/upload error | G | Failed VAL01–VAL07 or DOC01 |
| R2.A1 | Reduced-density rendering retaining required information | D | Current stage presentation |
| R2.A2 | Independently scoped reduction of optional illustration OPT01 and secondary explanation OPT02 | D | Eligible ElementID; required routes excluded |
| R2.A3 | Semantic grouping of applicant and document information | D | FLD01–FLD03 or ST04 group |
| R2.A4 | Emphasis of the currently legal primary control | D | Next, review or authorised-submit control |
| R2.A5 | Faithful checklist of REQ01–REQ03 with evidenced state | D | Requirement preparation/review |
| R3.A1 | Owned, versioned persistence of eligible accepted draft data | P | Service/draft revision |
| R3.A2 | Guarded retry adapter for the same authorised OP01 transaction | P | TransactionID, key and current permit |
| R3.A3 | Lighter registered equivalent of an optional illustration asset | P | Versioned asset pair; required content retained |
| R3.A4 | Recovery/status panel exposing lawful next actions | P | Current interruption/transaction episode |
| R3.A5 | Explicit submission feedback from accepted status evidence | P | Transaction/status-communication |
| R3.A6 | Controlled restoration of an owned compatible draft | P | Draft/version and nonconflicting local fields |
| R3.A7 | Read-only status adapter for an existing ambiguous transaction | P | Transaction/status-determination |
| R4.A1 | Staged presentation of the declared logical workflow | F | Legal StepID graph |
| R4.A2 | Progress indicator based on satisfied logical prerequisites | F | Current path and valid completed stages |
| R4.A3 | Validation presentation at its relevant stage | F | VAL01–VAL07 with field/upload anchors |
| R4.A4 | Snapshot-matched REVIEW01 summary | F | Reviewed payload and document reference |
| R4.A5 | Legal back/review controls preserving values | F | Declared navigation edges |
| R4.A6 | Cues explaining conditional fields and prerequisites | F | FLD04→FLD05 and stage/requirement dependencies |

Each binding retains the catalogue's legal values, defaults, guards, exclusions, transformations and trace requirements. The element scope supplies the concrete argument to a contract; it does not create a new action. R2.A2 retains the merged historical provenance and independent optional-element scopes. Required error, submission and recovery routes are excluded from reduction. A shared review/recovery region is eligible only under the catalogue's declared compatible realisations and retains both action identities. Registering a lighter asset specifies an available resource choice, not evidence of measured bandwidth or usability improvement.

## 5.6 Transaction and Connectivity Instantiation

The simulated OP01 contract binds TransactionID X, idempotency key k, authorised operation OP01, immutable payload reference p, ServiceVersion 1.0.0, authorisation reference and status revision. The simulator ledger is specified to allow at most one committed service effect for k. Initial submission follows the explicit reviewed-payload authorisation; adaptation cannot create that authorisation. Repeated clicks while X is unresolved do not allocate a second transaction identity.

The client's accepted transaction evidence is represented in S(t); the simulator ledger is the authoritative fixture source. U(t) controls presentation and eligible interaction modes, and cannot declare that a transaction completed. A request can reach the simulator while its response is lost. The client's unknown status therefore does not establish either success or failure at the ledger.

In this ambiguous-submit scenario, the original timeout supplies Poor/Unstable context evidence. Where repetition-prevention and continuity conditions hold, the existing mappings activate scoped N6/N7 and nominate R3. R3.A7 can become a candidate for X/status-determination only when its existing-transaction, ownership, query-capability and fresh-trigger guards hold. R3.A5 concerns the separate X/status-communication object. A message saying “status unknown” does not perform determination. A permitted read-only query issues no submission and produces a new observation for a fresh full decision cycle.

The fixture instantiates the locked TX-1 branches. Reliable **completed** evidence suppresses retry and supports completed feedback. Reliable **pending** evidence withholds retry and supports pending feedback while awaiting a new explicit trigger. **safely_retryable** evidence includes a current permit for the same X, k, OP01 and p; it only makes guarded retry potentially applicable in a new mediated decision and after final admission checks. **terminal_rejected** evidence suppresses retry and exposes the evidenced correction route. **unknown** includes missing, mismatched, stale or insufficient responses; it supplies neither a completion claim nor a retry permit.

R3.A7 never automatically triggers R3.A2. Its response handler records evidence rather than dispatching a resend. A permitted later retry consumes the appropriate current permit and preserves the transaction identity and payload. Query completion, query failure or a connectivity change caused by that query cannot mint another query trigger for the same episode. A fresh explicit status-check request is assessed under the existing trigger and guard contract; no polling timer is introduced.

Baseline authorisation, identity checking, duplicate-effect protection and required status communication remain available independently of adaptive nomination, with origin recorded as baseline_safety where appropriate. This distinguishes mandatory service safety from need-mediated orchestration. All branch descriptions are fixture contracts and expected decision boundaries, not reported execution results.

## 5.7 Adaptive Configuration and Safe Application

The renderer receives U(t)=[G,D,P,F] as a typed property map over semantic scopes. A compact illustrative target consists of contextual guidance at ST04 in G, reduced nonessential density for that stage in D, eligible draft-persistence support in P, and staged presentation of the legal path in F. This description denotes the corresponding catalogue properties and permitted values; it does not define new property names or Boolean rules. Other properties retain their recorded current values unless a justified effect changes them. The actual space includes per-element scopes, modes and permitted variants, so sixteen rule subsets do not bound the number of configurations.

The resolver produces U* and scoped action dispositions. Execution checks the current S(t), INV-01–INV-05, service/catalogue versions, draft and input revisions, and relevant episode/transaction tokens. Only admitted effects reach the same interface. A structural ST04 change during unfinished FLD05 input is deferred if it cannot preserve the control, buffer, selection and composition state. An independent instruction region can remain eligible only with noninterference established. There is no delay timer that substitutes for a safe point.

A field-edit completion or acknowledged cancellation can supply a safe-point event when composition has ended, no conflicting operation blocks the effect, and the logical state still matches the decision. The event initiates fresh evaluation rather than replaying the stored proposal. A successor decision records its predecessor and can retain, compose, legally transform, suppress or defer the target under the unchanged resolver. An unsafe current configuration is not preserved merely because it is current: data-preserving blocking and required status handling remain necessary.

The six ordered criteria and their comparison semantics remain those of Section 4. Unknown guards do not become equality, lower criteria cannot revive eliminated alternatives, and final substantive incomparability does not permit arbitrary canonical selection. When U*=U, redundant rendering is omitted. A new eligible service-interaction command still requires independent current admission; an unchanged configuration is neither a command prohibition nor permission to bypass transaction guards.

## 5.8 Logging and Instrumentation in the Instantiation

ObservationLogger is bound to the assistance controls, functional display/feature observations, manifest snapshots and simulated request adapter. DecisionTraceLogger is bound to mapping evaluation, scoped candidate generation and resolver comparison. ActionExecutionLogger is bound to admission, configuration application and service-command/result boundaries. Storage technology is an implementation choice; the required semantic records and links define the instrumentation contract.

The compact chain below is an **illustrative trace structure**, not a log exported from a running prototype. IDs are fixture examples, and the stated disposition illustrates a specified deferral branch.

| Observation/Event ID | Context result | Need/edge | Rule | Action candidate | Resolver operation | Execution status | Resulting U/S reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EX-OBS-01: typed step request at ST04 | C1.3 AssistanceNeeded, kind=step guidance | C1.3→N2; N2 scoped to ST04/next-action; N2→R4 | R4 | R4.A1 at ST04 | DEFER because proposed restructuring affects unfinished FLD05 | Not applied; await relevant safe-point evidence | U=u0 retained; S=s0 with edit e1; deferred decision EX-D01 |

This row projects one candidate path from a larger decision: the N2→R1 nomination and other assessed alternatives remain in the complete record. The full schema also records evidence quality, three-valued edge/guard judgements, comparator witnesses, scoped coverage, candidate variants, invariant results and governing versions. A later EX-D02 links to EX-D01 and cites new observations and snapshot references rather than copying its old decision outcome.

Transaction records distinguish command dispatch, query response, accepted status revision and committed-effect evidence. Query and retry tokens, baseline/adaptive origin, merged-action provenance and rejected stale responses remain reconstructable. Payload references can supply provenance without duplicating personal field contents in every log. Logging is specified to support subsequent trace reconstruction; the existence of this schema does not establish that reconstruction has been verified.

## 5.9 Instantiation Scenarios for Subsequent Verification

UAIS-VRI-1.0 supplies concrete identities and events to the existing verification package rather than defining another evaluation method. O1 concerns classification, O2 need/rule/action decisions, O3 resolver comparisons, O4 state/event sequences and O5 invariant preservation; end-to-end cases connect these boundaries. Historical principal cases and current VER-CAT1 child specifications retain their identifiers and expected-outcome authority.

Classification scenarios bind experience recency, ISS missing/reversal handling, functional reflow, feature availability and exact 2/4-second boundaries to the fixture observations. Sequence scenarios bind C1.3 preview/request/closure/resumption and C3.3 risk, recovery, gaps and relapse to ordered events. Mapping scenarios use the scoped paths in Table 8, including false/unknown conditional edges and device descriptors that do not independently activate needs.

Composition scenarios bind compatible guidance/progress effects, independently scoped R2.A2 reductions, protected navigation and shared review/recovery realisations to the same manifest. Conflict scenarios vary admissibility, scoped coverage, residual disruption, episode stability and typed property differences under the existing comparator policy. Active-input scenarios use FLD05 buffer/selection/composition snapshots, safe-point events and stale-version races to examine deferral and preservation.

Transaction scenarios instantiate X-C, X-P, X-R, X-F and X-U from TX-1, including repeated submission clicks, stale or wrong-identity responses, same-U query admission and query self-trigger exclusion. Draft scenarios distinguish compatible restoration from conflicting edits and unresolved transaction truth. Trace scenarios reconstruct the mediated path and deferred predecessor/successor links, while preserving separate baseline-safety provenance.

These families supply inputs for the existing historical/current cases, including the catalogue-specific action branches. They do not imply that every action executes in every scenario or that a rule subset is a separate application. Execution records, observed outcomes and verification judgements are reserved for Section 6. No implementation pass rate, user-study finding or accessibility-effectiveness claim follows from this instantiation specification.
