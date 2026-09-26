# 4 Proposed Context-Aware Adaptive UI Framework

## 4.1 Framework Overview

The proposed framework defines a context-aware adaptation mechanism in which interface decisions are mediated by explicit cognitive accessibility needs. Context evidence identifies a situation relevant to a task; a documented mapping relates that evidence to an interaction-support requirement; and the requirement nominates one or more adaptation rules. The rules contribute candidate actions whose effects are composed, compared and checked before execution. Village administrative services provide the application context, while the framework represents the decision relationships and state constraints independently of a particular service form.

The architecture forms a closed decision loop:

**Context evidence C(t) → Cognitive accessibility needs N(t) → Candidate rules R(t) → Candidate actions A(t) → Action Composition & Transition Resolver → Proposed configuration U*(t) → Execution under runtime state S(t) → Interaction/context update C(t+1).**

Here, t denotes a decision occasion rather than a fixed sampling interval. C(t) retains classified evidence together with its source, scope and quality. N(t) and R(t) may contain multiple concurrent needs and rules. A(t) contains scoped action candidates from the versioned catalogue, including candidates whose guards require further assessment. The resolver produces a proposed configuration and action dispositions; execution is conditional on the current runtime state. Its output can therefore include retained actions, a compatible composition, a permitted transformation, suppression or deferral rather than an immediate interface change.

The adaptive configuration has four dimensions:

**U(t) = [G, D, P, F],**

where G denotes Guidance, D Density / Presentation Demand, P Protection / Continuity & Resilience, and F Flow Structure. Each dimension contains typed, scoped properties, such as guidance visibility, optional-content reduction, continuity policies or staged presentation. These are configuration dimensions within one adaptive interface, not separate pages indexed by the set of active rules. U*(t) denotes a proposed target; U(t) denotes the configuration currently in effect. A proposal does not become the applied configuration solely because a rule is applicable.

Runtime state S(t) is distinct from U(t). It contains the logical service position, entered data, active editing state, pending operations, assistance and recovery episodes, and relevant transaction state. The resolver and execution layer consult S(t) to determine whether a proposed change can be realised without violating the service and interaction constraints. S(t) is not an additional adaptive-output dimension.

Figure 1 depicts the main decision path, the state inputs to resolution and execution, and the feedback route through new observations. Observation, decision and execution logging accompany the loop. They record the evidence used, the alternatives considered and the resulting disposition, including decisions that do not change U(t). New user events, changed context and validated service responses can initiate another decision occasion; they do not bypass the need and rule layers.

## 4.2 Context Representation

The Context Model contains four groups and twelve parameters, summarised in Table 1. Their representations remain heterogeneous because an experience category, an instrument score, a feature constraint and a service dependency describe different aspects of the interaction. The framework does not collapse them into a single difficulty score.

**Table 1. Context model and operational representations.**

| Group | Parameter | Representation | Role in the decision loop |
| --- | --- | --- | --- |
| C1 User | C1.1 Digital Experience | Recent Experience, No Recent Experience, and explicit uncertainty handling | Supplies factual service-experience evidence; does not diagnose ability |
| C1 User | C1.2 Digital Interaction Skills | Continuous ISS-20 vector: operational, information navigation, social and creative dimensions | Provides supporting context without low/medium/high adaptation cut-offs |
| C1 User | C1.3 Runtime Assistance Indication | Stable, Emerging, AssistanceNeeded, Recovering; separate evidence-quality metadata | Represents the current assistance-control episode |
| C2 Device | C2.1 Device/Form Factor | Mobile, Tablet or Desktop descriptor; uncertainty retained separately | Describes access conditions without independently activating a need |
| C2 Device | C2.2 Available Display Space / reflow constraint | ReflowOK, Constrained or Unknown; current viewport and reflow observations | Informs presentation feasibility and task-specific evidence of fragmentation |
| C2 Device | C2.3 Required Feature Availability | Supported, Limited or Unknown, with feature-level evidence | Constrains permitted effects and supplies evidence of relevant service limitations |
| C3 Connectivity | C3.1 Connection Quality | Preferred, Acceptable, Poor or Unknown | Represents application-request response evidence |
| C3 Connectivity | C3.2 Connection Stability | Stable, Unstable or Unknown for a logical request chain | Retains retry, failure and timeout evidence |
| C3 Connectivity | C3.3 Derived Disruption Risk | Normal, AtRisk, Disrupted or Recovering; uncertainty recorded separately | Summarises aligned connectivity evidence and recovery order |
| C4 Service | C4.1 Process Length / process vector | Number of steps, branching, dependencies and rollback points | Describes task sequence and cross-step relationships |
| C4 Service | C4.2 Requirement Load / requirement vector | Requirement count, types, dependencies and formats | Describes preparation and requirement relationships |
| C4 Service | C4.3 Form Interaction Complexity / form vector | Field count, conditional fields, validation, upload and review | Describes the interaction structure of the service form |

