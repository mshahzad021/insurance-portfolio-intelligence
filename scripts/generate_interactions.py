import pandas as pd
import numpy as np
import os

# ============================================================
# UAE INSURANCE CUSTOMER INTERACTION GENERATOR
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
    os.path.join(DATA_DIR, "customers.csv")
)

# ============================================================
# INTERACTION TYPES
# ============================================================

interaction_types = [
    "Phone Call",
    "Email",
    "Complaint",
    "Quote Request",
    "Policy Inquiry",
    "Claim Inquiry",
    "Payment Inquiry",
    "Website Visit",
    "Agent Meeting",
    "Service Request"
]

interaction_weights = [
    0.16,
    0.14,
    0.06,
    0.08,
    0.16,
    0.10,
    0.08,
    0.10,
    0.06,
    0.06
]

channels = [
    "Phone",
    "Email",
    "Mobile App",
    "Website",
    "Branch",
    "Agent"
]

# ============================================================
# GENERATE
# ============================================================

interactions = []

interaction_counter = 1

for _, customer in customers.iterrows():

    customer_type = customer[
        "Customer_Type"
    ]

    # Different customer types generate
    # different interaction volumes.

    if customer_type == "Individual":

        interaction_count = np.random.poisson(
            4
        )

    elif customer_type == "SME":

        interaction_count = np.random.poisson(
            7
        )

    else:

        interaction_count = np.random.poisson(
            10
        )

    # At least one interaction for meaningful analytics
    interaction_count = max(
        interaction_count,
        1
    )

    for _ in range(interaction_count):

        interaction_date = (
            TODAY
            - pd.Timedelta(
                days=np.random.randint(
                    0,
                    1095
                )
            )
        )

        interaction_type = np.random.choice(
            interaction_types,
            p=interaction_weights
        )

        channel = np.random.choice(
            channels
        )

        # Satisfaction score
        satisfaction_score = np.random.choice(
            [1, 2, 3, 4, 5],
            p=[
                0.05,
                0.08,
                0.17,
                0.35,
                0.35
            ]
        )

        # Resolution
        resolved_flag = np.random.choice(
            [0, 1],
            p=[
                0.15,
                0.85
            ]
        )

        # Response time
        response_time_hours = round(
            np.random.lognormal(
                mean=1.0,
                sigma=0.8
            ),
            2
        )

        interactions.append({

            "Interaction_ID":
                f"INT-{interaction_counter:08d}",

            "Customer_ID":
                customer["Customer_ID"],

            "Interaction_Date":
                interaction_date.date(),

            "Interaction_Type":
                interaction_type,

            "Channel":
                channel,

            "Satisfaction_Score":
                satisfaction_score,

            "Resolved_Flag":
                resolved_flag,

            "Response_Time_Hours":
                response_time_hours
        })

        interaction_counter += 1


# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(
    interactions
)

# ============================================================
# QUALITY
# ============================================================

print("\n========================================")
print("UAE INTERACTION DATA QUALITY")
print("========================================\n")

print(
    "Total Interactions:",
    f"{len(df):,}"
)

print(
    "Duplicate IDs:",
    df["Interaction_ID"].duplicated().sum()
)

print(
    "Missing Values:",
    df.isna().sum().sum()
)

print(
    "Invalid Customer IDs:",
    (~df["Customer_ID"].isin(
        customers["Customer_ID"]
    )).sum()
)

print("\nInteraction Types:")
print(
    df["Interaction_Type"].value_counts()
)

# ============================================================
# EXPORT
# ============================================================

csv_path = os.path.join(
    DATA_DIR,
    "interactions.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "interactions.xlsx"
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
print("INTERACTIONS GENERATED SUCCESSFULLY")
print("========================================")

print(f"CSV   : {csv_path}")
print(f"Excel : {excel_path}")