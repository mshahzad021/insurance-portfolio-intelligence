import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "policies": "policies.csv",
    "claims": "claims.csv",
    "payments": "payments.csv",
    "renewals": "renewals.csv",
    "interactions": "interactions.csv",
    "leads": "leads.csv",
}

PRIMARY_KEYS = {
    "customers": "Customer_ID",
    "products": "Product_ID",
    "policies": "Policy_ID",
    "claims": "Claim_ID",
    "payments": "Payment_ID",
    "renewals": "Renewal_ID",
    "interactions": "Interaction_ID",
    "leads": "Lead_ID",
}


def profile_dataset(name, filename):
    path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(path)

    pk = PRIMARY_KEYS[name]

    return {
        "Dataset": name,
        "Rows": len(df),
        "Columns": len(df.columns),
        "Duplicate_PK": df[pk].duplicated().sum(),
        "Null_Cells": int(df.isna().sum().sum()),
        "Null_Rate_%": round(
            df.isna().sum().sum() / df.size * 100, 2
        ),
        "Status": "PASS"
        if df[pk].duplicated().sum() == 0
        else "FAIL",
    }


results = []

for name, filename in FILES.items():
    results.append(profile_dataset(name, filename))

dq_report = pd.DataFrame(results)

output_file = os.path.join(
    OUTPUT_DIR,
    "data_quality_profile.csv"
)

dq_report.to_csv(output_file, index=False)

print("\nDATA QUALITY PROFILE")
print("=" * 60)
print(dq_report.to_string(index=False))

print(f"\nReport saved to: {output_file}")