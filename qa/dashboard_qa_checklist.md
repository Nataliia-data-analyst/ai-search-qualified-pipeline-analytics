# Looker Studio Dashboard QA Checklist

## Data Sources

- [ ] Correct Google Sheets / CSV source connected
- [ ] Correct worksheet selected
- [ ] Source range includes all required rows
- [ ] Headers are unique and stable
- [ ] No merged cells
- [ ] No unexpected blank rows
- [ ] Source grain documented

## Field Types

- [ ] Dates recognized as Date
- [ ] Counts recognized as Number
- [ ] Currency fields recognized as Currency / Number
- [ ] Percent fields correctly formatted
- [ ] Boolean indicators consistently represented
- [ ] No numeric measures stored as text

## Aggregation

- [ ] Additive metrics use SUM
- [ ] IDs are not accidentally summed
- [ ] CTR uses SUM(Clicks) / SUM(Impressions)
- [ ] CVR uses ratio of aggregated components
- [ ] CPA uses SUM(Spend) / SUM(Conversions)
- [ ] Pipeline ROAS uses SUM(Pipeline) / SUM(Spend)
- [ ] No unintended average-of-averages calculations
- [ ] No double aggregation

## AI Presence

- [ ] Brand Presence reconciled with source
- [ ] Citation Rate reconciled with source
- [ ] Accuracy denominator confirmed
- [ ] Assistant filter works
- [ ] Buyer Prompt filter works
- [ ] Weekly trend matches source

## Acquisition

- [ ] Sessions reconcile with source
- [ ] Demo Requests reconcile with source
- [ ] Demo CVR calculation verified
- [ ] AI Referral filter verified
- [ ] Organic comparison verified
- [ ] Direct comparison verified

## Branded Search

- [ ] Impressions reconcile
- [ ] Clicks reconcile
- [ ] Weighted CTR verified
- [ ] Date dimension verified
- [ ] Period comparisons checked

## CRM

- [ ] Opportunity IDs are unique
- [ ] Qualified logic verified
- [ ] Win logic verified
- [ ] Pipeline values reconcile
- [ ] Self-reported AI filter verified
- [ ] 100% qualification anomaly reviewed

## Paid AI

- [ ] Spend reconciles
- [ ] Impressions reconcile
- [ ] Clicks reconcile
- [ ] Conversions reconcile
- [ ] CTR verified
- [ ] CVR verified
- [ ] CPA verified
- [ ] Attributed Pipeline reconciles
- [ ] Pipeline ROAS verified
- [ ] Platform comparison verified

## Funnel

- [ ] Impressions total verified
- [ ] Clicks total verified
- [ ] Conversions total verified
- [ ] Stage order correct
- [ ] Values displayed as numbers, not percentages

## Filters & Controls

- [ ] Date control works
- [ ] Page filters affect intended charts
- [ ] Filters do not unexpectedly affect unrelated sources
- [ ] Reset restores baseline
- [ ] Empty states are understandable

## Presentation

- [ ] Currency formatting consistent
- [ ] Percentage precision consistent
- [ ] KPI names understandable
- [ ] Titles describe business questions
- [ ] No overlapping elements
- [ ] Charts remain readable
- [ ] Insights do not overstate causality

## Final Acceptance

- [ ] Five key KPIs manually reconciled
- [ ] Known anomalies documented
- [ ] Dashboard screenshots updated
- [ ] Synthetic-data disclaimer visible
- [ ] Business conclusions reviewed against limitations

