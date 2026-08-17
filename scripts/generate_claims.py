import pandas as pd
import numpy as np
import os

# ============================================================
# UAE INSURANCE CLAIMS SYNTHETIC DATA GENERATOR
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

os.makedirs(DATA_DIR, exist_ok=True)

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
# VALIDATION
# ============================================================

required_policy_columns = [
    "Policy_ID",
    "Customer_ID",
    "Product_ID",
    "Policy_Start_Date",
    "Policy_End_Date",
    "Policy_Status",
    "Premium"
]

required_product_columns = [
    "Product_ID",
    "Claim_Probability",
    "Claim_Severity_Min",
    "Claim_Severity_Max"
]

for col in required_policy_columns:
    if col not in policies.columns:
        raise ValueError(
            f"Missing policy column: {col}"
        )

for col in required_product_columns:
    if col not in products.columns:
        raise ValueError(
            f"Missing product column: {col}"
        )

# ============================================================
# MERGE PRODUCT CLAIM PARAMETERS
# ============================================================

policies = policies.merge(
    products[
        [
            "Product_ID",
            "Claim_Probability",
            "Claim_Severity_Min",
            "Claim_Severity_Max"
        ]
    ],
    on="Product_ID",
    how="left"
)

# ============================================================
# MERGE CUSTOMER INFORMATION
# ============================================================

policies = policies.merge(
    customers[
        [
            "Customer_ID",
            "Emirate",
            "Customer_Type",
            "Customer_Segment"
        ]
    ],
    on="Customer_ID",
    how="left"
)

# ============================================================
# GENERATE CLAIMS
# ============================================================

claims = []

claim_counter = 1

for _, policy in policies.iterrows():

    start_date = pd.Timestamp(
        policy["Policy_Start_Date"]
    )

    end_date = min(
        pd.Timestamp(policy["Policy_End_Date"]),
        TODAY
    )

    # Policy must have exposure
    if end_date < start_date:
        continue

    exposure_days = (
        end_date - start_date
    ).days

    exposure_years = max(
        exposure_days / 365,
        0.05
    )

    base_probability = float(
        policy["Claim_Probability"]
    )

    # Approximate probability based on exposure
    adjusted_probability = min(
        base_probability * exposure_years,
        0.70
    )

    # Number of claims
    number_of_claims = np.random.binomial(
        2,
        adjusted_probability
    )

    for _ in range(number_of_claims):

        claim_id = (
            f"CLM-{claim_counter:07d}"
        )

        claim_counter += 1

        # ----------------------------------------------------
        # CLAIM DATE
        # ----------------------------------------------------

        random_days = np.random.randint(
            0,
            max(1, exposure_days + 1)
        )

        claim_date = (
            start_date
            + pd.Timedelta(days=int(random_days))
        )

        # ----------------------------------------------------
        # CLAIM SEVERITY
        # ----------------------------------------------------

        minimum = float(
            policy["Claim_Severity_Min"]
        )

        maximum = float(
            policy["Claim_Severity_Max"]
        )

        claim_amount = np.random.uniform(
            minimum,
            maximum
        )

        claim_amount = round(
            claim_amount,
            2
        )

        # ----------------------------------------------------
        # CLAIM STATUS
        # ----------------------------------------------------

        claim_status = np.random.choice(
            [
                "Approved",
                "Settled",
                "Rejected",
                "Under Investigation"
            ],
            p=[
                0.35,
                0.40,
                0.12,
                0.13
            ]
        )

        # ----------------------------------------------------
        # SETTLEMENT
        # ----------------------------------------------------

        if claim_status in [
            "Approved",
            "Settled"
        ]:

            settlement_ratio = np.random.uniform(
                0.65,
                1.00
            )

            settlement_amount = (
                claim_amount
                * settlement_ratio
            )

            settlement_amount = round(
                settlement_amount,
                2
            )

        else:

            settlement_amount = 0

        # ----------------------------------------------------
        # CLAIM TYPE
        # ----------------------------------------------------

        claim_type = np.random.choice(
            [
                "Accident",
                "Theft",
                "Property Damage",
                "Medical",
                "Liability",
                "Travel Incident",
                "Natural Event",
                "Other"
            ]
        )

        # ----------------------------------------------------
        # FRAUD FLAG
        # ----------------------------------------------------

        fraud_flag = np.random.choice(
            [0, 1],
            p=[0.96, 0.04]
        )

        # ----------------------------------------------------
        # RECORD
        # ----------------------------------------------------

        claims.append({

            "Claim_ID": claim_id,

            "Policy_ID": policy[
                "Policy_ID"
            ],

            "Customer_ID": policy[
                "Customer_ID"
            ],

            "Product_ID": policy[
                "Product_ID"
            ],

            "Claim_Date": claim_date.date(),

            "Claim_Type": claim_type,

            "Claim_Status": claim_status,

            "Claim_Amount": claim_amount,

            "Settlement_Amount": settlement_amount,

            "Fraud_Flag": fraud_flag,

            "Emirate": policy[
                "Emirate"
            ],

            "Customer_Type": policy[
                "Customer_Type"
            ],

            "Customer_Segment": policy[
                "Customer_Segment"
            ]
        })


# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(claims)

# ============================================================
# QUALITY CHECKS
# ============================================================

print("\n========================================")
print("UAE CLAIM DATA QUALITY")
print("========================================\n")

print("Total Claims:", f"{len(df):,}")

print(
    "Duplicate Claim IDs:",
    df["Claim_ID"].duplicated().sum()
)

print(
    "Missing Values:",
    df.isna().sum().sum()
)

print(
    "Invalid Policy IDs:",
    (~df["Policy_ID"].isin(
        policies["Policy_ID"]
    )).sum()
)

print(
    "Total Claim Amount:",
    f"{df['Claim_Amount'].sum():,.2f}"
)

print(
    "Total Settlement Amount:",
    f"{df['Settlement_Amount'].sum():,.2f}"
)

print("\nClaim Status:")
print(df["Claim_Status"].value_counts())

print("\nClaim Type:")
print(df["Claim_Type"].value_counts())

# ============================================================
# EXPORT
# ============================================================

csv_path = os.path.join(
    DATA_DIR,
    "claims.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "claims.xlsx"
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
print("CLAIMS GENERATED SUCCESSFULLY")
print("========================================")

print(f"CSV   : {csv_path}")
print(f"Excel : {excel_path}")