C1.3 is an interaction-support control state derived from assistance-related evidence. Stable denotes a known current condition without an elevated assistance indication. Emerging records exploration of context-specific support before a request is confirmed. AssistanceNeeded represents an explicit request under the specified event guard. Recovering retains the assistance episode after closure while stable task participation is re-established. An explicit request can enter AssistanceNeeded directly; the four labels do not imply that every transition must pass through Emerging. An untyped help request does not establish all need categories, and unavailable evidence is not interpreted as observed Stable. The framework does not use task duration or error counts to infer cognitive impairment or silently escalate C1.3.

C3.1 uses the locked response-time intervals: Preferred below 2.000 s, Acceptable from 2.000 s to below 4.000 s, and Poor at or above 4.000 s or on timeout. Unavailable evidence is Unknown, and classification precedes any display rounding. C3.2 evaluates one logical request together with its retries: observed retry, failure or timeout produces Unstable; a sufficiently observed chain without those events is Stable. C3.3 combines temporally aligned quality and stability evidence with the preceding risk phase. Its Recovering state concerns connectivity and remains distinct from assistance recovery in C1.3.

The display parameter likewise represents a functional constraint rather than a device-based adaptation trigger. The locked reflow check includes the 320 CSS-pixel reference condition and observations at the actual viewport; width alone does not activate a rule. C4 parameters retain factual vectors rather than invented complexity classes. For these vectors, an empty set can indicate that a feature is absent, whereas an unknown value indicates missing evidence.

ContextRole identifies how an observation participates in a decision. **NeedEvidence** supports a documented task-related need condition. **Descriptor** records characteristics without independently establishing a support requirement. **Constraint** limits which effects can be realised. **DerivedControlState** summarises an episode or sequence used in current interpretation. A parameter can have different uses in different decisions, provided that the recorded role and mapping condition make the use explicit. For example, a reflow observation constrains presentation and may also support an orientation need when navigation fragmentation is evidenced; a device-class descriptor does not acquire that meaning simply because it describes a small device.

## 4.3 Cognitive Accessibility Need Layer

The Need Layer makes the support rationale explicit between context and adaptation. A contextual condition does not specify which interface property should change. The framework first relates the condition to a task-related requirement, then uses that requirement to nominate a response. This separation permits different contextual evidence to support the same need and allows one situation to justify several needs without assigning the user to a fixed interface category.

**Table 2. Operational cognitive accessibility needs.**

| Need | Support requirement | Operational focus |
| --- | --- | --- |
| N1 | Understanding / comprehension support | Explanations of relevant terms, instructions or information |
| N2 | Process-following support | Guidance concerning task sequence and the next permitted action |
| N3 | Orientation support | Identification of logical position, navigation and content relationships |
| N4 | Memory support | Availability or preservation of references, choices and task information |
| N5 | Decision support | Presentation of relevant alternatives, prerequisites and consequences |
| N6 | Error/failure prevention and recovery support | Correction information and protection against unsafe or inconsistent effects |
| N7 | Process-continuity support | Maintenance or resumption of task state across interruption |

