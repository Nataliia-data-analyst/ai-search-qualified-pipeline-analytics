# Data

This directory contains the synthetic datasets used in the **AI Search → Qualified Pipeline Analytics** portfolio project.

> All data in this repository is fictional and created for educational and portfolio purposes. It does not represent real customers, campaigns, companies, or financial results.

## Data Flow

```text
Synthetic Source Data
        ↓
      raw/
        ↓
Data Preparation & Aggregation
        ↓
   processed/
        ↓
   Looker Studio
        ↓
Metric Validation
        ↓
Business Analysis
```

## Raw Data

### `01_ai_presence.csv`

AI search monitoring dataset used to measure:

- brand presence;
- linked citations;
- answer accuracy;
- performance by AI assistant;
- performance by buyer-intent prompt;
- changes over time.

### `02_ga4_traffic.csv`

GA4-style acquisition dataset used to analyze:

- sessions;
- traffic source;
- demo requests;
- conversion rates;
- qualified opportunities;
- AI referral performance vs other channels.

### `03_gsc_branded.csv`

Google Search Console-style dataset used to analyze:

- branded impressions;
- branded clicks;
- branded CTR;
- branded demand trends.

### `04_crm_opportunities.csv`

CRM-style opportunity dataset used to analyze:

- self-reported attribution;
- opportunity qualification;
- pipeline value;
- AI-influenced opportunities;
- source performance.

### `05_ai_paid_media.csv`

Paid AI advertising dataset used to analyze:

- spend;
- impressions;
- clicks;
- conversions;
- CTR;
- conversion rate;
- CPA;
- attributed pipeline;
- Pipeline ROAS.

## Processed Data

### `06_weekly_kpis.csv`

Weekly aggregated KPI layer used for cross-channel trend analysis.

It supports comparisons between metrics such as AI visibility and branded search demand without creating unsafe many-to-many joins between raw datasets.

### `09_paid_ai_funnel.csv`

Aggregated dataset used to visualize the paid AI funnel:

```text
Impressions
    ↓
Clicks
    ↓
Conversions
```

## Data Modeling Principle

Raw datasets are kept separate from transformed and aggregated datasets.

This makes the analytical flow easier to validate and helps prevent issues such as:

- double aggregation;
- incorrect joins;
- duplicated records;
- averages of already aggregated percentages;
- inconsistent date grains.

Ratio metrics such as CTR, CVR, CPA and ROAS are calculated from their underlying components whenever possible rather than averaging pre-calculated ratios.
