# Section 4 Figures Tables and Supplementary Material

Companion to UAIS_Section4_Proposed_Framework.md. Governing specifications: UAIS-S3-FINAL-1.0, UAIS-CAT-1.0 and VER-CAT1. This file specifies figure production and article placement; it does not claim that a rendered figure or implemented system has been produced. Figure/table numbers are provisional within this package and should be reconciled with earlier manuscript numbering at assembly.

## Figure 1 Overall framework architecture

### Publication caption

**Figure 1. Context-aware adaptive UI decision loop.** Context evidence is related to scoped cognitive accessibility needs, which nominate adaptation rules and candidate actions. The Action Composition & Transition Resolver produces a proposed configuration U*(t) and action dispositions. Execution remains conditional on runtime state S(t) and current admissibility checks. Validated interaction and service events update the observation/context layer for a subsequent decision occasion. U(t) contains four adaptive-output dimensions; S(t) supplies state and control information rather than an additional output dimension. Logging accompanies observation, decision and execution, including suppressed and deferred changes.

### Composition and exact labels

Use a wide, two-lane vector composition. The primary lane reads left to right. A runtime-state rail below supplies the resolver and execution block. A separate feedback route returns along the bottom; the three logging blocks occupy a compact rail above or below the corresponding primary stages without crossing the feedback line.

| Node | Exact label | Contents or annotation |
| --- | --- | --- |
| F1-01 | Context Evidence C(t) | C1 User; C2 Device; C3 Connectivity; C4 Service; scope/quality/ContextRole |
| F1-02 | Cognitive Accessibility Needs N(t) | N1–N7; scoped need provenance |
| F1-03 | Candidate Adaptation Rules R(t) | R1–R4; more than one family may be nominated |
| F1-04 | Candidate Actions A(t) | UAIS-CAT-1.0; 24 actions; 6–5–7–6 |
| F1-05 | Action Composition & Transition Resolver | KEEP; COMBINE; TRANSFORM; SUPPRESS; DEFER |
| F1-06 | Proposed Configuration U*(t) | [G, D, P, F]; accompanying action dispositions |
| F1-07 | Execution Admissibility and Application | Current invariant, guard and version checks |
| F1-08 | Applied U and Evidenced Service Events | Applied configuration or safe hold; validated service responses update S separately |
| F1-09 | Updated Observations C(t+1) | Relevant user, context and validated service events |
| F1-S | Runtime Interaction/Control State S(t) | Logical step; entered/unfinished input; pending operations; assistance/recovery; transaction state |
| F1-U | Current Configuration U(t) | G Guidance; D Density / Presentation Demand; P Protection / Continuity & Resilience; F Flow Structure |
| F1-L1 | ObservationLogger | Evidence and context classification |
| F1-L2 | DecisionTraceLogger | Mapping, candidates, comparison and disposition |
| F1-L3 | ActionExecutionLogger | Admission, execution and resulting-state references |

### Directed connections

1. Primary solid decision arrows: F1-01→02→03→04→05→06→07→08.
2. Solid observation/feedback arrows: F1-08→09→01. Label the return “fresh evidence; next decision occasion”, not “automatic adaptation”.
3. Dashed state-input arrows: F1-S→05 and F1-S→07. F1-U→05 supplies the comparison baseline; F1-U→07 supplies the current configuration. Changes to S from validated events are recorded on a distinct F1-08→F1-S arrow.
4. Dotted trace arrows: F1-01→L1; F1-02/03/04/05→L2; F1-07/08→L3. Show thin linkage L1→L2→L3 labelled observation/decision/execution IDs.
5. Add a small deferred-record output from F1-05 with a feedback attachment to F1-09, labelled “reconsider on relevant event”. It must not connect directly back to application.

Do not draw Context→Rule, Context→Action, Need→Execution, or reconciliation-result→retry shortcuts. Do not draw S as a fifth box inside the U vector. Derived categories in C1.3/C3.3 and the associated episode records in S are coherent views of the same event history, not independent competing state machines.

### Production guidance

Use vector boxes and orthogonal connectors, readable at full manuscript width, with a compact label hierarchy. A practical full-width design target is approximately 170–180 mm, with final-size text around 8–9 pt and strokes at least 0.6 pt; these are figure-design choices rather than publisher-specific requirements. Distinguish decision, state and trace connections by line style and labels so the diagram remains understandable in grayscale. Keep the long P expansion in the vector legend, not in every block. Avoid screenshots, UI mockups, colour-only meanings and checkmarks that imply successful verification.

## Figure 2 Resolver process

### Publication caption

