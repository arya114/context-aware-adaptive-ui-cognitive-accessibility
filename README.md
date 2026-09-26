# Cognitive-Accessibility Adaptive UI Framework --- Research Artifacts

Research companion to **A Context-Aware Rule-Based Adaptive User
Interface Framework for Cognitive Accessibility in Digital Public
Services**.

**Authors (manuscript order):** Rosmasari; Ni Made Ary Esta Dewi
Wirastuti; Ida Bagus Alit Swamardika; Gede Sukadarmika.\
**Correspondence:** rosmasari.2591011025@student.unud.ac.id

## Status

This repository contains the research artifacts prepared for the
evaluated framework and its reproducibility materials.

-   **Repository:**
    https://github.com/arya114/context-aware-adaptive-ui-cognitive-accessibility
-   **Artifact version:** 0.2.3
-   **Frozen build:** UAIS-CORE-0.2.2
-   **Dataset:** UAIS-CORE-DATA-1.2
-   **Specification:** UAIS-S3-FINAL-1.0
-   **Action catalogue:** UAIS-CAT-1.0
-   **Verification obligations:** VER-CAT1
-   **Fixture:** UAIS-VRI-1.0
-   **Archive DOI:** https://doi.org/10.5281/zenodo.22971444
-   **Journal publication:** not represented as accepted or published by
    this repository

The **artifact version 0.2.3** identifies the versioned public archive
release. The **frozen build UAIS-CORE-0.2.2** identifies the evaluated
model contained in the release.

The version-specific archive DOI is:

https://doi.org/10.5281/zenodo.22971444

The DOI should be used consistently when citing this versioned research
artifact.

## Contents

``` text
docs/
  RELEASE_GUIDE.md
  SOURCE_MANIFEST.json

online-resource-1/
  Frozen specifications, action catalogue, mappings and binding
  inspection copies

online-resource-2/
  Executable semantic model, frozen inputs and complete historical
  verification evidence
  ├── UAIS-verification/
  └── reproduction-check/

source-code/
  Navigation to the final evaluated implementation

specifications/
  Navigation to the frozen specifications

synthetic-data/
  Navigation to the synthetic service fixture and frozen inputs

verification/
  Navigation to the canonical verification evidence

CITATION.cff
  Citation metadata for the versioned research artifact

LICENSE
  MIT License for source code and software materials

LICENSE-CC-BY-4.0.md
  CC BY 4.0 terms for non-software research materials

LICENSE-DECISION.md
  Repository licensing decision

SHA256SUMS.txt
  Integrity inventory for the package

Online_Resource_1.zip
Online_Resource_2.zip
  Unchanged supplementary archives
```

Start with the resource READMEs:

-   [Online Resource 1](online-resource-1/README.md)
-   [Online Resource 2](online-resource-2/README.md)
-   [Specifications](specifications/README.md)
-   [Verification](verification/README.md)
-   [Synthetic data](synthetic-data/README.md)
-   [Source code](source-code/README.md)
-   [Release guide](docs/RELEASE_GUIDE.md)

## Reproduction

The final evaluated build can be reproduced with **Python 3.12 and the
Python standard library only**.

From:

``` text
online-resource-2/UAIS-verification/
```

run:

``` text
python closure-0.2.2/runner.py
python closure-0.2.2/run_closure.py
```

The scripts verify the frozen inputs before execution and create
uniquely named run directories.

Expected results:

-   **770** regression cases: 770 Pass, 0 Fail, 0 Unresolved, with 5
    historical Not-run placeholders.
-   **98** closure cases: 98 executed, 98 Pass, 0 Fail.
-   **868 unique executed instances** in total.
-   Oracle-tag rows overlap and must not be summed as additional test
    instances.

The five historical Not-run records are preserved as historical
evidence. They are not additional executable failures.

For detailed evidence lineage and reproduction instructions, see [Online
Resource 2](online-resource-2/README.md).

## Scientific scope

The model links:

``` text
Context evidence
     ↓
Support needs
     ↓
Concurrent rule/action decisions
     ↓
State-aware execution
     ↓
Adaptive UI actions
```

