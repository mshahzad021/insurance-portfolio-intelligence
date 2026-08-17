SELECT
  cl.Claim_ID,
  cl.Policy_ID,
  cl.Customer_ID,
  cl.Product_ID,

  cl.Claim_Date,
  EXTRACT(YEAR FROM cl.Claim_Date) AS Claim_Year,
  EXTRACT(MONTH FROM cl.Claim_Date) AS Claim_Month,

  cl.Claim_Type,
  cl.Claim_Status,

  cl.Claim_Amount,
  cl.Settlement_Amount,

  COALESCE(cl.Claim_Amount, 0)
    - COALESCE(cl.Settlement_Amount, 0)
    AS Outstanding_Claim_Amount,

  cl.Fraud_Flag,
  cl.Settlement_Gap,

  c.Customer_Type,
  c.Customer_Segment,
  c.Emirate,

  pr.Product_Name,
  pr.Product_Category,
  pr.Risk_Level

FROM `insuranceanalytics.insurance_analytics.fact_claim` cl

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_customer` c
  ON cl.Customer_ID = c.Customer_ID

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_product` pr
  ON cl.Product_ID = pr.Product_ID