N1–N7 are the framework's operational representation informed by its knowledge base; they are not presented as a W3C taxonomy or diagnostic categories. Their activation denotes a justified interaction-support requirement, not a measured cognitive deficit or proof that an adaptation will be effective.

A need instance is scoped to the service version, task and relevant support object. Its provenance links the originating observations, ContextRole, derived state where applicable, task demand, mapping condition, and source rationale. Multiple observations supporting the same scoped need are combined while their provenance is retained. Uncertainty on one edge does not cancel a need justified by another true edge.

Scoped interpretation also prevents broad labels from concealing different obligations. Determining a transaction's status and communicating that status are distinct support objects within the same task. Both can be related to N6 or N7, but a message that honestly reports uncertainty does not itself perform status determination. Action coverage is therefore assessed against the currently justified scoped requirement and the effect declared in the action contract, rather than by counting need labels or treating all actions associated with N7 as interchangeable.

## 4.4 Evidence-to-Need and Need-to-Rule Mapping

The framework uses the imported mapping matrices as its relational structure. C→N contains 84 cells, including 51 non-dash edges; N→R contains 28 cells, including 18 non-dash edges. The current specification preserves this topology. The six versioned C1.3 refinements modify activation conditions without adding or removing edges.

The symbols distinguish three relationships. A tick (✓) denotes a primary candidate relationship when its documented condition holds. A circle (○) denotes a conditional relationship requiring the stated additional relevant evidence. A dash (–) denotes no relation. Neither symbol licenses unconditional activation from a raw value. Conditions are evaluated as true, false or unknown; only a true condition activates the edge. Table 3 presents the compact N→R matrix. The full C→N matrix and all edge conditions are supplied in the supplementary specification.

**Table 3. Need-to-rule relationships.**

| Need | R1 | R2 | R3 | R4 |
| --- | --- | --- | --- | --- |
| N1 | ✓ | ○ | – | – |
| N2 | ✓ | – | – | ✓ |
| N3 | ○ | ✓ | – | ✓ |
| N4 | – | ○ | ○ | ○ |
| N5 | ✓ | ✓ | – | ○ |
| N6 | ✓ | – | ✓ | ✓ |
| N7 | – | – | ✓ | ○ |

For example, a current, typed request for step guidance supports the conditional C1.3→N2 edge in the relevant task scope. N2 then nominates R1 and R4 through their documented primary relationships. Opening a help preview without a confirmed request does not establish this C1.3-derived need.

As a second example, Poor quality or Unstable request-chain evidence can support N6 and N7 when the corresponding prevention/recovery and continuity conditions apply to the operation. These needs nominate R3 through N→R; N6 also has documented primary links to R1 and R4. The action layer subsequently determines which of those families contains a relevant response for the current task. The connectivity value does not directly choose retry, reconciliation or any other action.

Rule nomination thus follows a true need-to-rule edge from an active need. The resolver cannot nominate a rule that the Need Layer has not justified, and a candidate action cannot create the need that would authorise itself. **No Context→Rule activation is permitted.**

## 4.5 Adaptation Rules and Candidate Actions

The four rule families describe response purposes. R1, Guided Interaction Support, provides task-relevant explanations and cues. R2, Interface Simplification, reduces nonessential presentation demand. R3, Interaction Resilience & Continuity, concerns preservation, interruption handling and safe continuation. R4, Step-by-Step Task Structure, concerns task sequence, progress, validation and review. A family can be nominated by several needs, and nomination does not imply that every action in that family is applicable on the current screen.

UAIS-CAT-1.0 contains 24 actions distributed as six R1, five R2, seven R3 and six R4 actions. Table 4 summarises their purposes, declared need coverage and main U dimension. Coverage entries remain subject to the existing need-to-rule conditions, scope matching and realisation guards; they are not empirical effectiveness rankings. Full contracts, legal parameters and permitted transformations are supplied in the supplementary catalogue.

