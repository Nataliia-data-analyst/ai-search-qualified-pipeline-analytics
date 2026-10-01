# Metric Reconciliation

This document reconciles source-data calculations with the metrics displayed in Looker Studio.

## Source Baseline

Source metrics were independently recalculated from the raw CSV datasets using:

`scripts/validate_metrics.py`

| Metric | Source Value | Looker Value | Difference | Status |
|---|---:|---:|---:|---|
| Brand Presence Rate | 38.12% | TBD | TBD | Pending |
| Citation Rate | 10.31% | TBD | TBD | Pending |
| Answer Accuracy Rate | 79.51% | TBD | TBD | Pending |
| AI Referral Demo CVR | 6.55% | TBD | TBD | Pending |
| Branded CTR | 7.07% | TBD | TBD | Pending |
| Qualified Opportunities | 89 | TBD | TBD | Pending |
| Qualification Rate | 74.17% | TBD | TBD | Pending |
| Paid AI Spend | $25,210.72 | TBD | TBD | Pending |
| Paid AI Conversions | 681 | TBD | TBD | Pending |
| Paid AI CPA | $37.02 | TBD | TBD | Pending |
| Attributed Pipeline | $4,344,616 | TBD | TBD | Pending |
| Pipeline ROAS | 172.33x | TBD | TBD | Pending |

## Validation Rule

A metric receives `PASS` when the Looker Studio result matches the independently calculated source result under the same:

- date range;
- filter context;
- data source;
- metric definition;
- aggregation rule.

## Status Definitions

**PASS** — source and dashboard results match.

**FAIL** — an unexplained discrepancy exists.

**KNOWN ISSUE** — discrepancy or anomaly has been identified and documented.

**PENDING** — dashboard comparison has not yet been completed.

---

## Synthetic Data Realism Notes

### Pipeline ROAS

Source calculation:

```text
$4,344,616 / $25,210.72 = 172.33x
```

The calculation is mathematically consistent with the synthetic source data.

However, the magnitude is unusually high for a realistic paid-media scenario and should therefore be treated as a synthetic-data realism issue rather than evidence of extraordinary campaign performance.

The underlying attributed-pipeline distribution should be reviewed during final synthetic-data QA.

---

## QA Principle

A mathematically correct result can still be analytically suspicious.

Validation therefore distinguishes between:

1. calculation correctness;
2. dashboard correctness;
3. source-data quality;
4. business plausibility.

