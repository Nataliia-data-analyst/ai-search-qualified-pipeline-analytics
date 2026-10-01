# Looker Studio Dashboard Documentation

## Dashboard

**AI Search → Qualified Pipeline Analytics**

The dashboard evaluates AI Search across the full buyer journey:

**AI Visibility → Buyer Behavior → Branded Demand → Opportunities → Pipeline → Paid AI Efficiency**

The dashboard is designed for marketing and growth teams that need to understand whether AI visibility creates measurable business value rather than visibility alone.

---

# 00 — Executive Overview

## Purpose

Provide management with a concise view of AI Search performance and its contribution to demand and pipeline.

## Business Question

> Is AI Search reaching potential buyers and contributing to measurable business outcomes?

## Key KPIs

- Brand Presence Rate
- Answer Accuracy Rate
- AI Referral Conversion Rate
- AI-influenced Pipeline
- Branded Search Growth
- Paid AI Pipeline ROAS

## Interpretation

This page summarizes the complete measurement framework.

It should answer three questions quickly:

1. Are we visible in AI?
2. Are AI-influenced buyers demonstrating intent?
3. Is that activity translating into business value?

---

# 01 — AI Search Visibility

## Purpose

Measure NovaFlow's visibility and representation across high-intent AI buyer prompts.

## Primary Source

`data/raw/01_ai_presence.csv`

## Business Questions

- How often is NovaFlow mentioned?
- How often is the company cited?
- Are AI descriptions accurate?
- Which assistants provide the strongest visibility?
- Which buyer prompts have weak coverage?

## KPIs

- Brand Presence Rate
- Citation Rate
- Answer Accuracy Rate
- Number of prompts tested

## Dimensions

- Week
- Assistant
- Buyer Prompt
- Intent

## Analysis

Performance is evaluated by AI assistant, prompt and time.

Presence alone is not considered sufficient: a brand mention may provide little business value if the description is inaccurate or the company is positioned incorrectly.

---

# 02 — Buyer Behavior & Acquisition

## Purpose

Evaluate whether identifiable AI referral traffic demonstrates stronger buyer intent than traditional acquisition channels.

## Primary Source

`data/raw/02_ga4_traffic.csv`

## Business Questions

- How much identifiable traffic comes from AI assistants?
- Does AI traffic generate demo requests?
- How does AI referral conversion compare with Organic and Direct?
- Does AI traffic create qualified opportunities?

## KPIs

- Sessions
- Demo Requests
- Demo Conversion Rate
- Qualified Opportunities
- Qualified Opportunity Rate
- Pipeline Value
- Pipeline per Session

## Main Comparison

**AI Referral vs Organic Search vs Direct**

## Interpretation

Traffic volume and traffic quality are evaluated separately.

A small channel with a high conversion rate should not automatically be considered more valuable without considering sample size and pipeline contribution.

---

# 03 — Branded Search Impact

## Purpose

Use branded search as a supporting demand signal that may capture AI influence not visible through referral attribution.

## Primary Source

`data/raw/03_gsc_branded.csv`

## Business Questions

- Is branded search demand increasing?
- Do branded impressions change alongside AI visibility?
- Are branded clicks increasing?
- Is search demand sustained over time?

## KPIs

- Branded Impressions
- Branded Clicks
- Weighted CTR

## Key Visualizations

- Branded Impressions Over Time
- Branded CTR Over Time
- First-period vs last-period comparison

## Interpretation

An increase in branded search following higher AI visibility may indicate an association between AI exposure and brand demand.

However:

> Correlation does not establish causation.

Other marketing activity, PR, seasonality or product changes may also affect branded demand.

---

# 04 — Pipeline & Attribution

## Purpose

Evaluate whether AI-influenced buyers progress into meaningful sales opportunities.

## Primary Source

`data/raw/04_crm_opportunities.csv`

## Business Questions

- How many opportunities report AI as a discovery source?
- How many become qualified?
- What pipeline value do they represent?
- How does self-reported attribution complement digital tracking?

## KPIs

- Opportunities
- Qualified Opportunities
- Qualification Rate
- Opportunity Value
- Win Rate
- Average Sales Cycle

## Attribution Framework

The project compares:

**Tracked attribution**

with

**Self-reported attribution**

rather than assuming that one source provides complete attribution.

## Important Limitation

Self-reported attribution reflects buyer memory and should not be interpreted as exact causal attribution.

It is used as an additional signal alongside GA4, branded search and CRM outcomes.

---

# 05 — Paid AI Performance

## Purpose

Evaluate the efficiency and business contribution of paid AI advertising.

## Primary Sources

`data/raw/05_ai_paid_media.csv`

and

`data/processed/09_paid_ai_funnel.csv`

## Business Questions

- Which paid AI platform drives the strongest efficiency?
- How much does each conversion cost?
- Which platform generates the most attributed pipeline?
- Does additional paid AI investment appear justified?

## KPIs

- Impressions
- Clicks
- Spend
- CTR
- Conversions
- Conversion Rate
- CPA
- Attributed Pipeline
- Pipeline ROAS

## Funnel

```text
Impressions
    ↓
Clicks
    ↓
Conversions
```

## Platform Comparison

Platforms are evaluated using both acquisition and business metrics.

A platform should not be selected solely because it produces the cheapest clicks.

The analysis prioritizes:

**CPA + Conversion Volume + Attributed Pipeline + Pipeline ROAS**

## Important Definition

Pipeline ROAS:

```text
Attributed Pipeline / Spend
```

Pipeline ROAS measures potential pipeline value generated per dollar of advertising spend.

It is not realized revenue ROAS.

---

# 06 — Insights & Recommendations

## Purpose

Translate dashboard metrics into business decisions.

This page intentionally contains fewer visualizations.

Its role is to answer:

> So what should the business do next?

## Insight Structure

Each finding follows:

```text
Observation
    ↓
Business Meaning
    ↓
Risk / Limitation
    ↓
Recommendation
```

Example:

```text
Observation:
AI Referral CVR exceeds Organic Search CVR.

Business Meaning:
AI visitors may arrive later in the consideration journey.

Limitation:
AI referral volume is smaller.

Recommendation:
Track qualified pipeline per AI session before increasing investment.
```

---

# Dashboard Filters

Depending on the page, the dashboard uses controls such as:

- Date / Week
- AI Assistant
- Channel Group
- Session Source
- Query Type
- CRM Source
- Paid AI Platform

Filters are intentionally page-specific because the underlying datasets have different grains and dimensions.

---

# Dashboard Design Principles

The dashboard follows several design principles:

1. Business questions before visualizations.
2. Limited KPI cards per page.
3. Consistent metric definitions.
4. Ratio-of-sums for aggregated rate metrics.
5. Clear separation between visibility, demand and revenue metrics.
6. Consistent formatting for percentages and currency.
7. Minimal visual clutter.
8. Business interpretation alongside reporting.
9. Page-specific sources instead of unnecessary raw-data blending.
10. Validation against source data before drawing conclusions.

---

# Intended Users

The dashboard is designed primarily for:

- Marketing leadership
- Growth teams
- Digital analysts
- SEO / AI Search teams
- Performance marketing teams
- Revenue / demand generation teams

---

# Decision Framework

The dashboard supports decisions such as:

### AI Search Strategy
Should the company invest further in improving AI visibility?

### Content Strategy
Which high-intent buyer prompts require better coverage?

### Attribution
Is AI influence being missed by conventional referral tracking?

### Demand Generation
Is increased AI presence accompanied by stronger branded demand?

### Paid Media
Which AI advertising platforms justify additional budget?

### Measurement
Which metrics should be monitored before scaling investment?

