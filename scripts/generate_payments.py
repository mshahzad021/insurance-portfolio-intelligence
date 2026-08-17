import pandas as pd
import numpy as np
import os

# ============================================================
# UAE INSURANCE PAYMENT SYNTHETIC DATA GENERATOR
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
# LOAD POLICIES
# ============================================================

policies = pd.read_csv(
    os.path.join(DATA_DIR, "policies.csv"),
    parse_dates=[
        "Policy_Start_Date",
        "Policy_End_Date"
    ]
)

# ============================================================
# GENERATE PAYMENTS
# ============================================================

payments = []

payment_counter = 1

for _, policy in policies.iterrows():

    start_date = pd.Timestamp(
        policy["Policy_Start_Date"]
    )

    end_date = min(
        pd.Timestamp(policy["Policy_End_Date"]),
        TODAY
    )

    if end_date < start_date:
        continue

    premium = float(
        policy["Premium"]
    )

    frequency = policy[
        "Payment_Frequency"
    ]

    if frequency == "Monthly":
        periods = 12

    elif frequency == "Quarterly":
        periods = 4

    else:
        periods = 1

    # Create payments within policy year
    payment_dates = pd.date_range(
        start=start_date,
        end=end_date,
        periods=min(
            periods,
            max(
                1,
                int(
                    (
                        end_date - start_date
                    ).days / 30
                )
            )
        )
    )

    payment_dates = list(
        payment_dates
    )

    if len(payment_dates) == 0:
        payment_dates = [start_date]

    amount_per_payment = (
        premium / periods
    )

    for payment_date in payment_dates:

        # Some payments become late/unpaid
        payment_status = np.random.choice(
            [
                "Paid",
                "Pending",
                "Failed",
                "Overdue"
            ],
            p=[
                0.82,
                0.08,
                0.04,
                0.06
            ]
        )

        if payment_status == "Paid":

            paid_amount = round(
                amount_per_payment,
                2
            )

        else:

            paid_amount = 0

        payment_method = np.random.choice(
            [
                "Credit Card",
                "Debit Card",
                "Bank Transfer",
                "Direct Debit",
                "Cash",
                "Online Payment"
            ],
            p=[
                0.22,
                0.18,
                0.25,
                0.15,
                0.05,
                0.15
            ]
        )

        payments.append({

            "Payment_ID":
                f"PAY-{payment_counter:08d}",

            "Policy_ID":
                policy["Policy_ID"],

            "Customer_ID":
                policy["Customer_ID"],

            "Payment_Date":
                payment_date.date(),

            "Payment_Due_Date":
                (
                    payment_date
                    - pd.Timedelta(days=5)
                ).date(),

            "Payment_Status":
                payment_status,

            "Payment_Method":
                payment_method,

            "Due_Amount":
                round(
                    amount_per_payment,
                    2
                ),

            "Paid_Amount":
                paid_amount
        })

        payment_counter += 1


# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(payments)

# ============================================================
# QUALITY CHECKS
# ============================================================

print("\n========================================")
print("UAE PAYMENT DATA QUALITY")
print("========================================\n")

print("Total Payments:", f"{len(df):,}")

print(
    "Duplicate Payment IDs:",
    df["Payment_ID"].duplicated().sum()
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
    "Total Due:",
    f"{df['Due_Amount'].sum():,.2f}"
)

print(
    "Total Paid:",
    f"{df['Paid_Amount'].sum():,.2f}"
)

print("\nPayment Status:")
print(
    df["Payment_Status"].value_counts()
)

# ============================================================
# EXPORT
# ============================================================

csv_path = os.path.join(
    DATA_DIR,
    "payments.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "payments.xlsx"
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
print("PAYMENTS GENERATED SUCCESSFULLY")
print("========================================")

print(f"CSV   : {csv_path}")
print(f"Excel : {excel_path}")