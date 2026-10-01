# Data Model & Analytics Architecture

This document describes how data flows through the **AI Search → Qualified Pipeline Analytics** project and why the datasets are intentionally kept at different grains.

---

## 1. Analytics Architecture

```text
                         AI SEARCH
                             │
              ┌──────────────┴──────────────┐
              │                             │
         ORGANIC AI                     PAID AI
              │                             │
      AI Presence Data              Paid Media Data
              │                             │
      Mentions / Citations          Impressions / Clicks
      Answer Accuracy               Spend / Conversions
              │                             │
              └──────────────┬──────────────┘
                             │
                             ▼
                          WEBSITE
                             │
                             ▼
                         GA4 TRAFFIC
                             │
                  Sessions / Demo Requests
                             │
                             ▼
                    QUALIFIED OPPORTUNITY
                             │
                             ▼
                            CRM
                             │
                 Pipeline / Won / Sales Cycle
                             │
                             ▼
                      BUSINESS VALUE


        Supporting demand signal:

        AI Visibility
             │
             ▼
       Branded Search
             │
             ▼
       GSC Impressions
       GSC Clicks / CTR
```

---

## 2. Source Layers

The project uses five primary analytical sources.

| Source | Grain | Main Purpose |
|---|---|---|
| AI Presence | Week × Prompt × Assistant | AI visibility and answer quality |
| GA4 Traffic | Week × Channel × Source | Website acquisition and conversion |
| GSC Branded Search | Week × Query Type | Branded demand |
| CRM Opportunities | Opportunity | Sales quality and pipeline |
| AI Paid Media | Week × Platform | Paid AI efficiency |

These datasets should not be directly joined at their raw grain.

---

## 3. Why Raw Tables Are Not Directly Joined

The datasets have different levels of granularity.

Example:

```text
AI Presence
Week × Prompt × Assistant

GA4
Week × Channel × Source

GSC
Week × Query Type

CRM
Opportunity

Paid AI
Week × Platform
```

Joining these raw tables only on `Week` could create many-to-many relationships.

Example:

```text
20 AI Presence rows
        ×
5 GA4 rows
        =
100 joined rows
```

This can duplicate metrics such as:

- sessions;
- impressions;
- clicks;
- pipeline;
- spend.

The resulting dashboard may look valid while reporting inflated totals.

---

## 4. Aggregation Layer

For cross-source trend analysis, data is first aggregated to a common weekly grain.

```text
RAW SOURCES
     │
     ├── AI Presence
     ├── GA4
     ├── GSC
     ├── CRM
     └── Paid AI
     │
     ▼
WEEKLY AGGREGATION
     │
     ▼
06_weekly_kpis.csv
     │
     ▼
Cross-source Analysis
```

This layer allows metrics from different systems to be compared without directly joining incompatible raw grains.

---

## 5. Paid AI Funnel Layer

Paid media also has a dedicated processed layer:

```text
05_ai_paid_media.csv
        │
        ▼
Aggregation
        │
        ▼
09_paid_ai_funnel.csv
        │
        ├── Impressions
        ├── Clicks
        └── Conversions
```

This dataset is used specifically for funnel visualization.

It should not replace the detailed paid-media source used for platform, time and efficiency analysis.

---

## 6. Looker Studio Model

The dashboard primarily uses separate data sources rather than one large blended table.

```text
                    LOOKER STUDIO
                         │
        ┌────────────────┼────────────────┐
        │                │                │
 AI Presence          GA4/GSC            CRM
        │                │                │
 Visibility          Acquisition       Pipeline
        │                │                │
        └────────────────┼────────────────┘
                         │
                    Paid AI
                         │
                   Efficiency
```

Each dashboard page uses the source appropriate for its analytical question.

This reduces unnecessary joins and makes metric validation easier.

---

## 7. Dashboard-to-Source Mapping

| Dashboard Page | Primary Source |
|---|---|
| Executive Overview | Multiple validated KPI sources |
| AI Search Visibility | `01_ai_presence.csv` |
| Buyer Behavior & Acquisition | `02_ga4_traffic.csv` |
| Branded Search Impact | `03_gsc_branded.csv` |
| Pipeline & Attribution | `04_crm_opportunities.csv` |
| Paid AI Performance | `05_ai_paid_media.csv` + `09_paid_ai_funnel.csv` |
| Insights & Recommendations | Validated outputs from all analytical layers |

---

## 8. Attribution Model

AI influence cannot be represented reliably by one attribution field.

A possible customer journey:

```text
AI exposure
     ↓
Buyer learns about NovaFlow
     ↓
Google branded search
     ↓
Website
     ↓
Demo request
     ↓
Qualified opportunity
     ↓
CRM pipeline
```

In this example:

GA4 may report:

```text
google / organic
```

while CRM self-reported attribution may report:

```text
ChatGPT or another AI assistant
```

Both observations can be correct.

Therefore, the project uses a multi-signal attribution framework.

---

## 9. Attribution Signals

### Signal 1 — AI Presence

Measures whether the brand appears during AI-assisted vendor research.

### Signal 2 — AI Referral Traffic

Measures identifiable sessions arriving directly from AI assistants.

### Signal 3 — Branded Search

Acts as a supporting demand signal after potential AI exposure.

### Signal 4 — Self-Reported Attribution

Captures buyers who remember discovering the company through AI.

### Signal 5 — CRM Pipeline

Measures whether AI-influenced buyers progress into meaningful sales opportunities.

These signals are analyzed together but are not automatically summed because the same buyer may appear in multiple measurement systems.

---

## 10. Data Lineage

```text
Synthetic Data Generation
          ↓
Google Sheets
          ↓
CSV Export
          ↓
Raw Data
          ↓
Data Quality Validation
          ↓
Processed / Aggregated Layers
          ↓
Looker Studio
          ↓
Metric Reconciliation
          ↓
Analysis
          ↓
Business Insights
          ↓
Recommendations
```

---

## 11. Design Principles

The data model follows several principles:

1. Preserve raw data at its original grain.
2. Separate raw and processed datasets.
3. Avoid many-to-many joins where possible.
4. Aggregate before cross-source comparison.
5. Recalculate ratio metrics from their components.
6. Validate dashboard totals against source data.
7. Treat attribution as multi-signal rather than purely last-click.
8. Keep business definitions documented and reproducible.

---

## 12. Production Architecture — Future State

For a production implementation, the architecture could evolve to:

```text
AI Monitoring APIs ─┐
GA4 → BigQuery ─────┤
GSC API ────────────┤
CRM ────────────────┼──► BigQuery
Paid Platforms ─────┘        │
                             ▼
                      Transformation Layer
                             │
                             ▼
                       Analytics Mart
                             │
                             ▼
                        Looker Studio
```

This would improve automation, scalability, historical storage, governance and reproducibility.

