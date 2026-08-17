import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime
import os


# ============================================================
# UAE INSURANCE CUSTOMER SYNTHETIC DATA GENERATOR
# ============================================================

SEED = 42
N_CUSTOMERS = 25_000

np.random.seed(SEED)
fake = Faker()
Faker.seed(SEED)


# ============================================================
# UAE REFERENCE DATA
# ============================================================

emirates = [
    "Dubai",
    "Abu Dhabi",
    "Sharjah",
    "Ajman",
    "Ras Al Khaimah",
    "Fujairah",
    "Umm Al Quwain"
]

# Realistic portfolio concentration
emirate_weights = [
    0.40,   # Dubai
    0.30,   # Abu Dhabi
    0.14,   # Sharjah
    0.06,   # Ajman
    0.05,   # Ras Al Khaimah
    0.03,   # Fujairah
    0.02    # Umm Al Quwain
]


# ============================================================
# UAE NATIONALITY MIX
# ============================================================

nationalities = [
    "Indian",
    "Pakistani",
    "Bangladeshi",
    "Filipino",
    "Emirati",
    "Egyptian",
    "Nepalese",
    "Sri Lankan",
    "British",
    "Other"
]

nationality_weights = [
    0.25,
    0.15,
    0.08,
    0.07,
    0.12,
    0.07,
    0.05,
    0.04,
    0.04,
    0.13
]


# ============================================================
# UAE INDUSTRIES
# ============================================================

industries = [
    "Retail",
    "Construction",
    "Real Estate",
    "IT & Software",
    "Financial Services",
    "Healthcare",
    "Education",
    "Logistics",
    "Hospitality",
    "Travel & Tourism",
    "Manufacturing",
    "Professional Services",
    "Government"
]


# ============================================================
# INSURANCE ACQUISITION CHANNELS
# ============================================================

channels = [
    "Insurance Broker",
    "Direct Online",
    "Insurance Agent",
    "Bank / Bancassurance",
    "Corporate Partner",
    "Branch"
]

channel_weights = [
    0.28,
    0.22,
    0.18,
    0.12,
    0.12,
    0.08
]


# ============================================================
# CUSTOMER TYPE
# ============================================================

customer_types = np.random.choice(
    ["Individual", "SME", "Corporate"],
    size=N_CUSTOMERS,
    p=[0.72, 0.20, 0.08]
)


# ============================================================
# CUSTOMER SEGMENT LOGIC
# ============================================================

customers = []

for i in range(N_CUSTOMERS):

    customer_id = f"CUST-{i+1:05d}"

    customer_type = customer_types[i]

    # --------------------------------------------------------
    # AGE
    # --------------------------------------------------------

    if customer_type == "Individual":
        age = np.random.randint(21, 70)

    elif customer_type == "SME":
        age = np.random.randint(25, 65)

    else:
        age = np.random.randint(30, 65)


    # --------------------------------------------------------
    # GENDER
    # --------------------------------------------------------

    gender = np.random.choice(
        ["Male", "Female"],
        p=[0.62, 0.38]
    )


    # --------------------------------------------------------
    # EMIRATE
    # --------------------------------------------------------

    emirate = np.random.choice(
        emirates,
        p=emirate_weights
    )


    # --------------------------------------------------------
    # NATIONALITY
    # --------------------------------------------------------

    nationality = np.random.choice(
        nationalities,
        p=nationality_weights
    )


    # --------------------------------------------------------
    # INDUSTRY
    # --------------------------------------------------------

    if customer_type == "Individual":

        industry = "Individual"

    else:

        industry = np.random.choice(
            industries
        )


    # --------------------------------------------------------
    # COMPANY SIZE
    # --------------------------------------------------------

    if customer_type == "Individual":

        company_size = "N/A"

    elif customer_type == "SME":

        company_size = np.random.choice(
            ["Micro", "Small", "Medium"],
            p=[0.30, 0.45, 0.25]
        )

    else:

        company_size = "Large"


    # --------------------------------------------------------
    # CUSTOMER SEGMENT
    # --------------------------------------------------------

    if customer_type == "Individual":

        segment = np.random.choice(
            [
                "Mass Market",
                "Affluent",
                "High Net Worth"
            ],
            p=[0.65, 0.28, 0.07]
        )

    elif customer_type == "SME":

        segment = "SME"

    else:

        segment = "Corporate"


    # --------------------------------------------------------
    # ACQUISITION CHANNEL
    # --------------------------------------------------------

    acquisition_channel = np.random.choice(
        channels,
        p=channel_weights
    )


    # --------------------------------------------------------
    # CUSTOMER SINCE
    # --------------------------------------------------------

    start_date = fake.date_between(
        start_date="-8y",
        end_date="-30d"
    )


    # --------------------------------------------------------
    # CUSTOMER RECORD
    # --------------------------------------------------------

    customers.append({

        "Customer_ID": customer_id,

        "Customer_Type": customer_type,

        "Gender": gender,

        "Age": age,

        "Nationality": nationality,

        "Emirate": emirate,

        "Industry": industry,

        "Company_Size": company_size,

        "Customer_Segment": segment,

        "Customer_Since": start_date,

        "Acquisition_Channel": acquisition_channel

    })


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(customers)


# ============================================================
# DATA QUALITY CHECKS
# ============================================================

print("\n========================================")
print("UAE CUSTOMER DATA QUALITY")
print("========================================\n")

print("Total Rows:", len(df))

print(
    "Duplicate Customer IDs:",
    df["Customer_ID"].duplicated().sum()
)

print(
    "Missing Values:",
    df.isna().sum().sum()
)


# ============================================================
# CUSTOMER TYPE DISTRIBUTION
# ============================================================

print("\nCustomer Type Distribution:")

print(
    df["Customer_Type"]
    .value_counts(normalize=True)
    .round(3)
)


# ============================================================
# CUSTOMER SEGMENT DISTRIBUTION
# ============================================================

print("\nCustomer Segment Distribution:")

print(
    df["Customer_Segment"]
    .value_counts()
)


# ============================================================
# UAE EMIRATE DISTRIBUTION
# ============================================================

print("\nEmirate Distribution:")

print(
    df["Emirate"]
    .value_counts()
)


# ============================================================
# NATIONALITY DISTRIBUTION
# ============================================================

print("\nNationality Distribution:")

print(
    df["Nationality"]
    .value_counts()
)


# ============================================================
# ACQUISITION CHANNEL DISTRIBUTION
# ============================================================

print("\nAcquisition Channel Distribution:")

print(
    df["Acquisition_Channel"]
    .value_counts()
)


# ============================================================
# EXPORT
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

# Create data folder if it doesn't exist
os.makedirs(
    DATA_DIR,
    exist_ok=True
)


# File paths
csv_path = os.path.join(
    DATA_DIR,
    "customers.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "customers.xlsx"
)


# Export CSV
df.to_csv(
    csv_path,
    index=False
)


# Export Excel
df.to_excel(
    excel_path,
    index=False
)


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n========================================")
print("UAE CUSTOMER DATA GENERATED SUCCESSFULLY")
print("========================================")

print(f"\nTotal Customers: {len(df):,}")

print("\nFiles created:")

print(f"CSV   : {csv_path}")
print(f"Excel : {excel_path}")

print("\nColumns:")

print(df.columns.tolist())