**Table 4. Action catalogue summary (UAIS-CAT-1.0).**

| Action ID | Action | Primary purpose | Declared Need coverage | Main U dimension |
| --- | --- | --- | --- | --- |
| R1.A1 | Contextual Guidance | Expose task-relevant instructions | N1, N2 | G |
| R1.A2 | Term Explanation | Explain a scoped service term | N1 | G |
| R1.A3 | Step Cue | Show current/next-step guidance | N2, N3 | G |
| R1.A4 | Examples | Offer valid contextual examples | N1, N5, N6 | G |
| R1.A5 | Contextual Help Access | Expose relevant help access | N1, N2, N3, N5 | G |
| R1.A6 | Contextual Error Explanation | Explain an evidenced error and correction | N6 | G |
| R2.A1 | Reduce Interface Density | Reduce nonessential presentation density | N1, N3 | D |
| R2.A2 | Contextual Secondary/Optional Content Reduction | Reduce independently scoped nonessential content | N1, N3 | D |
| R2.A3 | Semantic Grouping | Group related content within task constraints | N3, N4 | D |
| R2.A4 | Emphasise Primary Control | Prioritise the current valid primary control | N3, N5 | D |
| R2.A5 | Checklist Presentation | Present requirements as a faithful checklist | N4, N5 | D |
| R3.A1 | Draft Autosave | Persist eligible draft data | N4, N6, N7 | P |
| R3.A2 | Guarded Retry | Retry the same authorised request safely | N6, N7 | P |
| R3.A3 | Low-Bandwidth Asset Profile | Use permitted lighter resources | N7 | P |
| R3.A4 | Recovery Panel | Expose interruption state and recovery controls | N6, N7 | P |
| R3.A5 | Explicit Submission Feedback | Communicate the evidenced transaction status | N6, N7 | P |
| R3.A6 | Guided Draft Resumption | Guide compatible local draft resumption | N4, N7 | P |
| R3.A7 | Transaction Status Reconciliation | Determine transaction status by read-only check | N6, N7 | P |
| R4.A1 | Staged Flow | Present legal logical stages | N2, N3, N4 | F |
| R4.A2 | Progress Indicator | Show evidenced logical progress | N2, N3, N7 | F |
| R4.A3 | Step Validation | Expose validation at the task stage | N6 | F |
| R4.A4 | Review Summary | Present a faithful review summary | N4, N5, N6 | F |
| R4.A5 | Back/Review Navigation | Offer legal back/review navigation | N2, N3, N4 | F |
| R4.A6 | Dependency Cues | Explain task and field prerequisites | N2, N5, N6 | F |

R2.A2 combines the historical optional-element and secondary-navigation reductions within independently declared scopes. It can address optional content, secondary navigation and nonessential controls, but cannot remove the only route to required information, validation/error feedback, transaction status, service actions or recovery. Both predecessor identities remain in the catalogue provenance. This merge changes action granularity; it does not move the former secondary-navigation action into R3.

R3.A7 separately expresses Transaction Status Reconciliation. It determines the evidenced state of an existing in-flight or ambiguous logical transaction through a guarded read-only check. Its scope is the existing transaction identity, and candidacy requires justified N6 and/or N7 evidence that nominates R3. A timeout alone cannot activate it. The action does not resend the transaction, create a new submission, infer success from a lost response, or replace guarded retry and feedback.

The R3 contracts distinguish determining status (R3.A7), retrying under a current safe permit (R3.A2), communicating evidenced status (R3.A5), exposing recovery controls/state (R3.A4), and resuming persisted draft/task state (R3.A6). A reconciliation response becomes a new observation and initiates a new decision; it cannot directly call a retry. Completed status excludes retry, while a reliably established retryable status permits consideration of R3.A2 only under its own current identity, authorisation and idempotency guards. Unknown or pending status leaves unsafe repeat submission blocked. Essential baseline transaction safety remains active independently of adaptive orchestration and is labelled separately in the trace.

