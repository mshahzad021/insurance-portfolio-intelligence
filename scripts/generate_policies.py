import pandas as pd
import numpy as np
import os


# ============================================================
# UAE INSURANCE POLICY SYNTHETIC DATA GENERATOR
# ============================================================

SEED = 42
np.random.seed(SEED)

TARGET_POLICIES_MIN = 40_000
TARGET_POLICIES_MAX = 60_000


# ============================================================
# PROJECT DIRECTORIES
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

os.makedirs(
    DATA_DIR,
    exist_ok=True
)


# ============================================================
# LOAD SOURCE DATA
# ============================================================

customers_path = os.path.join(
    DATA_DIR,
    "customers.csv"
)

products_path = os.path.join(
    DATA_DIR,
    "products.csv"
)

customers = pd.read_csv(
    customers_path
)

products = pd.read_csv(
    products_path
)


# ============================================================
# VALIDATE SOURCE DATA
# ============================================================

required_customer_columns = [
    "Customer_ID",
    "Customer_Type",
    "Customer_Segment",
    "Emirate",
    "Acquisition_Channel"
]

required_product_columns = [
    "Product_ID",
    "Product_Name",
    "Product_Category",
    "Target_Customer",
    "Risk_Level",
    "Premium_Min",
    "Premium_Max",
    "Sum_Insured_Min",
    "Sum_Insured_Max",
    "Renewal_Base_Rate"
]

missing_customer_columns = [
    col for col in required_customer_columns
    if col not in customers.columns
]

missing_product_columns = [
    col for col in required_product_columns
    if col not in products.columns
]

if missing_customer_columns:
    raise ValueError(
        f"Missing customer columns: {missing_customer_columns}"
    )

if missing_product_columns:
    raise ValueError(
        f"Missing product columns: {missing_product_columns}"
    )


# ============================================================
# CUSTOMER POLICY COUNT LOGIC
# ============================================================

def determine_policy_count(customer_type, segment):

    if customer_type == "Individual":

        if segment == "High Net Worth":
            return np.random.choice(
                [1, 2, 3, 4],
                p=[0.25, 0.35, 0.25, 0.15]
            )

        elif segment == "Affluent":
            return np.random.choice(
                [1, 2, 3],
                p=[0.35, 0.45, 0.20]
            )

        else:
            return np.random.choice(
                [1, 2, 3],
                p=[0.60, 0.30, 0.10]
            )

    elif customer_type == "SME":

        return np.random.choice(
            [1, 2, 3, 4],
            p=[0.25, 0.35, 0.25, 0.15]
        )

    else:

        return np.random.choice(
            [2, 3, 4, 5, 6],
            p=[0.15, 0.25, 0.30, 0.20, 0.10]
        )


# ============================================================
# PRODUCT ELIGIBILITY
# ============================================================

def get_eligible_products(customer_type):

    # Handle Target_Customer values such as:
    # Individual
    # SME
    # Corporate
    # SME/Corporate

    eligible = products[
        products["Target_Customer"].apply(
            lambda x:
                customer_type in str(x).replace(
                    " ",
                    ""
                ).split("/")
        )
    ]

    return eligible


# ============================================================
# PREMIUM GENERATION
# ============================================================

def generate_premium(product):

    minimum = float(
        product["Premium_Min"]
    )

    maximum = float(
        product["Premium_Max"]
    )

    # Triangular distribution gives more realistic
    # concentration around the middle.

    mode = float(
        product["Base_Premium"]
    )

    premium = np.random.triangular(
        minimum,
        mode,
        maximum
    )

    return round(
        premium,
        2
    )


# ============================================================
# SUM INSURED GENERATION
# ============================================================

def generate_sum_insured(product):

    minimum = float(
        product["Sum_Insured_Min"]
    )

    maximum = float(
        product["Sum_Insured_Max"]
    )

    insured_amount = np.random.uniform(
        minimum,
        maximum
    )

    return round(
        insured_amount,
        2
    )


# ============================================================
# PAYMENT FREQUENCY
# ============================================================

def generate_payment_frequency(
    customer_type
):

    if customer_type == "Individual":

        return np.random.choice(
            [
                "Monthly",
                "Quarterly",
                "Annual"
            ],
            p=[
                0.45,
                0.25,
                0.30
            ]
        )

    elif customer_type == "SME":

        return np.random.choice(
            [
                "Monthly",
                "Quarterly",
                "Annual"
            ],
            p=[
                0.20,
                0.35,
                0.45
            ]
        )

    else:

        return np.random.choice(
            [
                "Quarterly",
                "Annual"
            ],
            p=[
                0.30,
                0.70
            ]
        )


# ============================================================
# POLICY STATUS
# ============================================================

