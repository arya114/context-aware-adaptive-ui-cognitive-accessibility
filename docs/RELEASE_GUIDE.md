# GitHub / Zenodo release preparation

1. The repository is `arya114/context-aware-adaptive-ui-cognitive-accessibility`. Confirm author agreement, exact institution/ORCID metadata and artifact licenses before a versioned release.
2. Use this directory as the repository root. Keep cover letters and administrative correspondence outside the public repository. Original files contain historical research notes and version labels; review them as release content without silently changing frozen bytes.
3. Review `CITATION.cff`: full personal names are preserved in `family-names` to avoid guessing how Balinese names should be split; authors should confirm their desired citation-name encoding. Add approved license and actual release date. The artifact version 0.2.2 refers to the evaluated model, not a claim that a versioned public release already exists.
4. Verify SHA-256 fingerprints and rerun the two documented commands on a copy. Preserve the five historical not-run records and separate new runs from original evidence.
5. Upload reviewed artifacts to the existing repository and arrange a versioned release after author and license decisions. Enable the repository in Zenodo before creating a release if using GitHub integration; alternatively deposit a reviewed archive directly. This package has not made a release or Zenodo deposit.
6. Check the actual Zenodo record, creators, license and files. Record the version-specific DOI used for the reproducibility snapshot, plus the concept DOI if provided. Do not invent or infer either identifier.
7. Update README, CITATION.cff, manuscript Availability of Data and Materials and cover letter with the same real URL/DOI. Verify unauthenticated access and downloaded hashes. If files change, recalculate package hashes and record a new artifact version as appropriate.
8. Compile and review the manuscript after inserting links and literature changes. Author confirmation remains necessary before journal submission; no submission is part of this task.

Zenodo sources checked 26 September 2026:
- https://help.zenodo.org/docs/github/archive-software/github-upload/
- https://help.zenodo.org/docs/github/describe-software/citation-file/

Only CITATION.cff is supplied to avoid conflicting metadata: Zenodo documentation says a .zenodo.json file takes precedence over CITATION.cff. No DOI, release date or license has been fabricated.
