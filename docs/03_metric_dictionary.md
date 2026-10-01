# Metric Dictionary

This document defines the key business and analytical metrics used in the **AI Search → Qualified Pipeline Analytics** project.

---

## 1. AI Search Visibility

### Brand Presence Rate

**Business question:** How often does NovaFlow appear in AI answers to high-intent buyer prompts?

```text
SUM(Mentioned) / COUNT(Mentioned)
```

**Format:** Percent  
**Source:** `01_ai_presence.csv`

---

### Citation Rate

**Business question:** How often does an AI answer include a linked citation to NovaFlow?

```text
SUM(Linked_Citation) / COUNT(Linked_Citation)
```

**Format:** Percent  
**Source:** `01_ai_presence.csv`

---

### Answer Accuracy Rate

**Business question:** When NovaFlow is mentioned, how often is it described accurately?

```text
SUM(Accurate) / SUM(Mentioned)
```

**Format:** Percent  
**Source:** `01_ai_presence.csv`

**Important:** Accuracy is evaluated relative to brand mentions, not all AI answers.

---

## 2. Website Acquisition

### Demo Conversion Rate

```text
SUM(Demo_Requests) / SUM(Sessions)
```

**Format:** Percent  
**Source:** `02_ga4_traffic.csv`

---

### Qualified Opportunity Rate

```text
SUM(Qualified_Opps) / SUM(Sessions)
```

**Format:** Percent  
**Source:** `02_ga4_traffic.csv`

---

### Pipeline per Session

```text
SUM(Pipeline_Value_USD) / SUM(Sessions)
```

**Format:** USD  
**Source:** `02_ga4_traffic.csv`

This metric helps compare traffic quality rather than traffic volume alone.

---

## 3. Branded Search

### Branded CTR

```text
SUM(Clicks) / SUM(Impressions)
```

**Format:** Percent  
**Source:** `03_gsc_branded.csv`

Do not use:

```text
AVG(CTR)
```

for multi-week or grouped analysis.

---

## 4. CRM & Pipeline

### Qualification Rate

```text
SUM(Qualified) / COUNT_DISTINCT(Opportunity_ID)
```

**Format:** Percent  
**Source:** `04_crm_opportunities.csv`

---

### Win Rate

```text
SUM(Won) / COUNT_DISTINCT(Opportunity_ID)
```

**Format:** Percent  
**Source:** `04_crm_opportunities.csv`

---

### Total Opportunity Value

```text
SUM(Opportunity_Value_USD)
```

**Format:** USD  
**Source:** `04_crm_opportunities.csv`

---

### Average Opportunity Value

```text
SUM(Opportunity_Value_USD) / COUNT_DISTINCT(Opportunity_ID)
```

**Format:** USD  
**Source:** `04_crm_opportunities.csv`

---

### Average Sales Cycle

```text
AVG(Sales_Cycle_Days)
```

**Format:** Number / Days  
**Source:** `04_crm_opportunities.csv`

---

## 5. Paid AI

### Paid AI CTR

```text
SUM(Clicks) / SUM(Impressions)
```

**Format:** Percent  
**Source:** `05_ai_paid_media.csv`

---

### Paid AI Conversion Rate

```text
SUM(Conversions) / SUM(Clicks)
```

**Format:** Percent  
**Source:** `05_ai_paid_media.csv`

---

### CPA

```text
SUM(Spend_USD) / SUM(Conversions)
```

**Format:** USD

**Interpretation:** Average paid-media cost per attributed conversion.

---

### Pipeline ROAS

```text
SUM(Attributed_Pipeline_USD) / SUM(Spend_USD)
```

**Format:** Decimal / X

Example:

```text
14.5 = 14.5x Pipeline ROAS
```

**Interpretation:** Each $1 of paid AI spend generated $14.50 of attributed pipeline.

Pipeline ROAS is not equivalent to revenue ROAS because pipeline represents potential business value rather than realized revenue.

---

# Metric Hierarchy

The project deliberately separates leading indicators from business outcomes.

```text
AI Visibility
    ↓
Presence / Citations / Accuracy

Buyer Behavior
    ↓
Sessions / Demo CVR

Demand
    ↓
Branded Search

Sales Quality
    ↓
Qualified Opportunities

Business Value
    ↓
Pipeline

Paid Efficiency
    ↓
CPA / Pipeline ROAS
```

---

# Measurement Principle

The project does not treat traffic growth as the final definition of success.

The primary analytical question is:

> Does AI exposure contribute to high-intent buyer behavior and measurable business value?

Therefore, metrics closer to pipeline and qualified demand receive greater business weight than visibility or traffic metrics alone.

---

# Aggregation Principle

For ratio metrics, calculate the ratio from aggregated components whenever possible.

Correct:

```text
SUM(Clicks) / SUM(Impressions)
```

Potentially misleading:

```text
AVG(CTR)
```

This prevents unweighted averages from giving small observations the same influence as large observations.

---

# Attribution Principle

AI influence is measured through multiple signals:

1. identifiable AI referral traffic;
2. branded search behavior;
3. CRM self-reported attribution;
4. qualified opportunity data;
5. attributed pipeline.

These signals should not automatically be added together because they may overlap.

For example, a buyer may:

```text
See NovaFlow in ChatGPT
        ↓
Search "NovaFlow" on Google
        ↓
Visit the website
        ↓
Submit a demo request
        ↓
Report AI as the original discovery source
```

GA4 may classify the session as Organic Search while CRM records AI influence.

This is why the project treats attribution as a multi-signal measurement problem rather than relying solely on last-click attribution.

