import pandas as pd
import numpy as np
import os

# ============================================================
# UAE INSURANCE LEAD GENERATOR
# ============================================================

SEED = 42
np.random.seed(SEED)

TODAY = pd.Timestamp("2026-08-15")

# ============================================================
# DIRECTORIES
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

# ============================================================
# LOAD CUSTOMERS
# ============================================================

customers = pd.read_csv(
    os.path.join(
        DATA_DIR,
        "customers.csv"
    )
)

# ============================================================
# LEAD SOURCES
# ============================================================

lead_sources = [
    "Google Ads",
    "Social Media",
    "Website",
    "Insurance Broker",
    "Referral",
    "Bank Partner",
    "Email Campaign",
    "Branch"
]

lead_source_weights = [
    0.16,
    0.12,
    0.18,
    0.18,
    0.10,
    0.10,
    0.08,
    0.08
]

products = [
    "Car Insurance",
    "Health Insurance",
    "Life Insurance",
    "Home Insurance",
    "Travel Insurance",
    "Business Insurance",
    "SME Insurance",
    "Cyber Security Insurance",
    "Motor Fleet Insurance"
]

lead_statuses = [
    "New",
    "Contacted",
    "Qualified",
    "Quoted",
    "Converted",
    "Lost"
]

# ============================================================
# GENERATE
# ============================================================

leads = []

lead_counter = 1

# Generate approximately 1.5 leads per customer
n_leads = int(
    len(customers) * 1.5
)

for _ in range(n_leads):

    customer = customers.iloc[
        np.random.randint(
            0,
            len(customers)
        )
    ]

    lead_date = (
        TODAY
        - pd.Timedelta(
            days=np.random.randint(
                0,
                1095
            )
        )
    )

    lead_source = np.random.choice(
        lead_sources,
        p=lead_source_weights
    )

    product_interest = np.random.choice(
        products
    )

    lead_status = np.random.choice(
        lead_statuses,
        p=[
            0.20,
            0.18,
            0.16,
            0.18,
            0.18,
            0.10
        ]
    )

    quoted_premium = round(
        np.random.uniform(
            300,
            25000
        ),
        2
    )

    converted_flag = int(
        lead_status == "Converted"
    )

    leads.append({

        "Lead_ID":
            f"LEAD-{lead_counter:08d}",

        "Customer_ID":
            customer["Customer_ID"],

        "Lead_Date":
            lead_date.date(),

        "Lead_Source":
            lead_source,

        "Product_Interest":
            product_interest,

        "Lead_Status":
            lead_status,

        "Quoted_Premium":
            quoted_premium,

        "Converted_Flag":
            converted_flag
    })

    lead_counter += 1


# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(
    leads
)

# ============================================================
# QUALITY
# ============================================================

print("\n========================================")
print("UAE LEAD DATA QUALITY")
print("========================================\n")

print(
    "Total Leads:",
    f"{len(df):,}"
)

print(
    "Duplicate Lead IDs:",
    df["Lead_ID"].duplicated().sum()
)

print(
    "Missing Values:",
    df.isna().sum().sum()
)

print("\nLead Status:")
print(
    df["Lead_Status"].value_counts()
)

print("\nLead Sources:")
print(
    df["Lead_Source"].value_counts()
)

# ============================================================
# EXPORT
# ============================================================

csv_path = os.path.join(
    DATA_DIR,
    "leads.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "leads.xlsx"
)

df.to_csv(
    csv_path,
    index=False
)

df.to_excel(
    excel_path,
    index=False
)

print("\n========================================")
print("LEADS GENERATED SUCCESSFULLY")
print("========================================")

print(f"CSV   : {csv_path}")
print(f"Excel : {excel_path}")