## 4.6 Action Composition and Transition Resolver

Concurrent needs and rules can produce actions that are compatible, duplicate an equivalent effect, compete for a property, cannot be realised under current constraints, or are temporarily unsafe to apply. These situations require different dispositions. In particular, rule applicability, candidate-action compatibility and execution admissibility are separate judgements. Two nominated families need not conflict, and two compatible actions need not be immediately executable.

The Action Composition & Transition Resolver assesses scoped alternatives against the same coherent context, need, configuration and runtime-state snapshot. Each alternative specifies its action identities, parameters, permitted realisations and joint effects. Compatible effects can form one plan; shared representations retain all contributing provenance. Table 5 summarises the five operations and the ordered criteria.

**Table 5. Resolver operations and ordered comparison policy.**

*Panel A. Operations.*

| Operation | Meaning | Boundary |
| --- | --- | --- |
| KEEP | Retain a legal, relevant effect that can coexist with the selected plan | Retention remains subject to current safety and relevance |
| COMBINE | Compose compatible effects or deduplicate equivalent effects | Preserve all contributing identities and need provenance |
| TRANSFORM | Select a declared alternative representation, parameterisation or realisation of an existing action | Preserve purpose and invariants; no unlisted action or function |
| SUPPRESS | Exclude an unjustified, prohibited or displaced target from the current plan | Record the reason and affected objective |
| DEFER | Withhold a disputed or not-yet-admissible change for fresh reconsideration | Preserve safe state and link the later decision to its predecessor |

*Panel B. Criteria, applied in the displayed order.*

| Order | Criterion | Comparison basis |
| --- | --- | --- |
| 1 | Validity & Integrity | Hard admissibility under INV-01–INV-05 |
| 2 | Feasibility | READY, WAIT, BLOCKED or UNKNOWN under current effect constraints |
| 3 | Need Coverage | Strict inclusion over justified scoped need coverage sets |
| 4 | State Continuity | Residual disruption of logical interaction anchors after mandatory invariants hold |
| 5 | Transition Stability | Disturbance of still-justified support commitments in unresolved episodes |
| 6 | Minimal Change | Number of distinct typed U-property changes from the current configuration |

Validity & Integrity is a hard gate. An invariant violation rejects the proposed immediate transition; an unestablished required predicate cannot be treated as a pass. Feasibility then distinguishes effects realisable now (READY), effects with a named temporary blocker and release event (WAIT), targets excluded by the current contract or capability (BLOCKED), and insufficient evidence (UNKNOWN). Only READY alternatives enter the executable lower-criterion comparison. A waiting plan preserves current state rather than applying an unsafe target and attempting to compensate afterwards.

Need Coverage compares sets of currently justified scoped requirements supported by the declared effects. An alternative covering a strict superset is preferred, subject to higher criteria. Equal counts do not establish equal coverage, and overlapping non-nested sets are incomparable. State Continuity compares residual disruptions, such as moving a non-editing logical focus or reading anchor, after mandatory data and progress protection has been satisfied. Transition Stability considers replacements or reversals of still-justified support during unresolved assistance or recovery episodes, including changes to still-relevant deferred targets. It is not a synonym for changing fewer properties.

Minimal Change compares the fixed, typed semantic property dictionary of U(t). A property affected by several actions contributes one change atom, and the merged R2.A2 action retains independently scoped element-state atoms. Actual transaction truth in S(t) does not become a new U dimension or an extra presentation-change weight. This criterion introduces no numerical accessibility weights.

Resolution is lexicographic. At each criterion, strictly dominated alternatives are removed simultaneously from the current survivor set; a lower criterion cannot restore an alternative eliminated earlier. Equal and incomparable survivors continue under the declared policy. Unknown is not equality and prevents an unsupported lower-criterion comparison for the affected alternative or component. Incomparable alternatives may be distinguished by a lower criterion, but incomparability is not relabelled as genuine equality.

