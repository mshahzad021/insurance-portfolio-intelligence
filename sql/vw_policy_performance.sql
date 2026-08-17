SELECT
  p.Policy_ID,
  p.Customer_ID,
  p.Product_ID,

  c.Customer_Type,
  c.Customer_Segment,
  c.Gender,
  c.Age,
  c.Nationality,
  c.Emirate,
  c.Industry,
  c.Company_Size,
  c.Acquisition_Channel,

  pr.Product_Name,
  pr.Product_Category,
  pr.Risk_Level,

  p.Policy_Start_Date,
  p.Policy_End_Date,
  p.Policy_Status,
  p.Premium,
  p.Sum_Insured,
  p.Payment_Frequency,
  p.Sales_Channel,
  p.Policy_Tenure_Months,
  p.Cancellation_Flag,

  p.Policy_Year,

  CASE
    WHEN p.Policy_Status = 'Active' THEN 1
    ELSE 0
  END AS Active_Policy_Flag,

  CASE
    WHEN p.Policy_Status = 'Cancelled' THEN 1
    ELSE 0
  END AS Cancelled_Policy_Flag

FROM `insuranceanalytics.insurance_analytics.fact_policy` p

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_customer` c
  ON p.Customer_ID = c.Customer_ID

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_product` pr
  ON p.Product_ID = pr.Product_ID