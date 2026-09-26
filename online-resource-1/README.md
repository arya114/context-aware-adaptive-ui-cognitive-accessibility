# Online Resource 1 — Framework specifications and bindings

Companion to **A Context-Aware Rule-Based Adaptive User Interface Framework for Cognitive Accessibility in Digital Public Services**.

This resource assembles existing research specifications without changing their scientific content. The frozen specifications bundled with the final evaluated build are authoritative for reproducing that build. Original UAIS identifiers are retained as version provenance; they do not indicate an active journal submission.

## Reading order and manuscript crosswalk

| Manuscript topic | Source file |
|---|---|
| Section 3.9: governing versions; Section 3 operational decisions | `specifications/UAIS_Section3_Final_Completion_Decisions.md` (UAIS-S3-FINAL-1.0) |
| Section 4: framework, mapping, resolver, invariants and traces | `specifications/UAIS_Section4_Proposed_Framework.md` |
| Section 4.5 / Table 4: 24 actions, distribution 6–5–7–6 | `specifications/UAIS_Final_Action_Catalogue.md`, `UAIS_Final_Action_Contracts.json` and identical `catalogue.json` (UAIS-CAT-1.0) |
| Verification obligations and lineage | `specifications/UAIS_Final_Verification_Delta.md`, `UAIS_Historical_Mapping_Verification_Import.md`, `UAIS_Verification_Child_Index.json` (VER-CAT1) |
| Section 5: synthetic service, scopes and fixture | `specifications/UAIS_Section5_Framework_Instantiation.md`, `UAIS_Section5_Fixture_and_Production_Specification.md`; `bindings/service_manifest.json` |
| Executable property, value and scope bindings | `bindings/semantic.py` and `bindings/model.py`, copied byte-for-byte from UAIS-CORE-0.2.2 |
| Historical derivation and editorial context | `historical-context/`; these records are explanatory, not replacements for frozen specifications |

Some source notes say verification is pending, because they were written before execution. These are preserved historical statuses. For final results use Online Resource 2, not those earlier readiness statements. Relative links inside original source documents may refer to their earlier authoring workspace; use this reading map for the packaged equivalents.

The binding files here are inspection copies. Run the complete executable package in Online Resource 2; do not try to execute this partial binding directory in isolation. No new contracts, cases, observations, empirical data or expected outcomes have been invented.

## Boundaries

The fixture is synthetic. It is not an official government workflow, a clinical instrument or a production service. Browser acquisition, DOM/IME behaviour, rendering and empirical user outcomes remain outside the evaluated domain. Full action-combination or state-space coverage is not claimed.

## Integrity and publication

`SHA256SUMS.txt` fingerprints this resource. Public repository URL, archive DOI and license selection are pending. Local assembly is complete; public availability has not yet been established.