If multiple final survivors are genuinely equal under all six criteria, the resolver uses the canonical ordering of versioned action identities, variants, scopes and typed parameters. This key provides reproducibility, not an accessibility-priority principle. If final survivors remain substantively incomparable, the resolver retains the safe current configuration and defers the disputed change while recording undelivered requirements. If the external state has made that configuration unsafe, data-preserving blocking and status handling take precedence over retaining an invalid interface. The policy does not claim globally optimal adaptation.

Figure 2 presents this resolution process. TRANSFORM remains closed by the catalogue: an empty transformation list prohibits it, and a legal default value is not automatically a purpose-preserving variant. A read-only status query cannot be transformed into retry or submission. Resolution is followed by an execution-admissibility check because relevant runtime evidence may have changed while the decision was being formed.

## 4.7 Runtime State, Safe Transition, and Reevaluation

S(t) supplies the state against which a proposed change is assessed. It includes the logical service step and satisfied prerequisites; entered values and draft/upload references; active control, editing buffer, selection and unfinished input; pending operations and transaction identity/status; and assistance, recovery and deferred-decision episodes. Its logical identifiers remain distinct from visual page positions or component instances.

Five invariants define mandatory protection. **INV-01**, Preservation of entered data, requires preservation of typed values or a declared lossless representation, including values in temporarily hidden conditional fields. **INV-02**, Preservation of valid task/progress state, protects logical position, satisfied prerequisites and valid service facts from arbitrary configuration changes. **INV-03**, Protection of active unfinished input, prevents disruptive restructuring of an active editing scope unless the required edit state is preserved. **INV-04**, Preservation of required functionality and information, maintains the required service routes and feedback under current constraints. **INV-05**, No adaptation-induced invalid or unauthorised irreversible state, prohibits configuration changes from bypassing authorisation, validation or transaction-identity protections. The resolver enforces these predicates under Validity & Integrity before comparing residual continuity preferences.

Selective reevaluation follows evidence dependencies. A changed assistance event revisits the relevant C1.3 conditions and their downstream needs, rules and actions; a connectivity event revisits the aligned connectivity evidence and affected support obligations. Coupled alternatives are assessed jointly where their effects interact. Selectivity reduces the scope of reconsideration without creating a shortcut from a changed parameter to a rule or action.

C1.3 persistence is event-based. A confirmed request remains active until explicitly closed, and closure enters Recovering rather than immediately establishing Stable. A later accepted user interaction at a safe point, with no outstanding request or preview, completes assistance recovery. Repeated preview observations do not silently escalate into a confirmed request, and a background autosave is not evidence of resumed user participation. Unavailable assistance evidence retains uncertainty separately from the last historical control value.

C3.3 uses the specified sequence of aligned observations: the first good pair after a risk episode enters Recovering, and the next good aligned pair establishes Normal. New adverse evidence selects AtRisk or Disrupted according to the locked derivation. An unknown or misaligned gap interrupts the consecutive recovery sequence and cannot complete Normal; after a known risk episode, a fresh good pair restarts Recovering. This hysteresis is event-based and introduces no additional time threshold.

A safe transition requires a coherent snapshot and preservation of the relevant state. A change that would disrupt an unfinished edit is withheld; a provably independent change outside that scope may remain eligible. Immediately before commit, the execution layer checks the relevant context, input, service, episode and specification-version tokens. A mismatch prohibits applying the stale proposal and causes fresh reconsideration.

DEFER therefore means withholding a change and reconsidering it when a relevant blocker or evidence condition changes. Its lifecycle is: **candidate → DEFER → relevant event → fresh Context/Need/Rule/Action evaluation → new resolver result → guarded execution, suppression or renewed deferral**. A transformed alternative follows the same execution gate. The new decision retains its predecessor link; it does not blindly replay the old target. Figure 3 shows this lifecycle. No unconditional eventual execution is implied when evidence remains unknown, the need clears or a substantive incomparability persists.