def generate_policy_status(
    start_date
):

    today = pd.Timestamp(
        "2026-08-15"
    )

    end_date = (
        start_date
        + pd.DateOffset(years=1)
    )

    # Current policies
    if end_date >= today:

        return np.random.choice(
            [
                "Active",
                "Cancelled"
            ],
            p=[
                0.94,
                0.06
            ]
        )

    # Historical policies
    return np.random.choice(
        [
            "Expired",
            "Cancelled"
        ],
        p=[
            0.88,
            0.12
        ]
    )


# ============================================================
# GENERATE POLICIES
# ============================================================

policy_records = []

policy_counter = 1


for _, customer in customers.iterrows():

    customer_type = customer[
        "Customer_Type"
    ]

    segment = customer[
        "Customer_Segment"
    ]

    customer_id = customer[
        "Customer_ID"
    ]

    acquisition_channel = customer[
        "Acquisition_Channel"
    ]

    # --------------------------------------------------------
    # NUMBER OF POLICIES
    # --------------------------------------------------------

    number_of_policies = determine_policy_count(
        customer_type,
        segment
    )

    # --------------------------------------------------------
    # ELIGIBLE PRODUCTS
    # --------------------------------------------------------

    eligible_products = get_eligible_products(
        customer_type
    )

    # Safety check
    if len(eligible_products) == 0:

        raise ValueError(
            f"No eligible products found for "
            f"{customer_type}"
        )

    # Avoid duplicate products for same customer
    number_of_products = min(
        number_of_policies,
        len(eligible_products)
    )

    selected_products = eligible_products.sample(
        n=number_of_products,
        replace=False,
        random_state=np.random.randint(
            1,
            1_000_000
        )
    )

    # --------------------------------------------------------
    # GENERATE EACH POLICY
    # --------------------------------------------------------

    for _, product in selected_products.iterrows():

        policy_id = (
            f"POL-{policy_counter:06d}"
        )

        policy_counter += 1

        # ----------------------------------------------------
        # POLICY DATE
        # ----------------------------------------------------

        customer_since = pd.to_datetime(
            customer["Customer_Since"]
        )

        start_date = customer_since + pd.Timedelta(
            days=np.random.randint(
                0,
                max(
                    1,
                    (
                        pd.Timestamp("2026-08-15")
                        - customer_since
                    ).days
                )
            )
        )

        # Keep historical window realistic
        if start_date > pd.Timestamp(
            "2026-08-15"
        ):
            start_date = pd.Timestamp(
                "2026-08-15"
            )

        end_date = (
            start_date
            + pd.DateOffset(years=1)
        )

        # ----------------------------------------------------
        # POLICY STATUS
        # ----------------------------------------------------

        status = generate_policy_status(
            start_date
        )

        # ----------------------------------------------------
        # PREMIUM
        # ----------------------------------------------------

        premium = generate_premium(
            product
        )

        # Affluent/HNW customers generally
        # carry higher premiums.

        if segment == "Affluent":

            premium *= np.random.uniform(
                1.10,
                1.35
            )

        elif segment == "High Net Worth":

            premium *= np.random.uniform(
                1.30,
                1.80
            )

        elif customer_type == "Corporate":

            premium *= np.random.uniform(
                1.20,
                1.60
            )

        premium = round(
            premium,
            2
        )

        # ----------------------------------------------------
        # SUM INSURED
        # ----------------------------------------------------

        sum_insured = generate_sum_insured(
            product
        )

        if segment == "High Net Worth":

            sum_insured *= np.random.uniform(
                1.20,
                1.60
            )

        elif customer_type == "Corporate":

            sum_insured *= np.random.uniform(
                1.30,
                2.00
            )

        sum_insured = round(
            sum_insured,
            2
        )

        # ----------------------------------------------------
        # PREMIUM CHANGE
        # ----------------------------------------------------

        premium_change = np.random.choice(
            [
                0,
                5,
                8,
                10,
                15,
                20
            ],
            p=[
                0.20,
                0.20,
                0.20,
                0.20,
                0.15,
                0.05
            ]
        )

        # ----------------------------------------------------
        # PAYMENT FREQUENCY
        # ----------------------------------------------------

        payment_frequency = (
            generate_payment_frequency(
                customer_type
            )
        )

        # ----------------------------------------------------
        # SALES CHANNEL
        # --------------------------------------------------------

        sales_channel = np.random.choice(
            [
                "Insurance Broker",
                "Direct Online",
                "Insurance Agent",
                "Bank / Bancassurance",
                "Corporate Partner",
                "Branch"
            ],
            p=[
                0.28,
                0.22,
                0.18,
                0.12,
                0.12,
                0.08
            ]
        )

        # ----------------------------------------------------
        # CANCELLATION
        # ----------------------------------------------------

        cancellation_flag = (
            1 if status == "Cancelled"
            else 0
        )

        # ----------------------------------------------------
        # TENURE
        # ----------------------------------------------------

        today = pd.Timestamp(
            "2026-08-15"
        )

        policy_tenure_months = max(
            0,
            (
                min(today, end_date)
                - start_date
            ).days // 30
        )

        # ----------------------------------------------------
        # POLICY RECORD
        # ----------------------------------------------------

        policy_records.append({

            "Policy_ID": policy_id,

            "Customer_ID": customer_id,

            "Product_ID": product[
                "Product_ID"
            ],

            "Product_Name": product[
                "Product_Name"
            ],

            "Product_Category": product[
                "Product_Category"
            ],

            "Agent_ID": (
                f"AGT-"
                f"{np.random.randint(1, 151):03d}"
            ),

            "Policy_Start_Date": (
                start_date.date()
            ),

            "Policy_End_Date": (
                end_date.date()
            ),

            "Policy_Status": status,

            "Premium": premium,

            "Sum_Insured": sum_insured,

            "Payment_Frequency": (
                payment_frequency
            ),

            "Sales_Channel": sales_channel,

            "Premium_Increase_Pct": (
                premium_change
            ),

            "Policy_Tenure_Months": (
                policy_tenure_months
            ),

            "Cancellation_Flag": (
                cancellation_flag
            )
        })


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(
    policy_records
)


