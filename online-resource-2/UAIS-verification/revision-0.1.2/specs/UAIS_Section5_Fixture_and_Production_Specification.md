# Section 5 fixture and production specification

Status: newly specified research bindings, not recovered implementation evidence. Governing framework: UAIS-S3-FINAL-1.0; catalogue: UAIS-CAT-1.0; verification: VER-CAT1. No framework contract is superseded by this fixture.

## Versioned service fixture

ServiceID: VILLAGE-RESIDENCE-DEMO. ServiceVersion: 1.0.0. FixtureID: UAIS-VRI-1.0. Operation OP01 records a simulated residence-statement application. It does not issue an official certificate. Every field and requirement below is a research-fixture choice, not a statement of government procedure. Source code, deployed backend and executed traces are not supplied or claimed by this document.

### Field and validation registry

| FieldID | Type and fixture value domain | Predicate | Applicability |
| --- | --- | --- | --- |
| FLD01 | Applicant name; synthetic text | VAL01: nonempty after whitespace check; retain original entered value | Required |
| FLD02 | Synthetic resident reference | VAL02: exactly RES- followed by four decimal digits | Required; no national identity number |
| FLD03 | Address; synthetic text | VAL03: nonempty after whitespace check | Required |
| FLD04 | Purpose enum: administrative, other | VAL04: member of the declared enum | Required |
| FLD05 | Purpose detail text | VAL05: nonempty when FLD04=other | Conditional; preserve existing value when inapplicable |
| FLD06 | Boolean declaration linked to reviewed payload revision | VAL07: true and REVIEW01 hash/revision matches current candidate payload | Required before OP01 authorisation |

VAL06 applies to DOC01: an owned upload reference is accepted by the simulated service, with detected media type application/pdf or image/jpeg, byte size greater than zero and at most 2,097,152, and matching content reference. These formats and size are fixture constants, not adaptation thresholds or official requirements. Filename suffix alone is not an acceptance witness. Missing upload evidence does not satisfy VAL06. Replace an upload only through an explicit user action; retain the previous reference until the new accepted reference is coherently committed.

### Requirements, documents and content

| Identity | Meaning and dependency |
| --- | --- |
| REQ01 | Applicant data: VAL01–VAL03 true |
| REQ02 | Address evidence: DOC01 and VAL06 true |
| REQ03 | Review declaration: VAL07 true for the current payload |
| DOC01 | Synthetic address-evidence document role; each upload attempt has an UploadID and content reference |
| REVIEW01 | Read-only rendering of FLD01–FLD05, applicability flags, accepted DOC01 reference and payload revision |
| INFO01 | Mandatory explanation that this is a simulated application, with fixture requirements and permitted continuation |
| TERM01 | “Address evidence”: a synthetic document attached for this fixture; it is not checked against a government eligibility standard |
| NAV01 | Required access to current position and legal next/back/review routes |
| OPT01 | Optional decorative illustration; reduction cannot remove instructions |
| OPT02 | Secondary explanation duplicating information accessible through a retained required route |
| ASSET01 / ASSET01-L | Registered normal/lighter illustration pair with identical optional informational role; asset bytes and hashes must accompany a later implementation |

Stage instruction IDs INFO-ST01 through INFO-ST07 bind plain-language instructions to the corresponding StepIDs. Field examples EX-FLD03, EX-FLD05 and EX-DOC01 use synthetic content and are labelled examples, never prefilled evidence of the applicant's circumstances. Required status, error and recovery objects are protected from optional reduction.

### Navigation and dependency registry

The declared forward graph is ST01→ST02→ST03→ST04→ST05→ST06→ST07. ST01 requires the service selection; ST03→ST04 requires VAL01–VAL03; ST04→ST05 requires VAL04–VAL06; ST05→ST06 requires VAL07 plus current explicit authorisation. ST06→ST07 follows dispatch, including response-loss cases. A pending upload cannot satisfy the ST04 gate.

Editable backward edges are ST02→ST01, ST03→ST02, ST04→ST03, ST05→ST03 and ST05→ST04 before transaction dispatch. A ST07→ST05 view is read-only while X is pending, unknown or completed. Terminal rejection permits an explicit correction branch to ST03 or ST04, with a new draft/payload revision, fresh review and new authorisation. There is no automatic resubmit edge. Completed transactions have no editing edge that changes the historical committed payload.

Dependencies include FLD04→FLD05 applicability; FLD01–FLD05 plus DOC01→REVIEW01; REVIEW01→FLD06 declaration→OP01 authorisation. An accepted payload change invalidates the earlier review/declaration and affected dependent validity. “Preserve valid progress” does not preserve validation that its own prerequisite change has invalidated. Stored values remain available for correction. Legal navigation never clears values merely because the presentation changes.

C4.1 contains seven steps, this graph, these dependencies and rollback boundaries. C4.2 contains three requirements, text/document/declaration types, their dependencies and declared file formats. C4.3 contains six fields, one conditional field, seven predicates, one upload role and one review object. Applicable counts and unknown metadata remain distinct from total declared counts. None is converted into a low/medium/high score.

### State and capability schema

S references service/manifest version, current StepID, accepted values and applicability, input revision, active FieldID, unfinished buffer, selection and composition flag; owned draft ID/revision; upload attempt/status/content references; review hash; transaction and pending-operation references; assistance and connectivity episodes; and deferred predecessor/successor records. UI state U has only G, D, P and F. Catalogue properties and legal values remain authoritative.