The evaluated fixture uses a **synthetic village-administration
service** and covers representative effects for the final 24-action
catalogue.

The verification evidence demonstrates agreement for the selected frozen
semantic-model scenarios. It does **not** establish:

-   exhaustive correctness across all possible contexts or state
    combinations;
-   independent validity of the verification oracle;
-   browser-level accessibility;
-   rendering, DOM, IME, or browser reflow behaviour;
-   measured human accessibility or usability benefits;
-   production readiness;
-   full action-combination or state-space coverage.

Browser acquisition, rendering and empirical user evaluation are outside
the evaluated domain. No participant or personal evaluation dataset is
included in this repository.

## Research artifacts

### Online Resource 1

Contains the frozen framework specifications, action catalogue,
bindings, mappings and related historical context used to document the
evaluated framework.

Key materials include:

-   governing specifications;
-   framework and resolver definitions;
-   the 24-action catalogue;
-   action contracts;
-   verification obligations and lineage;
-   synthetic service and fixture specifications;
-   executable semantic bindings.

See [Online Resource 1 README](online-resource-1/README.md) for the
manuscript crosswalk.

### Online Resource 2

Contains the executable semantic model, frozen regression and closure
inputs, original verification evidence, historical failures and retests,
trace audits, and the separately labelled reproduction check.

The original evidence archive is preserved without silently rewriting
historical failures or results.

See [Online Resource 2 README](online-resource-2/README.md) for the
complete evidence map.

## Citation and identifiers

Use [CITATION.cff](CITATION.cff) for artifact authorship and citation
metadata.

The versioned public archive for this repository is:

**Artifact version:** 0.2.3\
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22971444

This DOI identifies the archived v0.2.3 research artifact. The frozen
evaluated build remains **UAIS-CORE-0.2.2**.

Use the same version-specific DOI in the manuscript, cover letter and
supplementary-material description.

Do not use placeholder DOI values.

## Licensing

This repository uses a **split licensing model**.

### Source code and software materials

Source code and software materials are released under the **MIT
License**, unless a specific file or subdirectory states otherwise.

See [LICENSE](LICENSE).

### Non-software research materials

Non-software research materials are released under the **Creative
Commons Attribution 4.0 International License (CC BY 4.0)**, unless a
specific file or subdirectory states otherwise.

This includes, where applicable:

-   research specifications and documentation;
-   synthetic research data;
-   verification materials;
-   reproducibility materials;
-   research reports and supporting documentation;
-   other non-software research materials.

See [LICENSE-CC-BY-4.0.md](LICENSE-CC-BY-4.0.md) and
[LICENSE-DECISION.md](LICENSE-DECISION.md).

## Integrity and versioning

Frozen research evidence should not be overwritten to force agreement
with later executions.

Future changes should:

1.  create a new artifact version where appropriate;
2.  document changed cases, expectations, code and hashes;
3.  preserve historical failures and retests;
4.  recalculate relevant SHA-256 inventories;
5.  keep new reproduction runs separately labelled from original
    evidence.

The package-level integrity inventory is provided in
[SHA256SUMS.txt](SHA256SUMS.txt).

## Release preparation

Before creating a versioned release or archive deposit:

-   confirm author names, affiliations and ORCID metadata;
-   confirm the selected licenses;
-   verify SHA-256 fingerprints;
-   review the preserved historical evidence;
-   rerun the documented reproduction commands on a copy;
-   review the actual archive metadata and DOI after deposit;
-   update the manuscript and supplementary-material references
    consistently.

See [docs/RELEASE_GUIDE.md](docs/RELEASE_GUIDE.md).

## Repository boundaries

This repository is a research artifact package. The synthetic fixture is
**not** an official government workflow, clinical instrument, or
production service.

The repository should not be interpreted as evidence of production
deployment or measured accessibility benefit beyond the declared
verification domain.

------------------------------------------------------------------------

**Repository:**
https://github.com/arya114/context-aware-adaptive-ui-cognitive-accessibility\
**Artifact version:** 0.2.3\
**DOI:** https://doi.org/10.5281/zenodo.22971444
