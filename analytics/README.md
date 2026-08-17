# Analytics Data

This folder contains the analytical datasets generated for the Insurance Portfolio Intelligence project.

The data model follows a dimensional modeling approach using fact and dimension tables.

## Dimension Tables

- `dim_customer.csv` — Customer master data
- `dim_product.csv` — Insurance product master data

## Fact Tables

- `fact_policy.csv` — Insurance policy transactions
- `fact_claim.csv` — Insurance claims
- `fact_payment.csv` — Premium billing and payment transactions
- `fact_lead.csv` — Sales leads and conversion activity
- `fact_renewal.csv` — Policy renewal activity
- `fact_interaction.csv` — Customer interactions

## Data Quality

- `data_quality_profile.csv` — Data quality profiling results including row counts, column counts, duplicate primary keys, null cells, null rates and quality status.

## Purpose

These datasets were initially generated using Python and subsequently loaded into Google BigQuery for validation, modeling and analytical SQL development.

The datasets contain synthetic data for demonstration purposes only.