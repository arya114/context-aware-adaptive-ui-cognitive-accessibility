# Section 6 core verification closure

Decision: **SECTION 6 READY TO LOCK — BOUNDED SEMANTIC VERIFICATION**.

Final build: UAIS-CORE-0.2.2. Dataset: UAIS-CORE-DATA-1.2. Governing specifications and Sections 1–5 are unchanged. Section 7 is not drafted.

## Reproduce

With Python 3 and its standard library, run these separately from the package directory:

```text
python closure-0.2.2/runner.py
python closure-0.2.2/run_closure.py
```

Each command checks the frozen manifest and creates a uniquely named new run directory. It does not replace the retained runs. The first command executes all 770 legacy deterministic cases and preserves five historical not-run gap records. The second executes the 98 closure additions. The revised coverage register discharges three original gaps and retains two outside-domain boundaries; it does not modify their old records.

## Final evidence

- closure-0.2.2/execution_manifest.json: final pre-execution fingerprints and version lineage.
- closure-0.2.2/closure_inventory.json and closure_expected.json: new cases and frozen expectations.
- closure-0.2.2/runs/20260913T030324Z-075d96fc: 770/770 regression matches.
- closure-0.2.2/closure_runs/20260913T030322Z-8f183b76: 98/98 closure matches.
- closure-assessment-022: final representative trace acceptance and checker negative controls.
- closure-transaction-audit-0.2.2: final TX-1 acceptance.
- closure-0.2.0/equivalence_audit: two retained failed equivalent-plan checks.
- core_results: revised tables, manifest, action results, gap disposition, defect register, Section 6 and exact claim boundary.

The earlier builds, run records, eight trace acceptance failures, five transaction acceptance failures, three initial defects and their retests remain in their original directories. New IMPL-003 covers duplicate-equivalent plan merging; IMPL-004 is a separately labelled code-review finding about synthetic post-query assistance provenance. The latter is not presented as a missing historical failing run.

## Interpretation

The 98 additions comprise 49 action cases (24 positive, ten transformations, fourteen unlisted-transform rejections and one additional restoration), 27 canonical/resolver cases, 21 independently scoped multi-rule scenarios and one query-provenance check. These are representative semantic contract/scenario checks, not exhaustive scope or 24-action-combination enumeration.

Canonical utility cases use schema-tagged synthetic values to exercise the complete supported type structure. Such unit inputs do not add legal numeric or nested parameters to any catalogue action. Executable action cases use their registered property/value bindings. A representative record ID chosen during duplicate-plan merging is metadata for a single identical effect, not a new semantic priority.

Context/feature/reflow/task-relevance predicates remain controlled witnesses where declared. Actual browser acquisition, rendering, DOM/IME behaviour and empirical human outcomes are excluded from the evaluated domain. Same-author implementation/oracle translation remains an assurance limitation.

## Preservation note

The previous ZIP file was not present in the workspace when the new closure archive was prepared. Its recorded checksum and the original source, manifest, result and failure/retest files remain present. Frozen-file hashes were checked; the missing old ZIP's byte identity could not be rechecked. This new archive has a distinct name and checksum and includes the retained evidence directories. No claim is made that it is byte-identical to the old ZIP.
