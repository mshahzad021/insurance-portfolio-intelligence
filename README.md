# 🛡️ Insurance Portfolio Intelligence & Customer Lifecycle Analytics

> **End-to-end insurance analytics platform built with Python, SQL, Google BigQuery and Microsoft Power BI to transform synthetic insurance data into executive-level business intelligence.**

---

## 📊 Project Overview

This project demonstrates an end-to-end **Data Analytics Engineering and Business Intelligence workflow** for an insurance organization.

The objective is to build a centralized analytical solution that enables business stakeholders to understand:

* Insurance portfolio growth
* Premium performance
* Policy and customer trends
* Product performance
* Claims behavior and risk
* Customer retention and renewal
* Sales funnel performance
* Payment and collection performance
* Key executive KPIs

The project starts from **synthetic insurance data generation** and progresses through data quality, cloud data warehousing, analytical modeling, KPI engineering and executive dashboard development.

---

## 🎯 Business Objective

Insurance organizations generate data across multiple business processes including:

**Customers → Leads → Policies → Premiums → Claims → Renewals → Payments**

The goal of this project is to integrate these business processes into a unified analytical layer and provide management with a clear view of portfolio performance.

### Key Business Questions

* How is the insurance portfolio performing?
* Are premiums growing?
* Which products generate the most premium?
* Which products have high claims pressure?
* What is the overall loss ratio?
* Are customers renewing their policies?
* Where are we losing customers?
* Which sales channels generate the highest conversions?
* How much premium has been collected?
* How much remains outstanding?
* Where are the key business risks?

---

# 🏗️ Solution Architecture

```text
                    ┌──────────────────────┐
                    │   Synthetic Data     │
                    │      Generation      │
                    │       Python         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      CSV Files       │
                    │ Customers / Policies │
                    │ Claims / Leads etc.  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Google BigQuery   │
                    │      Data Warehouse  │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ Data Profiling &     │
                    │ Quality Validation   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Analytical SQL Views │
                    │ KPI / Fact / Dim     │
                    │ Business Logic       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Power BI        │
                    │ Semantic Model + DAX │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Executive Dashboard  │
                    │ Decision Intelligence│
                    └──────────────────────┘
```

---

# 🔄 End-to-End Data Analytics Workflow

## Phase 1 — Synthetic Data Generation

Synthetic insurance datasets were generated using **Python** to simulate realistic insurance business processes.

### Technologies

* Python
* Pandas
* NumPy
* Faker
* Randomized business rules

### Data Domains

The synthetic data covers:

* Customers
* Policies
* Products
* Claims
* Leads
* Renewals
* Payments
* Agents / Sales Channels

The data generation process was designed to create realistic relationships between business entities rather than independent random datasets.

---

# Phase 2 — Data Quality & Profiling

Before analytical modeling, the datasets were profiled to identify potential data quality issues.

### Quality Checks

* Row counts
* Column counts
* Primary-key duplicates
* Null values
* Null rates
* Data types
* Referential integrity
* Duplicate records
* Invalid values
* Relationship consistency

### Objective

Ensure that analytical KPIs are based on reliable and validated data.

---

# Phase 3 — Google BigQuery Data Warehouse

The generated CSV files were uploaded into **Google BigQuery**.

BigQuery was used as the centralized analytical data warehouse.

### Activities

* Dataset creation
* Table creation
* CSV ingestion
* Schema inspection
* Data profiling
* Data validation
* Relationship analysis
* SQL transformations
* Analytical view creation

---

# Phase 4 — Data Modeling

The insurance data was organized into analytical fact and dimension structures.

### Core Business Entities

```text
                    DIMENSIONS
                        │
        ┌───────────────┼────────────────┐
        │               │                │
    Customer         Product          Date
        │               │                │
        └───────────────┼────────────────┘
                        │
                        ▼
                  FACT / EVENTS
                        │
        ┌───────────────┼────────────────┐
        │               │                │
      Policy          Claims          Payments
        │
      Leads
        │
     Renewals
```

The model was designed to support reusable KPI calculations and analytical slicing across time, product, customer and business processes.

---

# Phase 5 — Analytical SQL Layer

Business logic was centralized in BigQuery analytical views.

### Analytical Views

