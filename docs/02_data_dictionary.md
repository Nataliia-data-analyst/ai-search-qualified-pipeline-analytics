# Data Dictionary

This document describes the core datasets used in the **AI Search → Qualified Pipeline Analytics** project.

All datasets are synthetic and were created for portfolio and analytical demonstration purposes.

---

# 1. AI Presence

**File:** `data/raw/01_ai_presence.csv`

**Grain:** One row represents one AI assistant response to one buyer prompt during one observation week.

| Field | Type | Description | Aggregation / Role |
|---|---|---|---|
| Week | Date | Observation week | Dimension |
| Prompt_ID | Text | Unique identifier of the tested buyer prompt | Dimension |
| Buyer_Prompt | Text | High-intent buyer question submitted to an AI assistant | Dimension |
| Intent | Text | Buyer-intent category of the prompt | Dimension |
| Assistant | Text | AI assistant used for the test | Dimension |
| Brand | Text | Brand being evaluated | Dimension |
| Mentioned | Boolean / 0-1 | Indicates whether the brand appeared in the AI response | SUM for mentions |
| Linked_Citation | Boolean / 0-1 | Indicates whether the response contained a linked citation to the brand | SUM for citations |
| Accurate | Boolean / 0-1 | Indicates whether the brand description was accurate | SUM for accurate answers |
| Position | Number | Brand position/order within the AI response when applicable | AVG / analytical dimension |
| Competitors_Named | Text | Competitors mentioned in the same AI response | Dimension |
| Notes | Text | Additional observation or QA notes | Dimension |

## Core Metrics

**Brand Presence Rate**

```text
SUM(Mentioned) / COUNT(Mentioned)
```

**Citation Rate**

```text
SUM(Linked_Citation) / COUNT(Linked_Citation)
```

**Answer Accuracy Rate**

For answers where the brand was mentioned:

```text
SUM(Accurate) / SUM(Mentioned)
```

> Accuracy should be interpreted only for responses in which the brand appears.

---

# 2. GA4 Traffic

**File:** `data/raw/02_ga4_traffic.csv`

**Grain:** One row represents weekly acquisition performance for one channel/source combination.

| Field | Type | Description | Aggregation / Role |
|---|---|---|---|
| Week | Date | Reporting week | Dimension |
| Channel_Group | Text | Marketing acquisition channel | Dimension |
| Session_Source | Text | Session-level traffic source | Dimension |
| Sessions | Integer | Number of website sessions | SUM |
| Demo_Requests | Integer | Number of submitted demo requests | SUM |
| Qualified_Opps | Integer | Number of qualified opportunities attributed to the traffic segment | SUM |
| Pipeline_Value_USD | Currency | Pipeline value attributed to the segment | SUM |

## Core Metrics

**Demo Conversion Rate**

```text
SUM(Demo_Requests) / SUM(Sessions)
```

**Session → Qualified Opportunity Rate**

```text
SUM(Qualified_Opps) / SUM(Sessions)
```

**Pipeline per Session**

```text
SUM(Pipeline_Value_USD) / SUM(Sessions)
```

---

# 3. GSC Branded Search

**File:** `data/raw/03_gsc_branded.csv`

**Grain:** One row represents weekly Google Search performance for a query category.

| Field | Type | Description | Aggregation / Role |
|---|---|---|---|
| Week | Date | Reporting week | Dimension |
| Query_Type | Text | Search query classification | Dimension |
| Impressions | Integer | Number of search-result impressions | SUM |
| Clicks | Integer | Number of search-result clicks | SUM |
| CTR | Percent | Click-through rate stored in the source | Do not SUM |

## Core Metric

**Weighted CTR**

```text
SUM(Clicks) / SUM(Impressions)
```

> For aggregated reporting, CTR should be recalculated from clicks and impressions rather than using `AVG(CTR)`.

---

# 4. CRM Opportunities

**File:** `data/raw/04_crm_opportunities.csv`

**Grain:** One row represents one sales opportunity.

| Field | Type | Description | Aggregation / Role |
|---|---|---|---|
| Opportunity_ID | Text | Unique opportunity identifier | COUNT DISTINCT |
| Created_Date | Date | Date the opportunity was created | Dimension |
| Self_Reported_Source | Text | Source reported by the buyer | Dimension |
| Qualified | Boolean / 0-1 | Indicates whether the opportunity was qualified | SUM |
| Stage | Text | Current/final sales stage | Dimension |
| Opportunity_Value_USD | Currency | Monetary value associated with the opportunity | SUM |
| Sales_Cycle_Days | Integer | Number of days in the sales cycle | AVG / Median |
| Won | Boolean / 0-1 | Indicates whether the opportunity was closed won | SUM |

## Core Metrics

**Qualification Rate**

```text
SUM(Qualified) / COUNT_DISTINCT(Opportunity_ID)
```

**Win Rate**

```text
SUM(Won) / COUNT_DISTINCT(Opportunity_ID)
```

**Average Opportunity Value**

```text
SUM(Opportunity_Value_USD) / COUNT_DISTINCT(Opportunity_ID)
```

## Known Synthetic Data Issue

The current synthetic dataset contains an unrealistically high qualification rate for the `AI self-reported` segment.

This is a source-data characteristic rather than a Looker Studio calculation error and will be adjusted during the final data QA stage.

---

# 5. AI Paid Media

**File:** `data/raw/05_ai_paid_media.csv`

**Grain:** One row represents one AI advertising platform for one reporting week.

| Field | Type | Description | Aggregation / Role |
|---|---|---|---|
| Week | Date | Reporting week | Dimension |
| Platform | Text | Paid AI advertising platform | Dimension |
| Impressions | Integer | Number of paid impressions | SUM |
| Clicks | Integer | Number of paid clicks | SUM |
| Spend_USD | Currency | Advertising spend | SUM |
| Conversions | Integer | Number of attributed conversions | SUM |
| Attributed_Pipeline_USD | Currency | Pipeline value attributed to paid AI activity | SUM |

## Core Metrics

**CTR**

```text
SUM(Clicks) / SUM(Impressions)
```

**Conversion Rate**

```text
SUM(Conversions) / SUM(Clicks)
```

**CPA**

```text
SUM(Spend_USD) / SUM(Conversions)
```

**Pipeline ROAS**

```text
SUM(Attributed_Pipeline_USD) / SUM(Spend_USD)
```

> Pipeline ROAS represents attributed pipeline value per dollar of advertising spend. It should not be interpreted as realized revenue ROAS.

---

# Aggregation Rules

Ratio metrics should generally be calculated from their underlying components.

## Correct

```text
CTR = SUM(Clicks) / SUM(Impressions)

CVR = SUM(Conversions) / SUM(Clicks)

CPA = SUM(Spend_USD) / SUM(Conversions)

Pipeline ROAS =
SUM(Attributed_Pipeline_USD) / SUM(Spend_USD)
```

## Avoid

```text
AVG(CTR)
AVG(CVR)
AVG(CPA)
AVG(ROAS)
```

when analyzing aggregated groups or longer reporting periods.

This prevents the common **average-of-averages** problem.

---

# Data Quality Rules

Before dashboard reporting, validate:

- date fields use consistent date types;
- numeric fields are not stored as text;
- currency symbols do not convert numeric fields into strings;
- identifiers remain unique where required;
- no unintended duplicate records exist;
- calculated ratios use the correct denominator;
- raw and aggregated datasets are not mixed without controlling grain;
- null values are reviewed before aggregation;
- source totals reconcile with Looker Studio totals.

