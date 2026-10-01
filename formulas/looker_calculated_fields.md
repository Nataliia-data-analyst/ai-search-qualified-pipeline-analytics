# Looker Studio Calculated Fields

## AI Presence

### Brand Presence Rate
```text
SUM(Mentioned) / COUNT(Mentioned)
```
Format: Percent

### Citation Rate
```text
SUM(Linked_Citation) / COUNT(Linked_Citation)
```
Format: Percent

### Answer Accuracy Rate
```text
SUM(Accurate) / SUM(Mentioned)
```
Format: Percent

---

## GA4 Traffic

### Demo Conversion Rate
```text
SUM(Demo_Requests) / SUM(Sessions)
```
Format: Percent

### Qualified Opportunity Rate
```text
SUM(Qualified_Opps) / SUM(Sessions)
```
Format: Percent

### Pipeline per Session
```text
SUM(Pipeline_Value_USD) / SUM(Sessions)
```
Format: Currency (USD)

---

## GSC

### Weighted CTR
```text
SUM(Clicks) / SUM(Impressions)
```
Format: Percent

---

## CRM

### Qualification Rate
```text
SUM(Qualified) / COUNT_DISTINCT(Opportunity_ID)
```
Format: Percent

### Win Rate
```text
SUM(Won) / COUNT_DISTINCT(Opportunity_ID)
```
Format: Percent

### Average Opportunity Value
```text
SUM(Opportunity_Value_USD) / COUNT_DISTINCT(Opportunity_ID)
```
Format: Currency (USD)

---

## Paid AI

### CTR
```text
SUM(Clicks) / SUM(Impressions)
```
Format: Percent

### Conversion Rate
```text
SUM(Conversions) / SUM(Clicks)
```
Format: Percent

### CPA
```text
SUM(Spend_USD) / SUM(Conversions)
```
Format: Currency (USD)

### Pipeline ROAS
```text
SUM(Attributed_Pipeline_USD) / SUM(Spend_USD)
```
Format: Decimal
