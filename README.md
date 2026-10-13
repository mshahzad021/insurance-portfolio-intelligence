# 🛡️ Insurance Portfolio Intelligence & Customer Lifecycle Analytics

An end-to-end insurance analytics project using **Python, SQL, Google
BigQuery, and Power BI** to transform synthetic insurance data into
executive-level business insights.

## 📊 Dashboard Preview

  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Executive Portfolio                                                   Product & Claims Intelligence
  --------------------------------------------------------------------- ----------------------------------------------------------------------------------------
  ![Executive                                                           ![Product & Claims
  Portfolio](dashboard/screenshots/1%20-%20Executive%20Portfolio.png)   Intelligence](dashboard/screenshots/2%20-%20Product%20%26%20Claims%20Intelligence.png)

  --------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------
  Customer & Retention Intelligence                             Commercial & Collections
  ------------------------------------------------------------- ----------------------------------------------------------------
  ![Customer & Retention                                        ![Commercial &
  Intelligence](dashboard/screenshots/customer-retention.png)   Collections](dashboard/screenshots/commercial-collections.png)

  ------------------------------------------------------------------------------------------------------------------------------

## 🎯 Project Overview

The project connects core insurance processes into one analytical view:

**Customers → Leads → Policies → Premiums → Claims → Renewals →
Payments**

It helps stakeholders assess portfolio growth, product performance,
claims risk, customer retention, sales conversion, and premium
collection.

## 🏗️ Workflow & Phases

1.  **Synthetic Data Generation** --- Created connected insurance
    datasets with Python, Pandas, NumPy, and Faker.
2.  **Data Quality & Profiling** --- Checked row counts, data types,
    missing values, duplicate keys, invalid values, and relationship
    consistency.
3.  **BigQuery Data Warehouse** --- Loaded CSV datasets into BigQuery,
    inspected schemas, validated data, and prepared SQL transformations.
4.  **Data Modeling** --- Organized business entities into analytical
    fact/event and dimension structures to support reusable reporting.
5.  **Analytical SQL Layer** --- Built views to centralize KPI logic and
    simplify reporting:
    -   `vw_executive_kpi` --- executive metrics
    -   `vw_monthly_portfolio` --- portfolio trends
    -   `vw_product_performance` --- product analytics
    -   `vw_claims_intelligence` --- claims and risk
    -   `vw_customer_360` --- customer analytics
    -   `vw_renewal_intelligence` --- renewals and retention
    -   `vw_sales_funnel` --- lead conversion
    -   `vw_payment_collection` --- billing and collections
6.  **Power BI Reporting** --- Developed a semantic model, DAX measures,
    and interactive dashboard pages for business analysis.

## 📈 KPI Framework

  -----------------------------------------------------------------------
  Business Area                       Key Performance Indicators
  ----------------------------------- -----------------------------------
  **Executive Portfolio**             Gross Written Premium (GWP), active
                                      policies, total customers, total
                                      claims, claim amount, loss ratio,
                                      renewal rate, lead conversion rate,
                                      collection rate

  **Products**                        GWP by product, active policies,
                                      average premium, product
                                      contribution, premium growth, loss
                                      ratio

  **Claims & Risk**                   Claim count and amount, claim
                                      frequency, claim severity, loss
                                      ratio, claims growth

  **Customers & Retention**           Total and active customers,
                                      policies per customer, premium per
                                      customer, renewal rate, retention
                                      rate, churn rate, at-risk customers

  **Sales Funnel**                    Total and converted leads,
                                      conversion rate, lead-to-policy
                                      conversion, premium by source,
                                      channel performance

  **Payments & Collections**          Total billed, total collected,
                                      outstanding and overdue amounts,
                                      collection rate, failed payment
                                      rate
  -----------------------------------------------------------------------

## 📊 Dashboard Pages

### 1. Executive Portfolio

Provides a high-level view of portfolio health through headline KPIs,
GWP and claims trends, premium-versus-claims analysis, product
contribution, policy status, and top products.

### 2. Product & Claims Intelligence

Compares product contribution and claims pressure using GWP, policy
counts, average premium, loss ratio, claims trends, frequency, severity,
claim status, and high-value claims.

### 3. Customer & Retention Intelligence

Examines customer growth, segmentation, premium and policies per
customer, renewals, retention, churn, at-risk customers, and customer
value.

### 4. Commercial & Collections

Tracks leads, conversion rates, lead sources, sales channels and agent
performance alongside billed premium, collected amounts, outstanding
balances, overdue amounts, and failed payments.

## 🧰 Technology Stack

  Layer                          Tools
  ------------------------------ ------------------------------
  Data generation & processing   Python, Pandas, NumPy, Faker
  Data quality                   Python, SQL
  Data warehouse                 Google BigQuery
  Transformations & metrics      SQL, DAX
  Visualization                  Microsoft Power BI
  Version control                Git, GitHub

## 📁 Repository Structure

``` text
insurance-portfolio-intelligence/
├── data/
│   ├── raw/
│   └── data_dictionary/
├── python/
│   ├── 01_generate_synthetic_data.py
│   └── 02_data_quality_profile.py
├── sql/
│   ├── staging/
│   ├── transformations/
│   └── views/
├── bigquery/
│   ├── schema/
│   ├── data_quality/
│   └── validation/
├── powerbi/
│   ├── Insurance_Analytics.pbix
│   ├── dax/
│   └── model/
├── dashboard/
│   └── screenshots/
├── docs/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Project Status

  Phase                                         Status
  --------------------------------------------- -------------
  Business requirements & synthetic data        Completed
  Data quality profiling & BigQuery ingestion   Completed
  Data modeling & analytical SQL views          Completed
  KPI framework & Power BI data model           Completed
  Executive dashboard & screenshots             Completed
  Final documentation                           In progress

## 💡 Business Value

The dashboard supports analysis of portfolio growth, product
performance, claims exposure, customer retention, sales conversion, and
collection gaps---helping stakeholders identify trends and areas for
further investigation.

## 🛠️ Skills Demonstrated

**Python · SQL · BigQuery · Power BI · DAX · Data Modeling · Data
Quality · ETL · KPI Development · Business Intelligence · Insurance
Analytics · Customer Lifecycle Analytics**

## ⚠️ Disclaimer

This project uses **synthetic data** for demonstration and portfolio
purposes. No real customer, policy, claims, financial, or personally
identifiable information is included.

## 👨‍💻 Author

**Muhammad Shahzad**\
Data Analytics \| Data Engineering \| Business Intelligence