Capabilities are independently witnessed for field/composition event handling, file selection, upload transfer, versioned draft read/write and authenticated submission/status requests. Failure of draft persistence does not imply loss of the currently held input; it prevents claiming successful persistence. When a required service capability is unavailable, required information and an explanation remain reachable and the unsafe operation is blocked. Feature checks themselves do not add mapping edges.

### Synthetic payload and transaction branches

An illustrative payload reference p1 points to: FLD01="Synthetic Applicant A"; FLD02="RES-0001"; FLD03="Fixture Lane 1"; FLD04="other"; FLD05="Research demonstration"; accepted DOC01 reference doc-fixture-01; and its service/review revisions. FLD06 authorisation is a separate current record bound to that payload. The document reference is a scenario input requiring corresponding synthetic bytes and acceptance evidence when executed; it is not an already uploaded file.

Transaction X, key k, operation OP01, payload p1 and authorisation a1 remain associated throughout retries. The simulated ledger contract enforces at most one committed effect per k and rejects reuse with mismatched operation/payload/ownership. Status responses carry transaction/key, service version, revision and evidence source. A read-only query cannot change the ledger or allocate a transaction.

| Existing TX-1 branch | Fixture evidence supplied in a later run | Contract consequence |
| --- | --- | --- |
| X-C | Matching completed receipt | No retry; retain existing effect; evidenced completion feedback |
| X-P | Matching pending record | Withhold retry; pending feedback; no automatic query loop |
| X-R | Matching safely_retryable attestation and current permit | New full mediated decision may admit one permitted same-identity attempt |
| X-F | Matching terminal rejection | Suppress retry; explicit correction/review/authorisation required for a new payload |
| X-U | Absent, lost, stale, conflicting or wrong-identity evidence | No completion or retry permit inferred; preserve safe status handling |

These branches instantiate VER-CAT1 fixture X; they do not replace its oracle. Ledger truth and client-known status are separately represented. A timed-out dispatch can already have a committed effect. Command attempts, transaction identities and committed effects must be counted separately in eventual records. Baseline safety remains active in all comparison conditions.

## Figure 4 — Instantiated service architecture

Purpose: locate framework roles in the specified application, rather than redraw Section 4's generic logic. Produce one landscape diagram with an application boundary containing: (1) Service UI with field/help/upload/review/status regions; (2) Context Observers; (3) Context/Need Decision Engine, internally labelled C→N→R→candidate actions; (4) Action Resolver and execution gate; (5) Adaptive State Store U=[G,D,P,F]; (6) Runtime/Service State S; (7) Logging. Place the versioned manifest adjacent to the engine/state inputs and a Simulated Service/Backend outside the application boundary.

Solid event arrows: UI→Observers; backend responses→Observers; Observers→Engine; Engine→Resolver. Resolver proposals pass through the execution gate before updating U; U configures the same UI. The gate dispatches admitted service interactions through a service adapter to the simulator. The simulator's validated responses update S through an acceptance boundary, then initiate fresh observations/decisions. Initial authorised submission also enters this adapter through its explicit service contract; it is not invented as an adaptive action.

Dashed dependency arrows: manifest→Engine/Resolver; S and current U→Resolver/gate. Dotted record arrows connect observations, decisions and execution/service results to the three logger roles. Place the simulated ledger in the backend, with “accepted transaction evidence” inside S. Do not label U as transaction truth. Do not draw backend/query-result→retry or Context→Action shortcuts. Show baseline safety at the service adapter with distinct provenance.

Caption: **Figure 4. Placement of the framework in the specified village-service instantiation. A single service interface binds semantic manifest objects to context observation, need-mediated decisions and guarded action application. Adaptive configuration U is distinct from runtime and accepted service evidence S. The simulated backend supplies transaction evidence through validated responses; logging accompanies observation, decision and execution boundaries. The diagram specifies component responsibilities and does not report a deployed implementation.**

This deliverable is a figure specification and caption, not a rendered image. Distinguish arrow types by line pattern as well as colour. Keep labels legible in grayscale. Final dimensions and numbering follow manuscript assembly.

## Table placement and supplementary allocation

Recommended main tables: service workflow, context acquisition, representative mediated paths, and all 24 action bindings. Tables 6–9 follow first appearance: workflow, acquisition, mediated paths, then action bindings. Final numbering is reconciled with the assembled manuscript. The compact example trace can remain an unnumbered schema display or receive the next available number. Do not reproduce the twenty-field contracts in Section 5.

Extend the Section 4 supplement allocation without replacing existing material:

- S5: append this versioned service manifest, IDs, predicates, dependencies, capabilities and TX-1 fixture bindings.
- S3: append Table 9's concrete binding configuration alongside, but separate from, the unchanged normative action contracts; retain optional scope identities and registered asset references.
- S6: append fixture/scenario references to existing historical and VER-CAT1 case IDs; retain their expected outcomes and NOT RUN status. Supply payload/document bytes and event schedules with a later execution package.
- S7: append illustrative trace schema and synthetic records, clearly separated from future executed logs. Include observation scope/quality, need/edge provenance, all candidates, comparisons, invariant/guard evidence, versions, commands/results, permits and predecessor/successor links.

Implementation assets, simulator code and executed datasets are not bundled with this manuscript specification. Before making any implementation or execution claim, the corresponding artifacts and records must be supplied and assessed. This production boundary does not require reopening the locked framework.
