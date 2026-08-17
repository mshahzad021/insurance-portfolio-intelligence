# Python Scripts

This folder contains the Python scripts used to generate and validate the synthetic insurance datasets.

## Data Generation

The following scripts generate the individual business datasets:

- `generate_customers.py` — Generates synthetic customer records
- `product_master.py` — Creates the insurance product master
- `generate_policies.py` — Generates policy records
- `generate_claims.py` — Generates insurance claims
- `generate_payments.py` — Generates payment transactions
- `generate_leads.py` — Generates sales lead records
- `generate_renewals.py` — Generates policy renewal records
- `generate_interactions.py` — Generates customer interaction records

## Analytics Build

- `build_analytics.py` — Builds the analytical datasets from the generated source data.

## Data Quality

- `data_quality_check.py` — Performs data quality validation and generates the data quality profile.

## Documentation

- `docs/KPI_Dictionary.md` — Documents the business KPIs and metric definitions used in the analytics solution.

## Workflow

Python scripts were used to:

1. Generate synthetic insurance data
2. Establish relationships between business entities
3. Build analytical datasets
4. Validate data quality
5. Produce datasets for BigQuery ingestion