Configuration commits and subsequent service events remain separate. A validated reconciliation response can update the evidenced transaction state in S(t) and initiate another decision; the UI configuration cannot manufacture that truth. If target U equals current U, no redundant configuration mutation occurs. A new query or other eligible service-interaction event still requires its own current guards and token. The completion or failure of a query cannot itself authorise another query for the same unresolved transaction, preventing the deferred lifecycle from becoming an unbounded polling loop.

## 4.8 Traceability and Decision Provenance

The framework specifies three complementary logging roles. **ObservationLogger** records observations, their sources, scope, quality, temporal or request-chain relationships, and context classifications. **DecisionTraceLogger** records C→N conditions and evidence, active scoped needs, N→R conditions, nominated rules, candidate actions, guard assessments, comparator outcomes and resolver dispositions. **ActionExecutionLogger** records execution admission, relevant version checks, resulting configuration and service-event references, and any deferral, suppression, restoration or failure disposition.

The intended provenance chain is **Observation → Context classification → C→N edge → Need → N→R edge → Rule → Candidate Action → Resolver decision → Execution decision → Resulting UI/service state**. New service evidence links back into the observation stage rather than being treated as an assumed outcome of the earlier decision. Deferred records retain predecessor/successor identities; transformed records retain the permitted variant and original action provenance. Suppression records identify the relevant exclusion or displaced objective. Comparison records distinguish genuine equality, incomparability and unknown, and include the invariant judgements and specification/catalogue versions.

Logging is the instrumentation defined to support this chain. Traceability is the property that subsequent verification examines: whether the required links and decision evidence are present and consistent. The presence of logger roles does not itself demonstrate that property. Service payloads and personal data need not be duplicated where scoped identifiers, status, versioned references and event records provide the required evidence.

## 4.9 Runtime Operation Example

The following **illustrative operational walkthrough** describes a specification-level decision occasion, not an evaluation result. A user is completing a multistep village administrative form and explicitly requests help with the next step. A reflow observation shows that access to a navigation cue is fragmented, while the relevant application-request chain has Poor quality and Unstable behaviour. The user also has an unfinished active field.

The typed assistance request supports C1.3→N2 in the current scope. The evidenced navigation fragmentation supports C2.2→N3. The relevant poor/unstable request evidence supports N6 and N7 under their documented prevention/recovery and continuity conditions. N2 nominates R1 and R4; N3 nominates R2 and R4; N6 nominates R1, R3 and R4; and N7 nominates R3, with its R4 edge remaining conditional. The resulting candidate families therefore include R1–R4. The display condition is not used to bypass N3 and directly activate simplification.

Subject to their individual guards, candidate effects include contextual guidance or a step cue, reduced-density or semantically grouped presentation, draft/low-bandwidth continuity support, and staged flow or a progress indicator. R4.A1 would restructure the active editing scope and is deferred because INV-03 does not permit the proposed change during the unfinished edit. A grouping change that moves the same active field is assessed under the same protection. Guidance in an existing independent region or continuity support for already accepted draft data may remain eligible if their joint noninterference and capability checks hold. A simplification target that removes required navigation is excluded rather than justified by the small display.

No ambiguous submitted transaction is stipulated in this walkthrough. Consequently, poor connectivity alone does not make R3.A7 applicable: its transaction-scope guard and mediated need justification must also hold. Similarly, maintaining an autosave policy does not imply that the unfinished editing buffer has already been committed.

When the user completes the field edit, the resulting safe-point event initiates fresh evaluation of context, needs, rules, candidates and the resolver. It does not automatically execute the deferred staged-flow proposal or close the assistance request. The new decision can apply a still-relevant safe target, select a permitted alternative, suppress a target that is no longer justified, or defer again if another blocker remains. The walkthrough illustrates how need mediation and state protection constrain the decision loop without asserting a particular executed outcome or improvement in user experience.
