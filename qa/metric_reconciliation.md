# Metric Reconciliation

This document records manual reconciliation between source datasets and Looker Studio.

## Acceptance Rule

For each validated KPI:

```text
Source calculation = Looker Studio result
```

after applying the same filters and date scope.

## Reconciliation Table

| Metric | Source | Source Value | Looker Value | Difference | Status |
|---|---|---:|---:|---:|---|
| Brand Presence Rate | AI Presence | TBD | TBD | TBD | Pending |
| Citation Rate | AI Presence | TBD | TBD | TBD | Pending |
| AI Referral Demo CVR | GA4 Traffic | TBD | TBD | TBD | Pending |
| Branded CTR | GSC | TBD | TBD | TBD | Pending |
| Qualified Opportunities | CRM | TBD | TBD | TBD | Pending |
| Paid AI CPA | Paid AI | TBD | TBD | TBD | Pending |
| Pipeline ROAS | Paid AI | TBD | TBD | TBD | Pending |

## Status Definitions

**PASS** — source and dashboard match.

**FAIL** — unexplained difference exists.

**PENDING** — validation has not yet been completed.

**KNOWN ISSUE** — difference or anomaly has been explained and documented.

