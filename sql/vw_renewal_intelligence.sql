SELECT

  r.Renewal_ID,

  r.Policy_ID,

  r.Customer_ID,

  r.Product_ID,

  r.Expiry_Date,

  r.Renewal_Date,

  r.Renewal_Status,

  r.Renewed_Flag,

  r.Previous_Premium,

  r.New_Premium,

  r.Premium_Change,

  r.`Premium_Change_%` AS premium_change_pct,

  r.Renewal_Lead_Days,

  c.Customer_Type,

  c.Customer_Segment,

  c.Emirate,

  c.Acquisition_Channel,

  pr.Product_Name,

  pr.Product_Category,

  pr.Risk_Level,

  CASE
    WHEN r.Renewed_Flag = 1
      THEN 'Retained'

    WHEN r.Renewal_Status = 'Lost to Competitor'
      THEN 'Lost to Competitor'

    WHEN r.Renewal_Status = 'Customer Cancelled'
      THEN 'Customer Cancelled'

    WHEN r.Renewal_Status = 'Not Renewed'
      THEN 'Not Renewed'

    ELSE 'Unknown'
  END AS retention_outcome,

  CASE
    WHEN r.Renewed_Flag = 1
      THEN 'Low'

    WHEN r.Renewal_Status = 'Lost to Competitor'
      THEN 'High'

    WHEN r.Renewal_Status = 'Customer Cancelled'
      THEN 'High'

    WHEN r.Renewal_Status = 'Not Renewed'
         AND COALESCE(r.`Premium_Change_%`, 0) >= 15
      THEN 'High'

    WHEN r.Renewal_Status = 'Not Renewed'
      THEN 'Medium'

    ELSE 'Low'
  END AS renewal_risk,

  CASE
    WHEN r.Renewal_Lead_Days < 15
      THEN 'Urgent'

    WHEN r.Renewal_Lead_Days < 30
      THEN 'High'

    WHEN r.Renewal_Lead_Days < 60
      THEN 'Medium'

    ELSE 'Planned'
  END AS renewal_timing

FROM `insuranceanalytics.insurance_analytics.fact_renewal` r

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_customer` c
  ON r.Customer_ID = c.Customer_ID

LEFT JOIN `insuranceanalytics.insurance_analytics.dim_product` pr
  ON r.Product_ID = pr.Product_ID