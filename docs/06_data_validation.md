# Data Quality & Validation

The purpose of this QA layer is to ensure that the **AI Search → Qualified Pipeline Analytics** dashboard reports metrics consistently with its underlying source data.

A visually correct dashboard can still produce incorrect business conclusions if field types, aggregation rules, filters, joins or calculated metrics are configured incorrectly.

---

## Validation Framework

The project uses four validation layers:

```text
Source Data
    ↓
Field & Type Validation
    ↓
Metric & Aggregation Validation
    ↓
Dashboard Reconciliation
    ↓
Business Interpretation
```

---

## 1. Source Structure Validation

Checks performed or planned:

- one header row per dataset;
- no merged cells;
- consistent column names;
- consistent date structure;
- numeric values stored as numeric fields;
- currency fields validated;
- null values reviewed;
- duplicate records checked;
- source grain documented;
- processed data separated from raw data.

---

## 2. Field Type Validation

Important Looker Studio field types include:

| Field | Expected Type |
|---|---|
| Week | Date |
| Created_Date | Date |
| Mentioned | Number / Boolean indicator |
| Linked_Citation | Number / Boolean indicator |
| Accurate | Number / Boolean indicator |
| Sessions | Number |
| Impressions | Number |
| Clicks | Number |
| CTR | Percent |
| Spend_USD | Currency |
| Opportunity_Value_USD | Currency |
| Pipeline_Value_USD | Currency |
| Attributed_Pipeline_USD | Currency |

Currency fields remain additive numeric measures.

Percentages are not summed across rows.

---

## 3. Aggregation Validation

A major QA focus is avoiding incorrect aggregation.

### Example: CTR

Incorrect:

```text
SUM(CTR)
```

or, for unequal groups:

```text
AVG(CTR)
```

Preferred:

```text
SUM(Clicks) / SUM(Impressions)
```

The same principle applies to CVR and other ratio metrics.

---

## 4. AI Presence Validation

### Brand Presence Rate

```text
SUM(Mentioned) / COUNT(Mentioned)
```

Expected format:

```text
Percent
```

### Citation Rate

```text
SUM(Linked_Citation) / COUNT(Linked_Citation)
```

Expected format:

```text
Percent
```

### Historical QA Finding

During dashboard development, an incorrectly aggregated citation metric produced an implausible value such as:

```text
32,000%
```

This was treated as a QA signal rather than a business result.

Root-cause review focused on:

- source field type;
- default aggregation;
- calculated-field formula;
- percentage formatting.

This illustrates why dashboard outputs must be reconciled against source counts.

---

## 5. Paid Media Validation

### Spend

```text
SUM(Spend_USD)
```

Format:

```text
Currency
```

### Attributed Pipeline

```text
SUM(Attributed_Pipeline_USD)
```

Format:

```text
Currency
```

### CPA

```text
SUM(Spend_USD) / SUM(Conversions)
```

Format:

```text
Currency
```

CPA is not a percentage.

### Pipeline ROAS

```text
SUM(Attributed_Pipeline_USD) / SUM(Spend_USD)
```

Format:

```text
Decimal / X
```

Pipeline ROAS is not a percentage unless the reporting convention explicitly requires percentage representation.

---

## 6. Funnel Validation

The paid AI funnel uses:

```text
Impressions
    ↓
Clicks
    ↓
Conversions
```

The processed funnel dataset is:

`data/processed/09_paid_ai_funnel.csv`

Validation checks include:

- Impressions = total source impressions;
- Clicks = total source clicks;
- Conversions = total source conversions;
- Stage order is preserved;
- funnel values are numeric;
- no percentage formatting is applied to stage volumes.

The aggregated funnel represents the selected prepared scope and does not automatically inherit every dimension available in the detailed paid-media source.

---

## 7. CRM Validation

CRM metrics are validated at opportunity grain.

Checks include:

- unique `Opportunity_ID`;
- qualification logic;
- win logic;
- opportunity value;
- self-reported source;
- sales-cycle values.

### Known Synthetic Data Anomaly

The synthetic dataset currently contains a segment where:

```text
AI self-reported opportunities = 20
Qualified AI self-reported opportunities = 20
```

which produces:

```text
Qualification Rate = 100%
```

The calculation can be mathematically correct while the synthetic source distribution is unrealistic.

Status:

**Pending synthetic-data adjustment during final QA.**

This distinction is important:

> A surprising dashboard value does not automatically mean the dashboard formula is wrong.

The source data must also be investigated.

---

## 8. Date Validation

Date controls require genuine date fields rather than text labels.

Checks include:

- `Week` recognized as Date;
- `Created_Date` recognized as Date;
- chart date dimensions use the intended grain;
- date-range controls affect the intended charts;
- comparison periods are interpreted consistently.

---

## 9. Filter Validation

Page-level controls should be tested independently.

Examples:

- Assistant
- Channel Group
- Session Source
- Query Type
- Self-Reported Source
- Platform

Validation questions:

1. Does the filter affect the intended charts?
2. Does it leave unrelated data sources unchanged?
3. Does selecting all values reproduce the unfiltered total?
4. Do empty selections create misleading results?
5. Are charts using compatible sources?

---

## 10. Cross-Source Validation

Raw datasets are not joined blindly on `Week`.

Different grains can create many-to-many duplication.

Cross-source comparisons should use:

`data/processed/06_weekly_kpis.csv`

or another explicitly aggregated common-grain layer.

---

## 11. Reconciliation Principle

For key KPIs:

```text
Source Value
      =
Looker Studio Value
```

within the expected calculation and filtering scope.

Any difference should be investigated before business conclusions are accepted.

---

## 12. QA Status

| Area | Status |
|---|---|
| Source structure | Validated / ongoing |
| Field types | Validated / ongoing |
| Core aggregation rules | Defined |
| AI presence calculations | Validated |
| Paid media calculations | Validated |
| Funnel structure | Validated |
| CRM synthetic anomaly | Pending adjustment |
| Date controls | Final QA pending |
| Filter interactions | Final QA pending |
| Full metric reconciliation | Final QA pending |

---

## Key QA Principle

> Never trust a dashboard metric only because it looks plausible.

Validation should confirm the source data, field type, aggregation rule, filter context and business definition before the metric is used for decision-making.

