WITH policy_summary AS (

  SELECT
    Customer_ID,
    COUNT(DISTINCT Policy_ID) AS policy_count,
    COUNTIF(Policy_Status = 'Active') AS active_policy_count,
    SUM(Premium) AS total_premium,
    AVG(Premium) AS average_premium
  FROM `insuranceanalytics.insurance_analytics.fact_policy`
  GROUP BY Customer_ID

),

claim_summary AS (

  SELECT
    Customer_ID,
    COUNT(DISTINCT Claim_ID) AS claim_count,
    SUM(Claim_Amount) AS total_claim_amount,
    SUM(Settlement_Amount) AS total_settlement_amount
  FROM `insuranceanalytics.insurance_analytics.fact_claim`
  GROUP BY Customer_ID

),

payment_summary AS (

  SELECT
    Customer_ID,
    SUM(Due_Amount) AS total_due,
    SUM(Paid_Amount) AS total_paid,
    SUM(Outstanding_Amount) AS total_outstanding,
    COUNTIF(Payment_Delay_Days > 0) AS late_payment_count
  FROM `insuranceanalytics.insurance_analytics.fact_payment`
  GROUP BY Customer_ID

),

interaction_summary AS (

  SELECT
    Customer_ID,
    COUNT(DISTINCT Interaction_ID) AS interaction_count,
    AVG(Satisfaction_Score) AS avg_satisfaction,
    AVG(Response_Time_Hours) AS avg_response_time,
    COUNTIF(Resolved_Flag = 1) AS resolved_interactions
  FROM `insuranceanalytics.insurance_analytics.fact_interaction`
  GROUP BY Customer_ID

),

renewal_summary AS (

  SELECT
    Customer_ID,
    COUNT(DISTINCT Renewal_ID) AS renewal_count,
    COUNTIF(Renewed_Flag = 1) AS renewed_count
  FROM `insuranceanalytics.insurance_analytics.fact_renewal`
  GROUP BY Customer_ID

)

SELECT

  c.Customer_ID,
  c.Customer_Type,
  c.Gender,
  c.Age,
  c.Nationality,
  c.Emirate,
  c.Industry,
  c.Company_Size,
  c.Customer_Segment,
  c.Customer_Since,
  c.Acquisition_Channel,

  COALESCE(p.policy_count, 0) AS policy_count,
  COALESCE(p.active_policy_count, 0) AS active_policy_count,
  COALESCE(p.total_premium, 0) AS total_premium,
  COALESCE(p.average_premium, 0) AS average_premium,

  COALESCE(cl.claim_count, 0) AS claim_count,
  COALESCE(cl.total_claim_amount, 0) AS total_claim_amount,

  COALESCE(pay.total_due, 0) AS total_due,
  COALESCE(pay.total_paid, 0) AS total_paid,
  COALESCE(pay.total_outstanding, 0) AS total_outstanding,
  COALESCE(pay.late_payment_count, 0) AS late_payment_count,

  COALESCE(i.interaction_count, 0) AS interaction_count,
  i.avg_satisfaction,
  i.avg_response_time,

  COALESCE(r.renewal_count, 0) AS renewal_count,
  COALESCE(r.renewed_count, 0) AS renewed_count,

  SAFE_DIVIDE(
    r.renewed_count,
    r.renewal_count
  ) * 100 AS customer_renewal_rate,

  SAFE_DIVIDE(
    pay.total_paid,
    pay.total_due
  ) * 100 AS collection_rate,

  CASE
    WHEN COALESCE(p.policy_count, 0) >= 3
         AND COALESCE(p.total_premium, 0) >= 50000
      THEN 'High Value'

    WHEN COALESCE(cl.claim_count, 0) >= 3
      THEN 'High Claim'

    WHEN COALESCE(pay.late_payment_count, 0) >= 2
      THEN 'Payment Risk'

    WHEN COALESCE(r.renewal_count, 0) > 0
         AND COALESCE(r.renewed_count, 0) = 0
      THEN 'At Risk'

    WHEN DATE_DIFF(
           CURRENT_DATE(),
           c.Customer_Since,
           MONTH
         ) <= 12
      THEN 'New Customer'

    ELSE 'Standard'
  END AS analytical_segment

FROM `insuranceanalytics.insurance_analytics.dim_customer` c

LEFT JOIN policy_summary p
  ON c.Customer_ID = p.Customer_ID

LEFT JOIN claim_summary cl
  ON c.Customer_ID = cl.Customer_ID

LEFT JOIN payment_summary pay
  ON c.Customer_ID = pay.Customer_ID

LEFT JOIN interaction_summary i
  ON c.Customer_ID = i.Customer_ID

LEFT JOIN renewal_summary r
  ON c.Customer_ID = r.Customer_ID