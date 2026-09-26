# Revised gap disposition

**SECTION 6 READY TO LOCK — BOUNDED SEMANTIC VERIFICATION**

| Original gap entry | Current disposition | Evidence / boundary |
| --- | --- | --- |
| GAP/browser-reflow | RETAINED AS EXPLICIT BOUNDARY | Controlled C2.2/reachability witnesses; acquisition and rendering are outside this evaluated semantic domain. |
| GAP/full-contract-effects | CLOSED | 24 positive action effects, 10 declared transformations, 14 empty-list transform rejections and an additional missing-value draft restoration. Representative fixture scope/effect coverage only. |
| GAP/canonical-typed-domain | CLOSED | 27 canonical/resolver checks cover exact typed normalisation, ordered/unordered structures, genuine ties, unknown, incomparability, permutation and duplicate equivalent-plan merging. |
| GAP/all-scope-combinations | CLOSED | 16 reachable scoped rule subsets plus five concurrent disposition/conflict scenarios; not exhaustive 24-action combination coverage. |
| GAP/ime-dom-preservation | RETAINED AS EXPLICIT BOUNDARY | Symbolic field/buffer/selection/composition state only; no actual DOM, focus or IME measurement. |

Raw predicate derivation remains an additional explicit limitation: where observations and task-relevance predicates are supplied as controlled witnesses, the tests establish gating and subsequent behaviour given those witnesses, not derivation from natural interaction evidence.

The five historical gap rows remain stored with their original NOT RUN verdicts. The closure assessment changes the current coverage interpretation without editing those records. Browser and actual IME boundaries are neither failed tests nor claimed completed tests.
