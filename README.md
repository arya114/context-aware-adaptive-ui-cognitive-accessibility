# Cognitive-accessibility adaptive UI framework — research artifacts

Research companion to **A Context-Aware Rule-Based Adaptive User Interface Framework for Cognitive Accessibility in Digital Public Services**.

Authors (manuscript order): Rosmasari; Ni Made Ary Esta Dewi Wirastuti; Ida Bagus Alit Swamardika; Gede Sukadarmika. Correspondence: rosmasari.2591011025@student.unud.ac.id.

## Status

Repository: https://github.com/arya114/context-aware-adaptive-ui-cognitive-accessibility. This package records the research artifacts prepared on 26 September 2026. No Zenodo record, version release, or journal submission has been made by this workflow. The manuscript is not represented as accepted or published. DOI, license selection and final author approval remain pending.

## Contents

```text
online-resource-1/       Frozen specifications, action catalogue, mappings and binding inspection copies
online-resource-2/       Executable semantic model, frozen inputs and complete historical evidence
  UAIS-verification/    Unmodified extraction of the source evidence archive
  reproduction-check/   Separately labelled 26 September 2026 rerun
docs/                   Provenance and release instructions
CITATION.cff            Citation metadata without fabricated DOI or publication date
LICENSE-DECISION.md     License choices requiring author decision
SHA256SUMS.txt          Package integrity inventory
```

Start with the resource READMEs. To reproduce the selected 868 instances, follow `online-resource-2/README.md`. Python 3.12 and its standard library are sufficient. Frozen build: UAIS-CORE-0.2.2; dataset: UAIS-CORE-DATA-1.2; specification: UAIS-S3-FINAL-1.0; catalogue: UAIS-CAT-1.0; verification obligations: VER-CAT1; fixture: UAIS-VRI-1.0.

## Scientific scope

The model links context evidence, non-diagnostic support needs, concurrent rule/action decisions and state-aware execution in a synthetic village-administration fixture. Final evidence comprises 770 regression cases plus 98 closure cases, covering representative effects for 24 actions. These selected tests do not show exhaustive correctness or measured accessibility benefits. Browser acquisition, rendering, DOM/IME and user studies are outside the evaluated domain. See the exact-claims document in Online Resource 2.

## Citation and identifiers

Use `CITATION.cff` for artifact authorship. Repository: https://github.com/arya114/context-aware-adaptive-ui-cognitive-accessibility. Archive DOI is not yet assigned. After publishing an approved release, add the version-specific DOI, then use the same identifiers in the manuscript, cover letter and supplementary resource descriptions. Never use the manuscript template DOI ending in XXXX.

## Rights and contributions

No new license grant is made by this package. See `LICENSE-DECISION.md`. Preserve frozen files and historical failures. Future changes should create a new version and document changed cases, expectations, code and hashes. Do not overwrite evidence to force agreement.

## Navigation

- [Specifications](specifications/README.md)
- [Verification](verification/README.md)
- [Synthetic data](synthetic-data/README.md)
- [Source code](source-code/README.md)

Online_Resource_1.zip and Online_Resource_2.zip are unchanged supplementary archives. Their extracted contents are also included in the online-resource directories. SHA256SUMS.txt covers this upload package. Historical README statements inside the original resources describe their packaging time.

