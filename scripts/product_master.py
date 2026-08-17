import pandas as pd
import os


products = [
    {
        "Product_ID": "PROD001",
        "Product_Name": "Medical Malpractice Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "High",
        "Base_Premium": 10000,
        "Premium_Min": 5000,
        "Premium_Max": 25000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 1000000,
        "Claim_Probability": 0.14,
        "Claim_Severity_Min": 5000,
        "Claim_Severity_Max": 150000,
        "Renewal_Base_Rate": 0.78
    },

    {
        "Product_ID": "PROD002",
        "Product_Name": "Marine Cargo Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "High",
        "Base_Premium": 12000,
        "Premium_Min": 5000,
        "Premium_Max": 30000,
        "Sum_Insured_Min": 200000,
        "Sum_Insured_Max": 5000000,
        "Claim_Probability": 0.13,
        "Claim_Severity_Min": 10000,
        "Claim_Severity_Max": 300000,
        "Renewal_Base_Rate": 0.76
    },

    {
        "Product_ID": "PROD003",
        "Product_Name": "Workmen Compensation",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "High",
        "Base_Premium": 7000,
        "Premium_Min": 3000,
        "Premium_Max": 20000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 2000000,
        "Claim_Probability": 0.15,
        "Claim_Severity_Min": 3000,
        "Claim_Severity_Max": 100000,
        "Renewal_Base_Rate": 0.77
    },

    {
        "Product_ID": "PROD004",
        "Product_Name": "Property and Business Interruption",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "High",
        "Base_Premium": 14000,
        "Premium_Min": 7000,
        "Premium_Max": 35000,
        "Sum_Insured_Min": 500000,
        "Sum_Insured_Max": 10000000,
        "Claim_Probability": 0.11,
        "Claim_Severity_Min": 10000,
        "Claim_Severity_Max": 500000,
        "Renewal_Base_Rate": 0.75
    },

    {
        "Product_ID": "PROD005",
        "Product_Name": "Contractors All Risks",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "High",
        "Base_Premium": 15000,
        "Premium_Min": 7000,
        "Premium_Max": 40000,
        "Sum_Insured_Min": 500000,
        "Sum_Insured_Max": 15000000,
        "Claim_Probability": 0.16,
        "Claim_Severity_Min": 10000,
        "Claim_Severity_Max": 600000,
        "Renewal_Base_Rate": 0.74
    },

    {
        "Product_ID": "PROD006",
        "Product_Name": "Motor Fleet Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "High",
        "Base_Premium": 18000,
        "Premium_Min": 8000,
        "Premium_Max": 50000,
        "Sum_Insured_Min": 500000,
        "Sum_Insured_Max": 10000000,
        "Claim_Probability": 0.22,
        "Claim_Severity_Min": 5000,
        "Claim_Severity_Max": 250000,
        "Renewal_Base_Rate": 0.72
    },

    {
        "Product_ID": "PROD007",
        "Product_Name": "Public Liability Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "SME",
        "Risk_Level": "Medium",
        "Base_Premium": 5000,
        "Premium_Min": 2000,
        "Premium_Max": 15000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 3000000,
        "Claim_Probability": 0.09,
        "Claim_Severity_Min": 3000,
        "Claim_Severity_Max": 100000,
        "Renewal_Base_Rate": 0.80
    },

    {
        "Product_ID": "PROD008",
        "Product_Name": "Professional Indemnity Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "SME",
        "Risk_Level": "Medium",
        "Base_Premium": 6000,
        "Premium_Min": 2500,
        "Premium_Max": 18000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 3000000,
        "Claim_Probability": 0.08,
        "Claim_Severity_Min": 3000,
        "Claim_Severity_Max": 120000,
        "Renewal_Base_Rate": 0.81
    },

    {
        "Product_ID": "PROD009",
        "Product_Name": "Group Health Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "Medium",
        "Base_Premium": 9000,
        "Premium_Min": 4000,
        "Premium_Max": 25000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 2000000,
        "Claim_Probability": 0.18,
        "Claim_Severity_Min": 1000,
        "Claim_Severity_Max": 80000,
        "Renewal_Base_Rate": 0.83
    },

    {
        "Product_ID": "PROD010",
        "Product_Name": "Group Life Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "Low",
        "Base_Premium": 7500,
        "Premium_Min": 3000,
        "Premium_Max": 20000,
        "Sum_Insured_Min": 200000,
        "Sum_Insured_Max": 5000000,
        "Claim_Probability": 0.05,
        "Claim_Severity_Min": 10000,
        "Claim_Severity_Max": 500000,
        "Renewal_Base_Rate": 0.87
    },

    {
        "Product_ID": "PROD011",
        "Product_Name": "Event Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "SME",
        "Risk_Level": "Medium",
        "Base_Premium": 3000,
        "Premium_Min": 1000,
        "Premium_Max": 10000,
        "Sum_Insured_Min": 50000,
        "Sum_Insured_Max": 1000000,
        "Claim_Probability": 0.07,
        "Claim_Severity_Min": 1000,
        "Claim_Severity_Max": 50000,
        "Renewal_Base_Rate": 0.68
    },

    {
        "Product_ID": "PROD012",
        "Product_Name": "Drone Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "SME",
        "Risk_Level": "High",
        "Base_Premium": 2500,
        "Premium_Min": 1000,
        "Premium_Max": 8000,
        "Sum_Insured_Min": 20000,
        "Sum_Insured_Max": 500000,
        "Claim_Probability": 0.17,
        "Claim_Severity_Min": 1000,
        "Claim_Severity_Max": 50000,
        "Renewal_Base_Rate": 0.70
    },

    {
        "Product_ID": "PROD013",
        "Product_Name": "Cyber Security Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "SME",
        "Risk_Level": "High",
        "Base_Premium": 8000,
        "Premium_Min": 3000,
        "Premium_Max": 25000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 5000000,
        "Claim_Probability": 0.16,
        "Claim_Severity_Min": 5000,
        "Claim_Severity_Max": 300000,
        "Renewal_Base_Rate": 0.78
    },

    {
        "Product_ID": "PROD014",
        "Product_Name": "SME Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "SME",
        "Risk_Level": "Medium",
        "Base_Premium": 4500,
        "Premium_Min": 2000,
        "Premium_Max": 15000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 3000000,
        "Claim_Probability": 0.10,
        "Claim_Severity_Min": 2000,
        "Claim_Severity_Max": 100000,
        "Renewal_Base_Rate": 0.82
    },

    {
        "Product_ID": "PROD015",
        "Product_Name": "Political Violence Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "Corporate",
        "Risk_Level": "High",
        "Base_Premium": 20000,
        "Premium_Min": 10000,
        "Premium_Max": 60000,
        "Sum_Insured_Min": 1000000,
        "Sum_Insured_Max": 20000000,
        "Claim_Probability": 0.06,
        "Claim_Severity_Min": 20000,
        "Claim_Severity_Max": 1000000,
        "Renewal_Base_Rate": 0.65
    },

    {
        "Product_ID": "PROD016",
        "Product_Name": "Car Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Medium",
        "Base_Premium": 800,
        "Premium_Min": 400,
        "Premium_Max": 2500,
        "Sum_Insured_Min": 5000,
        "Sum_Insured_Max": 100000,
        "Claim_Probability": 0.12,
        "Claim_Severity_Min": 500,
        "Claim_Severity_Max": 15000,
        "Renewal_Base_Rate": 0.84
    },

    {
        "Product_ID": "PROD017",
        "Product_Name": "Home Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Low",
        "Base_Premium": 900,
        "Premium_Min": 400,
        "Premium_Max": 3000,
        "Sum_Insured_Min": 20000,
        "Sum_Insured_Max": 500000,
        "Claim_Probability": 0.07,
        "Claim_Severity_Min": 500,
        "Claim_Severity_Max": 20000,
        "Renewal_Base_Rate": 0.88
    },

    {
        "Product_ID": "PROD018",
        "Product_Name": "Health Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Medium",
        "Base_Premium": 1200,
        "Premium_Min": 500,
        "Premium_Max": 5000,
        "Sum_Insured_Min": 10000,
        "Sum_Insured_Max": 500000,
        "Claim_Probability": 0.18,
        "Claim_Severity_Min": 500,
        "Claim_Severity_Max": 25000,
        "Renewal_Base_Rate": 0.85
    },

    {
        "Product_ID": "PROD019",
        "Product_Name": "Life Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Low",
        "Base_Premium": 1500,
        "Premium_Min": 600,
        "Premium_Max": 5000,
        "Sum_Insured_Min": 50000,
        "Sum_Insured_Max": 1000000,
        "Claim_Probability": 0.04,
        "Claim_Severity_Min": 5000,
        "Claim_Severity_Max": 500000,
        "Renewal_Base_Rate": 0.90
    },

    {
        "Product_ID": "PROD020",
        "Product_Name": "Savings",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Low",
        "Base_Premium": 1000,
        "Premium_Min": 500,
        "Premium_Max": 5000,
        "Sum_Insured_Min": 5000,
        "Sum_Insured_Max": 100000,
        "Claim_Probability": 0.01,
        "Claim_Severity_Min": 100,
        "Claim_Severity_Max": 5000,
        "Renewal_Base_Rate": 0.92
    },

    {
        "Product_ID": "PROD021",
        "Product_Name": "Travel Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Low",
        "Base_Premium": 250,
        "Premium_Min": 100,
        "Premium_Max": 1000,
        "Sum_Insured_Min": 5000,
        "Sum_Insured_Max": 100000,
        "Claim_Probability": 0.06,
        "Claim_Severity_Min": 100,
        "Claim_Severity_Max": 10000,
        "Renewal_Base_Rate": 0.65
    },

    {
        "Product_ID": "PROD022",
        "Product_Name": "Bike Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Medium",
        "Base_Premium": 350,
        "Premium_Min": 150,
        "Premium_Max": 1000,
        "Sum_Insured_Min": 2000,
        "Sum_Insured_Max": 30000,
        "Claim_Probability": 0.13,
        "Claim_Severity_Min": 200,
        "Claim_Severity_Max": 8000,
        "Renewal_Base_Rate": 0.80
    },

    {
        "Product_ID": "PROD023",
        "Product_Name": "Pet Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Medium",
        "Base_Premium": 400,
        "Premium_Min": 150,
        "Premium_Max": 1500,
        "Sum_Insured_Min": 2000,
        "Sum_Insured_Max": 30000,
        "Claim_Probability": 0.09,
        "Claim_Severity_Min": 200,
        "Claim_Severity_Max": 6000,
        "Renewal_Base_Rate": 0.78
    },

    {
        "Product_ID": "PROD024",
        "Product_Name": "Business Insurance",
        "Product_Category": "Commercial",
        "Target_Customer": "SME",
        "Risk_Level": "Medium",
        "Base_Premium": 7500,
        "Premium_Min": 3000,
        "Premium_Max": 25000,
        "Sum_Insured_Min": 100000,
        "Sum_Insured_Max": 5000000,
        "Claim_Probability": 0.11,
        "Claim_Severity_Min": 3000,
        "Claim_Severity_Max": 150000,
        "Renewal_Base_Rate": 0.81
    },

    {
        "Product_ID": "PROD025",
        "Product_Name": "Cycle Insurance",
        "Product_Category": "Personal",
        "Target_Customer": "Individual",
        "Risk_Level": "Low",
        "Base_Premium": 200,
        "Premium_Min": 100,
        "Premium_Max": 700,
        "Sum_Insured_Min": 1000,
        "Sum_Insured_Max": 20000,
        "Claim_Probability": 0.08,
        "Claim_Severity_Min": 100,
        "Claim_Severity_Max": 5000,
        "Renewal_Base_Rate": 0.75
    }
]


df = pd.DataFrame(products)


# -----------------------------
# EXPORT
# -----------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)


csv_path = os.path.join(
    DATA_DIR,
    "products.csv"
)

excel_path = os.path.join(
    DATA_DIR,
    "products.xlsx"
)


df.to_csv(
    csv_path,
    index=False
)

df.to_excel(
    excel_path,
    index=False
)


print("Product master created successfully!")
print(f"Products: {len(df)}")

print("\nFiles created:")
print(csv_path)
print(excel_path)

print("\nProduct Preview:")
print(
    df[
        [
            "Product_ID",
            "Product_Name",
            "Risk_Level"
        ]
    ]
)