| View                      | Purpose                       |
| ------------------------- | ----------------------------- |
| `vw_executive_kpi`        | Executive-level KPIs          |
| `vw_monthly_portfolio`    | Portfolio trends              |
| `vw_product_performance`  | Product analytics             |
| `vw_claims_intelligence`  | Claims and risk analytics     |
| `vw_customer_360`         | Customer analytics            |
| `vw_renewal_intelligence` | Renewal and retention         |
| `vw_sales_funnel`         | Lead and conversion analytics |
| `vw_payment_collection`   | Billing and collection        |

This approach keeps business logic centralized and makes the Power BI layer cleaner and more maintainable.

---

# 📈 KPI Framework

The dashboard focuses on a controlled set of business KPIs rather than displaying excessive metrics.

## Executive KPIs

* Gross Written Premium
* Active Policies
* Total Customers
* Total Claims
* Total Claim Amount
* Loss Ratio
* Renewal Rate
* Lead Conversion Rate
* Collection Rate

## Product KPIs

* GWP
* Active Policies
* Average Premium
* Product Contribution
* Premium Growth
* Loss Ratio

## Claims KPIs

* Claim Count
* Claim Amount
* Claim Frequency
* Claim Severity
* Loss Ratio
* Claims Growth

## Customer KPIs

* Total Customers
* Active Customers
* Policies per Customer
* Premium per Customer
* Renewal Rate
* Retention Rate
* Churn Rate
* At-Risk Customers

## Sales KPIs

* Total Leads
* Converted Leads
* Conversion Rate
* Lead-to-Policy Conversion
* Premium by Source
* Best Performing Channel

## Collection KPIs

* Total Billed
* Total Collected
* Outstanding Amount
* Overdue Amount
* Collection Rate
* Failed Payment Rate

---

# 📊 Power BI Dashboard

The final analytics solution is being developed in **Microsoft Power BI**.

The dashboard is designed as an executive decision-support solution with four analytical pages.

---

## 1️⃣ Executive Portfolio

### Purpose

Provide management with a high-level view of insurance portfolio performance.

### KPIs

* GWP
* Active Policies
* Customers
* Claims
* Claim Amount
* Loss Ratio
* Renewal Rate
* Lead Conversion Rate
* Collection Rate

### Analysis

* GWP trend
* Claims trend
* Premium vs Claims
* Product contribution
* Policy status
* Top products
* KPI performance

---

## 2️⃣ Product & Claims Intelligence

### Purpose

Identify high-performing products and products generating excessive claims pressure.

### Analysis

* GWP by product
* Policies by product
* Average premium
* Loss ratio
* Claims trend
* Claim frequency
* Claim severity
* Claims by status
* High-value claims

### Strategic Analysis

**Premium × Claims Risk Matrix**

```text
                  CLAIM PRESSURE
                 Low          High

HIGH        Core Business    Risky Growth
PREMIUM

LOW         Stable           Review
PREMIUM
```

---

## 3️⃣ Customer & Retention Intelligence

### Purpose

Understand customer value, retention and churn.

### Analysis

* Customer growth
* Customer segmentation
* Policies per customer
* Premium per customer
* Renewal rate
* Retention rate
* Churn rate
* At-risk customers
* Customer value analysis

### Strategic Framework

```text
                CUSTOMER RISK

              Low              High

HIGH      PROTECT            RETAIN
VALUE

LOW       GROW               REVIEW
VALUE
```

---

## 4️⃣ Commercial & Collections

### Purpose

Connect sales performance with revenue realization.

### Sales Funnel

```text
Leads
  ↓
Qualified Leads
  ↓
Converted Leads
  ↓
Policies
  ↓
Premium
```

### Sales Analysis

* Leads trend
* Conversion rate
* Lead source
* Premium by source
* Channel performance
* Agent performance

### Collection Analysis

```text
Premium
   ↓
Billing
   ↓
Collection
   ↓
Outstanding
   ↓
Overdue
```

### Collection KPIs

* Total Billed
* Total Collected
* Outstanding
* Overdue
* Collection Rate
* Failed Payments

---

# 🧠 Analytics & Engineering Skills Demonstrated

This project demonstrates the following capabilities:

### Data Engineering

* Synthetic data generation
* Data ingestion
* Data validation
* Data profiling
* Data warehousing
* BigQuery
* SQL transformations
* Analytical views

### Data Analytics

* KPI design
* Business metric definition
* Trend analysis
* Customer analytics
* Product analytics
* Claims analytics
* Retention analysis
* Sales funnel analysis
* Collection analytics

