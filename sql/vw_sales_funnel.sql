SELECT

  -- LEAD IDENTIFICATION
  l.Lead_ID,

  l.Customer_ID,

  l.Lead_Date,

  -- DATE ATTRIBUTES
  EXTRACT(YEAR FROM l.Lead_Date) AS lead_year,

  EXTRACT(MONTH FROM l.Lead_Date) AS lead_month,

  FORMAT_DATE(
    '%Y-%m',
    l.Lead_Date
  ) AS year_month,

  -- LEAD ATTRIBUTES
  l.Lead_Source,

  l.Product_Interest,

  l.Lead_Status,

  l.Quoted_Premium,

  -- SOURCE CONVERSION FLAG
  l.Converted_Flag AS source_converted_flag,

  -- FUNNEL STAGE FLAGS
  CASE
    WHEN l.Lead_Status = 'New'
      THEN 1
    ELSE 0
  END AS new_lead_flag,

  CASE
    WHEN l.Lead_Status = 'Contacted'
      THEN 1
    ELSE 0
  END AS contacted_flag,

  CASE
    WHEN l.Lead_Status = 'Qualified'
      THEN 1
    ELSE 0
  END AS qualified_flag,

  CASE
    WHEN l.Lead_Status = 'Quoted'
      THEN 1
    ELSE 0
  END AS quoted_flag,

  CASE
    WHEN l.Converted_Flag = 1
      OR l.Lead_Status = 'Converted'
      THEN 1
    ELSE 0
  END AS converted_flag,

  CASE
    WHEN l.Lead_Status = 'Lost'
      THEN 1
    ELSE 0
  END AS lost_flag,

  -- CUSTOMER ATTRIBUTES
  c.Customer_Type,

  c.Customer_Segment,

  c.Emirate,

  c.Acquisition_Channel

FROM
  `insuranceanalytics.insurance_analytics.fact_lead` l

LEFT JOIN
  `insuranceanalytics.insurance_analytics.dim_customer` c

ON
  l.Customer_ID = c.Customer_ID