**Figure 2. Action composition and lexicographic resolution.** Scoped candidate plans are assessed against a coherent snapshot using Validity & Integrity, Feasibility, Need Coverage, State Continuity, Transition Stability and Minimal Change, in that order. Lower criteria cannot restore an alternative eliminated by a higher criterion. Incomparable survivors may proceed to lower comparisons, but only genuine six-criterion equality permits canonical tie selection. Unknown or unresolved disputed changes are withheld. A selected plan is checked again against current execution state before application.

### Layout and nodes

Use a vertical main column for the ordered stages, with left-hand non-execution dispositions and a right-hand snapshot rail. Display the six criteria as numbered rectangles, not as equal-weight inputs to a scoring or averaging node.

| Node | Exact label | Decision semantics |
| --- | --- | --- |
| F2-01 | Scoped Candidate Plans | Candidate generation from N→R; relevant legal realisations and joint effects |
| F2-02 | 1 Validity & Integrity | INV-01–INV-05; hard immediate-transition gate |
| F2-03 | 2 Feasibility | READY / WAIT / BLOCKED / UNKNOWN |
| F2-04 | 3 Need Coverage | Strict set inclusion of justified scoped coverage |
| F2-05 | 4 State Continuity | Residual disruption after mandatory protection |
| F2-06 | 5 Transition Stability | Disturbance of unresolved support commitments |
| F2-07 | 6 Minimal Change | Distinct typed U-property changes |
| F2-08 | One Survivor? | A unique survivor can be selected after the declared filtering |
| F2-09 | Genuine Equality at All Six Criteria? | Only for multiple final survivors |
| F2-10 | Canonical Reproducibility Key | Action/variant/scope/typed-parameter order |
| F2-11 | Selected Action Plan | KEEP / COMBINE / permitted TRANSFORM as applicable |
| F2-12 | Current Execution-Admissibility Check | Verify current state, invariants, guards and version tokens |
| F2-13 | Apply Eligible Effects | Configuration application and separately guarded service interactions |
| F2-H | Safe Hold / DEFER | Record disputed need, blocker and successor-trigger requirements |
| F2-X | Exclude Target / SUPPRESS | Record exclusion or displacement reason |
| F2-S | Coherent Snapshot | C(t), N(t), S(t), U(t), specification versions |

### Flow rules

- F2-01→02→03 follows the hard gates. From F2-03 only READY proceeds to F2-04.
- At F2-02, false means no immediate execution, not permission to compensate with lower criteria. A known illegal/excluded target routes to F2-X. A state-dependent unsafe immediate proposal can have a separate safe holding plan at F2-H; this does not turn a failed immediate invariant into a pass. Unestablished required evidence also prohibits immediate execution and routes to the appropriate fresh-evidence deferral.
- WAIT routes to F2-H; BLOCKED routes to F2-X; UNKNOWN withholds the target and records the missing evidence at F2-H. Label dispositions as target-specific; a proven-independent admitted component need not be blocked by an unrelated component.
- F2-04→05→06→07 uses survivor-set filtering. Add a side note: “remove strictly dominated alternatives simultaneously; retain equal/incomparable survivors; unknown cannot support lower comparison”. Do not depict pairwise sorting or a weighted sum.
- F2-07→08. If one survivor remains, route to F2-11. Otherwise F2-08→09. Genuine six-criterion equality routes F2-09→10→11. Substantive incomparability routes F2-09→F2-H; it cannot reach F2-10.
- F2-11→12→13 only when the fresh check passes. A stale token routes F2-12→F2-H with “new linked decision; fresh evaluation”.
- F2-S supplies F2-02 through F2-07. The check at F2-12 uses the currently valid tokens, not an assumption that the earlier snapshot remained current.

The lower comparison stages may use scope-specific set relations; do not label equal cardinality as equivalent need coverage. Avoid a “best possible UI” terminal label. The output is a policy-selected admissible plan, not a globally optimal adaptation claim.

## Figure 3 State-aware DEFER and reevaluation lifecycle

### Publication caption

**Figure 3. Deferred-decision lifecycle under current runtime evidence.** A deferred target is retained as a record with a blocker, relevant triggers and predecessor identity. A relevant event initiates fresh context, need, rule and action evaluation and produces a linked successor decision. Execution requires a new admissibility check; the original deferred target is never replayed directly. The successor can apply a retained, combined or transformed plan, suppress the obsolete or excluded target, or defer again. Lifecycle labels do not add resolver operations or guarantee eventual execution.

### Layout and labels

Use a compact lifecycle diagram with a central fresh-evaluation block and three outcome branches. Place runtime evidence above the cycle and predecessor/successor logging below it.