### BI & Visualization

* Power BI
* Data modeling
* DAX
* KPI cards
* Executive dashboards
* Interactive filtering
* Drill-down analysis
* Business storytelling

### Data Quality

* Duplicate detection
* Null analysis
* Primary-key validation
* Referential integrity
* Data consistency checks
* Data quality profiling

### Business Intelligence

* Executive reporting
* Insurance portfolio analytics
* Risk analysis
* Customer lifecycle analytics
* Revenue intelligence
* Decision-support analytics

---

# 🛠️ Technology Stack

| Layer           | Technology         |
| --------------- | ------------------ |
| Data Generation | Python             |
| Data Processing | Pandas / NumPy     |
| Data Quality    | Python / SQL       |
| Data Warehouse  | Google BigQuery    |
| Transformation  | SQL                |
| Analytics       | SQL / DAX          |
| Visualization   | Microsoft Power BI |
| Version Control | Git / GitHub       |

---

# 📁 Repository Structure

```text
insurance-portfolio-intelligence/
│
├── data/
│   ├── raw/
│   └── data_dictionary/
│
├── python/
│   ├── 01_generate_synthetic_data.py
│   └── 02_data_quality_profile.py
│
├── sql/
│   ├── staging/
│   ├── transformations/
│   └── views/
│
├── bigquery/
│   ├── schema/
│   ├── data_quality/
│   └── validation/
│
├── powerbi/
│   ├── Insurance_Analytics.pbix
│   ├── dax/
│   └── model/
│
├── dashboard/
│   └── screenshots/
│
├── docs/
│   ├── project_overview.md
│   ├── business_requirements.md
│   ├── data_architecture.md
│   ├── data_model.md
│   ├── kpi_framework.md
│   ├── data_quality.md
│   └── dashboard_guide.md
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🚀 Project Status

| Phase                     | Status         |
| ------------------------- | -------------- |
| Business Requirements     | ✅ Completed    |
| Synthetic Data Generation | ✅ Completed    |
| Data Quality Profiling    | ✅ Completed    |
| CSV Data Generation       | ✅ Completed    |
| BigQuery Ingestion        | ✅ Completed    |
| BigQuery Inspection       | ✅ Completed    |
| Data Modeling             | ✅ Completed    |
| Analytical SQL Views      | ✅ Completed    |
| KPI Framework             | ✅ Completed    |
| Power BI Data Model       | ✅ Completed    |
| Executive Dashboard       | 🔄 In Progress |
| Dashboard Screenshots     | ⏳ Pending      |
| Final Documentation       | ⏳ Pending      |

---

# 📸 Dashboard Preview

> Dashboard screenshots will be added after completion.

### Executive Portfolio

`dashboard/screenshots/executive-portfolio.png`

### Product & Claims Intelligence

`dashboard/screenshots/product-claims.png`

### Customer & Retention Intelligence

`dashboard/screenshots/customer-retention.png`

### Commercial & Collections

`dashboard/screenshots/commercial-collections.png`

---

# 🔍 Key Business Insights

The completed dashboard will enable management to identify:

* Portfolio growth opportunities
* Underperforming insurance products
* High-loss products
* Claims pressure
* Customer retention risks
* High-value customer segments
* Sales channel performance
* Conversion bottlenecks
* Collection gaps
* Outstanding and overdue premium

---

# 🎯 Project Outcome

This project demonstrates an end-to-end approach to transforming raw insurance data into actionable business intelligence.

The solution connects:

**Data → Quality → Warehouse → Modeling → KPIs → Analytics → Visualization → Business Decisions**

Rather than producing a standalone dashboard, the project establishes a reusable analytics architecture that can support future insurance reporting and analytical use cases.

---

# 👨‍💻 Skills Demonstrated

**Python | SQL | BigQuery | Power BI | DAX | Data Modeling | Data Quality | ETL | Business Intelligence | KPI Engineering | Insurance Analytics | Customer Analytics | Claims Analytics | Sales Analytics | Data Visualization | Git | GitHub**

---

## Disclaimer

This project uses **synthetic data** created for demonstration and portfolio purposes.

No real customer, policy, claims, financial or personally identifiable information is included.

---

## Author

**Muhammad Shahzad**

Data Analytics | Data Engineering | Business Intelligence

---
