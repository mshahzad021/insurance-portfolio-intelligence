import pandas as pd
import numpy as np
import os

# ============================================================
# UAE INSURANCE RENEWAL SYNTHETIC DATA GENERATOR
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
# LOAD DATA
# ============================================================

policies = pd.read_csv(
    os.path.join(DATA_DIR, "policies.csv"),
    parse_dates=[
        "Policy_Start_Date",
        "Policy_End_Date"
    ]
)

products = pd.read_csv(
    os.path.join(DATA_DIR, "products.csv")
)

customers = pd.read_csv(
    os.path.join(DATA_DIR, "customers.csv")
)

# ============================================================
# MERGE
# ============================================================

df = policies.merge(
    products[
        [
            "Product_ID",
            "Renewal_Base_Rate"
        ]
    ],
    on="Product_ID",
    how="left"
)

df = df.merge(
    customers[
        [
            "Customer_ID",
            "Customer_Type",
            "Customer_Segment",
            "Emirate"
        ]
    ],
    on="Customer_ID",
    how="left"
)

# ============================================================
# GENERATE RENEWAL RECORDS
# ============================================================

renewals = []

renewal_counter = 1

for _, policy in df.iterrows():

    expiry_date = pd.Timestamp(
        policy["Policy_End_Date"]
    )

    # Only policies that have reached expiry
    if expiry_date > TODAY:
        continue

    base_rate = float(
        policy["Renewal_Base_Rate"]
    )

    # Customer segment adjustment
    if policy["Customer_Segment"] == "High Net Worth":
        base_rate += 0.05

    elif policy["Customer_Segment"] == "Affluent":
        base_rate += 0.03

    # Corporate relationship effect
    if policy["Customer_Type"] == "Corporate":
        base_rate += 0.03

    base_rate = min(
        base_rate,
        0.97
    )

    renewed = np.random.choice(
        [0, 1],
        p=[
            1 - base_rate,
            base_rate
        ]
    )

    renewal_date = (
        expiry_date
        + pd.Timedelta(
            days=np.random.randint(
                -10,
                31
            )
        )
    )

    if renewed == 1:

        renewal_status = "Renewed"

        new_premium = round(
            float(policy["Premium"])
            * np.random.uniform(
                1.03,
                1.15
            ),
            2
        )

    else:

        renewal_status = np.random.choice(
            [
                "Not Renewed",
                "Lost to Competitor",
                "Customer Cancelled"
            ],
            p=[
                0.50,
                0.30,
                0.20
            ]
        )

        new_premium = 0

    renewals.append({

        "Renewal_ID":
            f"REN-{renewal_counter:07d}",

        "Policy_ID":
            policy["Policy_ID"],

        "Customer_ID":
            policy["Customer_ID"],

        "Product_ID":
            policy["Product_ID"],

        "Expiry_Date":
            expiry_date.date(),

        "Renewal_Date":
            renewal_date.date(),

        "Renewal_Status":
            renewal_status,

        "Renewed_Flag":
            renewed,

        "Previous_Premium":
            round(
                float(policy["Premium"]),
                2
            ),

        "New_Premium":
            new_premium,

        "Customer_Type":
            policy["Customer_Type"],

        "Customer_Segment":
            policy["Customer_Segment"],

        "Emirate":
            policy["Emirate"]
    })

    renewal_counter += 1


# ============================================================
# DATAFRAME
# ============================================================

result = pd.DataFrame(
    renewals
)

# ============================================================
# QUALITY CHECKS
# ============================================================

print("\n========================================")
print("UAE RENEWAL DATA QUALITY")
print("========================================\n")

print(
    "Total Renewal Records:",
    f"{len(result):,}"
)

print(
    "Duplicate Renewal IDs:",
    result["Renewal_ID"].duplicated().sum()
)

print(
    "Missing Values:",
    result.isna().sum().sum()
)

print("\nRenewal Status:")
print(
    result["Renewal_Status"]
    .value_counts()
)

# ============================================================
# EXPORT
# ============================================================

csv_path = os.path.join(
    DATA_DIR,
    "renewals.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "renewals.xlsx"
)

result.to_csv(
    csv_path,
    index=False
)

result.to_excel(
    excel_path,
    index=False
)

print("\n========================================")
print("RENEWALS GENERATED SUCCESSFULLY")
print("========================================")

print(f"CSV   : {csv_path}")
print(f"Excel : {excel_path}")