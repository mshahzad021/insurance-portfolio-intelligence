SELECT

  p.Payment_ID,

  p.Policy_ID,

  p.Customer_ID,

  p.Payment_Date,

  p.Payment_Due_Date,

  p.Payment_Status,

  p.Payment_Method,

  p.Due_Amount,

  p.Paid_Amount,

  p.Outstanding_Amount,

  p.Payment_Delay_Days,

  pol.Product_ID,

  pr.Product_Name,

  pr.Product_Category,

  c.Customer_Type,

  c.Customer_Segment,

  c.Emirate,

  c.Acquisition_Channel,

  CASE
    WHEN p.Payment_Status = 'Paid'
      THEN 1
    ELSE 0
  END AS paid_flag,

  CASE
    WHEN p.Payment_Status = 'Pending'
      THEN 1
    ELSE 0
  END AS pending_flag,

  CASE
    WHEN p.Payment_Status = 'Overdue'
      THEN 1
    ELSE 0
  END AS overdue_flag,

  CASE
    WHEN p.Payment_Status = 'Failed'
      THEN 1
    ELSE 0
  END AS failed_flag,

  CASE
    WHEN p.Payment_Delay_Days > 0
      THEN 1
    ELSE 0
  END AS late_payment_flag,

  SAFE_DIVIDE(
    p.Paid_Amount,
    p.Due_Amount
  ) * 100 AS transaction_collection_rate

FROM `insuranceanalytics.insurance_analytics.fact_payment` p

LEFT JOIN `insuranceanalytics.insurance_analytics.fact_policy` pol
  ON p.Policy_ID = pol.Policy_ID

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_product` pr
  ON pol.Product_ID = pr.Product_ID

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_customer` c
  ON p.Customer_ID = c.Customer_ID