1. **Scoped candidate** → **DEFER decision d₀**.
2. **DEFER decision d₀** → **Deferred record: target, blocker, scope, versions, triggers**.
3. An external **Relevant event** enters the deferred-record boundary: edit completion, fresh relevant evidence, episode recovery, service-state change or authorised version change. Mere elapsed time is not a trigger unless the contract declares one.
4. Event → **Fresh C → derived states → N → R → A** → **New resolver decision d₁**.
5. Link d₀ to d₁ beneath the main flow, labelled **predecessor → successor; no replay**.
6. From d₁ draw three branches:
   - **KEEP / COMBINE / TRANSFORM** → **Current admissibility check** → **Eligible execution**.
   - **SUPPRESS** → **Reason recorded; no execution of target**.
   - **DEFER again** → **New linked deferred record** → await another relevant event.
7. Failed/stale current check returns to **New linked deferred record**, not to the old target or unchecked execution.
8. Execution returns validated observations to the framework loop, and updates configuration/state only under the applicable event contract.

Use “superseded”, “executed” and “awaiting event” only as lifecycle annotations. They are not a sixth resolver operation, a new C1.3 state or a fifth C3.3 category. Show neither an unconditional arrow from safe point to application nor an automatic query polling cycle. A query's own result/failure cannot manufacture a new reconciliation trigger for the same unresolved transaction.

## Recommended manuscript tables

The full manuscript-ready tables are embedded in the Section 4 draft. Keep these tables with the indicated discussion:

| Table | Placement | Main-body content | Material excluded from the table |
| --- | --- | --- | --- |
| 1 Context model | 4.2 | Twelve parameters, representation and operational use | Full instrument items, classification provenance and transition tables |
| 2 Cognitive needs | 4.3 | Seven operational needs and support focus | Per-observation evidence records and every predicate witness |
| 3 Need-to-rule matrix | 4.4 | Compact seven-by-four relationship matrix and symbol definitions | The 84-cell C→N matrix and all detailed C→N/N→R conditions |
| 4 Action catalogue summary | 4.5 | 24 ActionIDs, names, concise purposes, declared coverage and main U dimension | Twenty-field action contracts and enumerated variant guards |
| 5 Resolver summary | 4.6 | Panel A: five operations; Panel B: six ordered criteria | Full comparator definitions, canonicalisation rules and execution trace schema |

Table 3 is the compact mapping table recommended in addition to the context, needs, actions and resolver summaries. Do not compress the 24-action table by dropping R3.A7 or using the obsolete 6–6–6–6 count. If layout requires a continuation, repeat its column header and retain one table number. The operation and precedence panels can share a table number while preserving their distinct roles.

## Supplementary-material plan

The following labels describe proposed supplementary units, not claims that separate published supplements already exist. Existing locked deliverables supply their content.

| Proposed unit | Details to move out of the main article | Existing source |
| --- | --- | --- |
| S1 Context and state specification | Complete evidence fields; experience recency/missing rules; ISS administration/scoring; C2 feature/reflow protocol; exact C3 classifications; C1.3 transitions; C3.3 recovery including unknown gaps; C4 vector schema | UAIS-S3-FINAL-1.0 and recovered context specification |
| S2 Mapping specification | Full 84-cell C→N and 28-cell N→R matrices; 51/18 non-dash conditions; six C1.3 condition deltas; provenance and version identity | Historical Mapping and Verification Import plus MAP-CD1 |
| S3 Action contracts | All 24 × 20 fields; merged historical provenance; scoped NeedCoverage; parameter dictionary; transformation registry; compatibility and transition guards | UAIS_Final_Action_Catalogue.md and UAIS_Final_Action_Contracts.json |
| S4 Resolver detail | Comparator domains, K/D/T sets, unknown/incomparable semantics, simultaneous survivor filtering, typed change atoms and canonical equality key | RES-CD1 plus UAIS-CAT-1.0 common clauses |
| S5 Service-state and execution contract | Complete INV-01–INV-05 predicates, safe input boundaries, validated response events, status authority/identity, retry permits, query tokens and baseline-safety distinction | INV-CD1 and TX-1 |
| S6 Verification specification | Original 35 parent cases and unchanged historical expectations; versioned current child families and expected dispositions, explicitly distinguished from later execution results | VER-CAT1 and original parent import |
| S7 Trace schema | Observation/decision/execution fields, comparator evidence, variant provenance, predecessor/successor links, commit checks and version manifest | TRACE-CD1 and TRACE-CAT1 |

Keep the functional rationale and key boundaries in the main article even when their full operational details move to supplements. In particular, the no-Context→Rule restriction, U/S distinction, invariant gate, scoped coverage, genuine-equality tie rule and mediated R3.A7 operation must remain explicit in Section 4. Research-development procedure belongs in Section 3; concrete instantiation and actual verification evidence belong in later sections, not in this framework description.
