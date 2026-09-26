# Exact Section 3 Text Patches

Working title: A Context-Aware Rule-Based Adaptive User Interface Framework for Cognitive Accessibility in Digital Public Services

Use the following exact English passages to replace the corresponding Section 3 discussion of versioning, candidate actions, action contracts, transaction handling and verification. Locations are identified by subject so that existing subsection numbering can be preserved. These are current manuscript passages; the historical proposal and original 35-case record must not be edited to match them. No new empirical result is asserted.

## Patch 1 Versioning and methodological status

Replace the passage treating the current catalogue or six-criterion resolver as unchanged historical specifications with:

The study distinguishes the recovered dissertation specification from the current UAIS specification and records their differences as versioned refinements. The current Action Composition & Transition Resolver extends the earlier priority/conflict mechanism through explicit action contracts, admissibility checks, six ordered comparison criteria, and state-safe reevaluation. The six-criterion formulation is the current refined policy rather than a restatement of the earlier PR1–PR4 specification. The current catalogue, UAIS-CAT-1.0, and its associated decision and verification contracts are fixed for subsequent technical verification. Specification closure does not constitute evidence of implementation correctness or empirical accessibility effectiveness.

## Patch 2 Final action catalogue

Replace the catalogue-pending paragraph and any current statement that every family contains six actions with:

The current catalogue contains 24 actions distributed across Guided Interaction Support (R1, six actions), Interface Simplification (R2, five actions), Interaction Resilience & Continuity (R3, seven actions), and Step-by-Step Task Structure (R4, six actions). This distribution is a versioned refinement of the historical 6–6–6–6 catalogue. Historical optional-element collapsing and secondary-navigation collapsing are merged into R2.A2, Contextual Secondary/Optional Content Reduction, with independently declared scopes. Historical R2.A6 is therefore preserved as predecessor provenance rather than retained as a current action or reassigned to R3. R3.A7, Transaction Status Reconciliation, separately formalises the status-checking requirement previously embedded in retry, safety and recovery behaviour. The merge and separation preserve a total of 24 current ActionIDs.

## Patch 3 Action contracts and scoped coverage

Replace the incomplete-contract or undecided-coverage passage with:

Each action contract specifies its catalogue version, rule source, historical provenance, primary purpose, scoped NeedCoverage, target property, legal parameters, default and target states, preconditions, exclusions, temporary blockers, expected effects, postconditions, compatibility and transition constraints, permitted transformations, invariants, logging requirements and verification references. An action becomes a candidate only when a currently justified need nominates its rule through the existing N→R mapping and the action's scope is relevant. Coverage denotes the support capability guaranteed by the declared realisation, rather than an empirical benefit or a claim that the need has been resolved. Need instances are matched to predefined support objects within a task; communicating an unknown transaction status does not satisfy the distinct requirement to determine that status. The resolver compares coverage by strict set inclusion without numerical accessibility weights.

The minimal-change representation uses the versioned semantic property dictionary of U(t)=[G,D,P,F], where G denotes guidance, D density/presentation, P protection/continuity and F flow structure. R2.A2 contributes independently scoped element-state properties, while transaction truth remains in the service state S. Each changed property is counted once, irrespective of the number of actions sharing its provenance. Neither action merging nor shared rendering changes this dictionary during execution.

## Patch 4 Merged simplification action and required access

Replace the separate current R2.A2/R2.A6 description with:

R2.A2 reduces nonessential interface demand within explicitly declared optional-content, secondary-navigation or nonessential-control scopes. Each scope retains independent state and both historical predecessor identities remain traceable. The action cannot conceal required information, validation or error feedback, transaction status, required service actions or recovery functions, including their only accessible routes. A declared scope-narrowing transformation may retain a nonempty eligible subset, with coverage recomputed for that subset. If no eligible subset remains, the reduction target is suppressed. These constraints operationalise INV-04 and do not imply that state preservation is unique to simplification actions.

## Patch 5 Reconciliation retry and feedback

Insert after the R3 action-family description, replacing any unresolved seventh-action placeholder:

