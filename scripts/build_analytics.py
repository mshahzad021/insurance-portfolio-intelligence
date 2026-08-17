import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "analytics")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load(name):
    return pd.read_csv(os.path.join(DATA_DIR, f"{name}.csv"))


# ============================================================
# LOAD
# ============================================================

customers = load("customers")
products = load("products")
policies = load("policies")
claims = load("claims")
payments = load("payments")
renewals = load("renewals")
interactions = load("interactions")
leads = load("leads")


# ============================================================
# DIM_CUSTOMER
# ============================================================

dim_customer = customers.copy()

dim_customer["Customer_Since"] = pd.to_datetime(
    dim_customer["Customer_Since"]
)

dim_customer.to_csv(
    os.path.join(OUTPUT_DIR, "dim_customer.csv"),
    index=False
)


# ============================================================
# DIM_PRODUCT
# ============================================================

dim_product = products.copy()

dim_product.to_csv(
    os.path.join(OUTPUT_DIR, "dim_product.csv"),
    index=False
)


# ============================================================
# FACT_POLICY
# ============================================================

fact_policy = policies.copy()

fact_policy["Policy_Start_Date"] = pd.to_datetime(
    fact_policy["Policy_Start_Date"]
)

fact_policy["Policy_End_Date"] = pd.to_datetime(
    fact_policy["Policy_End_Date"]
)

fact_policy["Policy_Duration_Days"] = (
    fact_policy["Policy_End_Date"]
    - fact_policy["Policy_Start_Date"]
).dt.days

fact_policy["Policy_Year"] = (
    fact_policy["Policy_Start_Date"].dt.year
)

fact_policy.to_csv(
    os.path.join(OUTPUT_DIR, "fact_policy.csv"),
    index=False
)


# ============================================================
# FACT_CLAIMS
# ============================================================

fact_claim = claims.copy()

fact_claim["Claim_Date"] = pd.to_datetime(
    fact_claim["Claim_Date"]
)

fact_claim["Claim_Year"] = (
    fact_claim["Claim_Date"].dt.year
)

fact_claim["Settlement_Gap"] = (
    fact_claim["Claim_Amount"]
    - fact_claim["Settlement_Amount"]
)

fact_claim.to_csv(
    os.path.join(OUTPUT_DIR, "fact_claim.csv"),
    index=False
)


# ============================================================
# FACT_PAYMENT
# ============================================================

fact_payment = payments.copy()

fact_payment["Payment_Date"] = pd.to_datetime(
    fact_payment["Payment_Date"]
)

fact_payment["Payment_Due_Date"] = pd.to_datetime(
    fact_payment["Payment_Due_Date"]
)

fact_payment["Outstanding_Amount"] = (
    fact_payment["Due_Amount"]
    - fact_payment["Paid_Amount"]
)

fact_payment["Payment_Delay_Days"] = (
    fact_payment["Payment_Date"]
    - fact_payment["Payment_Due_Date"]
).dt.days

fact_payment.to_csv(
    os.path.join(OUTPUT_DIR, "fact_payment.csv"),
    index=False
)


# ============================================================
# FACT_RENEWAL
# ============================================================

fact_renewal = renewals.copy()

fact_renewal["Expiry_Date"] = pd.to_datetime(
    fact_renewal["Expiry_Date"]
)

fact_renewal["Renewal_Date"] = pd.to_datetime(
    fact_renewal["Renewal_Date"]
)

fact_renewal["Renewal_Lead_Days"] = (
    fact_renewal["Expiry_Date"]
    - fact_renewal["Renewal_Date"]
).dt.days

fact_renewal["Premium_Change"] = (
    fact_renewal["New_Premium"]
    - fact_renewal["Previous_Premium"]
)

fact_renewal["Premium_Change_%"] = (
    fact_renewal["Premium_Change"]
    / fact_renewal["Previous_Premium"]
    * 100
)

fact_renewal.to_csv(
    os.path.join(OUTPUT_DIR, "fact_renewal.csv"),
    index=False
)


# ============================================================
# FACT_INTERACTION
# ============================================================

fact_interaction = interactions.copy()

fact_interaction["Interaction_Date"] = pd.to_datetime(
    fact_interaction["Interaction_Date"]
)

fact_interaction.to_csv(
    os.path.join(OUTPUT_DIR, "fact_interaction.csv"),
    index=False
)


# ============================================================
# FACT_LEAD
# ============================================================

fact_lead = leads.copy()

fact_lead["Lead_Date"] = pd.to_datetime(
    fact_lead["Lead_Date"]
)

fact_lead["Lead_Year"] = (
    fact_lead["Lead_Date"].dt.year
)

fact_lead.to_csv(
    os.path.join(OUTPUT_DIR, "fact_lead.csv"),
    index=False
)


print("\nANALYTICAL LAYER CREATED")
print("=" * 60)

for file in os.listdir(OUTPUT_DIR):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(OUTPUT_DIR, file))
        print(f"{file:<30} {len(df):>10,} rows")

print("\nOutput directory:")
print(OUTPUT_DIR)