# ============================================================
# DATA QUALITY CHECKS
# ============================================================

print("\n========================================")
print("UAE POLICY DATA QUALITY")
print("========================================\n")

print(
    "Total Policies:",
    f"{len(df):,}"
)

print(
    "Duplicate Policy IDs:",
    df["Policy_ID"].duplicated().sum()
)

print(
    "Missing Values:",
    df.isna().sum().sum()
)


# ============================================================
# REFERENTIAL INTEGRITY
# ============================================================

valid_customers = set(
    customers["Customer_ID"]
)

invalid_customers = (
    ~df["Customer_ID"]
    .isin(valid_customers)
).sum()

print(
    "Invalid Customer IDs:",
    invalid_customers
)


valid_products = set(
    products["Product_ID"]
)

invalid_products = (
    ~df["Product_ID"]
    .isin(valid_products)
).sum()

print(
    "Invalid Product IDs:",
    invalid_products
)


# ============================================================
# POLICY STATUS
# ============================================================

print("\nPolicy Status Distribution:")

print(
    df["Policy_Status"]
    .value_counts(
        normalize=True
    ).round(3)
)


# ============================================================
# CUSTOMER TYPE POLICY ANALYSIS
# ============================================================

customer_type_map = customers[
    [
        "Customer_ID",
        "Customer_Type"
    ]
]

df_check = df.merge(
    customer_type_map,
    on="Customer_ID",
    how="left"
)

print(
    "\nPolicies by Customer Type:"
)

print(
    df_check[
        "Customer_Type"
    ].value_counts()
)


# ============================================================
# PRODUCT DISTRIBUTION
# ============================================================

print(
    "\nTop Insurance Products:"
)

print(
    df[
        "Product_Name"
    ].value_counts().head(15)
)


# ============================================================
# PREMIUM SUMMARY
# ============================================================

print(
    "\nPremium Summary:"
)

print(
    df[
        "Premium"
    ].describe().round(2)
)


# ============================================================
# TOTAL PREMIUM
# ============================================================

print(
    "\nTotal Portfolio Premium:",
    f"{df['Premium'].sum():,.2f}"
)


# ============================================================
# AVERAGE PREMIUM
# ============================================================

print(
    "Average Policy Premium:",
    f"{df['Premium'].mean():,.2f}"
)


# ============================================================
# MULTI-POLICY CUSTOMERS
# ============================================================

policies_per_customer = (
    df.groupby(
        "Customer_ID"
    )["Policy_ID"]
    .count()
)

multi_policy_rate = (
    (
        policies_per_customer >= 2
    ).mean()
)

print(
    "\nMulti-Policy Customer Rate:",
    f"{multi_policy_rate:.2%}"
)


# ============================================================
# EXPORT
# ============================================================

csv_path = os.path.join(
    DATA_DIR,
    "policies.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "policies.xlsx"
)


df.to_csv(
    csv_path,
    index=False
)

df.to_excel(
    excel_path,
    index=False
)


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n========================================")
print("UAE POLICY DATA GENERATED SUCCESSFULLY")
print("========================================")

print(
    f"\nTotal Policies: {len(df):,}"
)

print(
    f"Total Premium: {df['Premium'].sum():,.2f}"
)

print(
    f"Average Premium: {df['Premium'].mean():,.2f}"
)

print("\nFiles created:")

print(
    f"CSV   : {csv_path}"
)

print(
    f"Excel : {excel_path}"
)