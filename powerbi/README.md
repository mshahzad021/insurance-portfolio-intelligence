# Power BI Analytics

This folder contains the Microsoft Power BI implementation of the Insurance Portfolio Intelligence & Customer Lifecycle Analytics platform.

Power BI is used as the final semantic modeling and business intelligence layer.

## Dashboard Objective

The Power BI solution converts curated BigQuery analytical views into an interactive executive reporting environment.

The dashboard focuses on:

- Portfolio performance
- Product performance
- Claims intelligence
- Customer lifecycle
- Renewal and retention
- Sales funnel
- Payment and collections
- Executive KPIs

---

## Architecture

```text
Google BigQuery
       │
       ▼
Analytical SQL Views
       │
       ▼
Power BI Semantic Model
       │
       ├── Relationships
       ├── Measures
       ├── Calculated Logic
       └── KPI Framework
       │
       ▼
Executive Dashboard