R3.A7 performs a guarded, read-only determination of the status of an existing in-flight or ambiguously completed logical transaction. Its candidacy requires scoped N6 and/or N7 evidence that nominates R3; a timeout or connectivity state cannot activate the action directly. The query retains the existing transaction identity and uses an authorised status facility. It cannot create or resend a submission, infer success from an absent response, or replace guarded retry or user-facing feedback. A result is accepted only when its identity, authority and freshness satisfy the service-state contract; otherwise the result remains unknown or pending and unsafe repeat submission remains blocked.

The result is recorded as a new observation and triggers fresh evaluation of Context→Need→Rule→Candidate Action→Resolver before any continuation. A confirmed completed transaction excludes retry. A reliably established retryable state may make R3.A2 applicable in a subsequent decision, provided that the original authorisation, payload, idempotency identity and current retry permit remain valid. R3.A5 communicates the resulting evidenced state, R3.A4 exposes recovery controls, and R3.A6 supports local draft resumption. These distinct functions cannot be substituted through TRANSFORM. Repeated query tokens do not dispatch repeated queries, and query completion does not automatically invoke a retry.

## Patch 6 Invariant and execution boundaries

Insert in the state-preservation and execution-admissibility discussion:

The current INV-01–INV-05 predicates protect entered data, valid logical task state, unfinished input, required information and functionality, and authorised service effects. Configuration changes are distinguished from subsequent service-evidence events: installing a reconciliation policy does not itself change transaction truth, while a later validated response may update S and initiate a new decision. Similarly, guided draft restoration requires a separately recorded user authorisation and a compatible, nonconflicting snapshot. If target U equals current U, no redundant configuration mutation occurs; a separately eligible service-interaction event still requires its own fresh token, admission checks and execution trace. Baseline authorisation, validation, idempotency protection, honest feedback and mandatory pre-retry status checking remain active in both adaptive and non-adaptive conditions.

## Patch 7 Closed transformations and deferred decisions

Replace references to an undeclared transformation catalogue with:

Permitted transformations are closed by the action contracts in UAIS-CAT-1.0. A transformation may change only a listed representation, parameterisation or realisation while preserving the action's support purpose, relevant need provenance and invariants. Shared cue/progress and recovery/review realisations retain all contributing action identities. An empty transformation list explicitly prohibits TRANSFORM; legal default values do not automatically constitute purpose-preserving variants. R3.A7 cannot be transformed into retry or submission. Deferred decisions are reconsidered through the full current decision chain, linked to their successors, and checked again immediately before execution. Canonical tie handling is used solely for reproducibility after genuine equality under all six semantic criteria; unknown or unresolved incomparable alternatives are not treated as ties.

## Patch 8 Verification provenance and scope

Replace the passage stating that catalogue-dependent oracle expectations remain undecided with:

The recovered Verification v1.0 package is retained as 35 historical principal cases: 15 decision cases, 12 resolver cases and eight safety cases. Current refinements are represented by versioned child-case specifications and a verification delta rather than changes to the historical records. Catalogue-specific cases examine legal values and guards, independently scoped simplification, preservation of essential routes, mediated reconciliation, safe retry, recovery continuity and complete provenance. A transaction sequence follows ambiguous-result evidence through N6/N7 and R3 to R3.A7, records the status result as a new observation, and then checks retry suppression for completed transactions or separately admitted retry for reliably retryable transactions, with accurate feedback and no duplicate committed effect. These child cases are specified for subsequent execution; no pass outcome is inferred from catalogue finalisation.

## Removal and consistency checklist for the current Section 3

- Replace current catalogue-pending, action-level-unrecovered or six-per-family passages with Patches 1–3. Do not delete historical version explanations.
- Replace a current standalone R2.A6 with the merged R2.A2 scope/provenance description. Retain H:R2.A6 only in historical delta discussion.
- Replace the current seventh-R3 placeholder with R3.A7 and Patch 5.
- Replace incomplete-variant statements with Patch 7 and reference the final contract appendix.
- Keep the existing C1.3 and six-comparator specifications; apply the service-event clarification in Patch 6 wherever 'same U means no action execution' or 'state can never be updated' would otherwise be implied.
- Keep all original 35 historical parent case IDs; reference VER-CAT1 for current child expectations. Never import historical test passes as results of this refinement.
- Preserve the numbering and approved Section 1–2 text. These patches do not introduce Section 4 content.
