# SQL Analytics Layer

This folder contains the analytical SQL views developed in Google BigQuery.

The SQL layer centralizes business logic and prepares reusable datasets for Power BI.

## Analytical Views

### Executive Analytics

- `vw_executive_kpi.sql`

Provides high-level portfolio KPIs for executive reporting.

### Portfolio Analytics

- `vw_monthly_portfolio.sql`

Provides monthly portfolio performance and trend analysis.

### Product Analytics

- `vw_product_performance.sql`

Provides product-level premium, policy and performance metrics.

### Claims Analytics

- `vw_claims_intelligence.sql`

Provides claims volume, claim amount, frequency, severity and loss-ratio analysis.

### Customer Analytics

- `vw_customer_360.sql`

Provides a consolidated customer-level analytical view.

### Renewal Analytics

- `vw_renewal_intelligence.sql`

Provides renewal, retention and customer lifecycle metrics.

### Sales Analytics

- `vw_sales_funnel.sql`

Provides lead, conversion and sales funnel analytics.

### Payment Analytics

- `vw_payment_collection.sql`

Provides billing, payment, outstanding, overdue and collection metrics.

## Purpose

The analytical SQL layer separates business logic from the visualization layer and provides reusable datasets for Power BI.

BigQuery acts as the central analytical warehouse, while Power BI consumes the curated analytical views for reporting and visualization.