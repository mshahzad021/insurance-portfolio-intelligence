WITH policy AS (

  SELECT
    COUNT(DISTINCT Policy_ID) AS total_policies,

    COUNTIF(Policy_Status = 'Active') AS active_policies,

    COUNTIF(Policy_Status = 'Expired') AS expired_policies,

    COUNTIF(Policy_Status = 'Cancelled') AS cancelled_policies,

    COALESCE(SUM(Premium), 0) AS gross_written_premium,

    COALESCE(AVG(Premium), 0) AS average_premium,

    COALESCE(SUM(Sum_Insured), 0) AS total_sum_insured

  FROM `insuranceanalytics.insurance_analytics.fact_policy`

),

customer AS (

  SELECT
    COUNT(DISTINCT Customer_ID) AS total_customers

  FROM `insuranceanalytics.insurance_analytics.dim_customer`

),

claims AS (

  SELECT
    COUNT(DISTINCT Claim_ID) AS total_claims,

    COALESCE(SUM(Claim_Amount), 0) AS total_claim_amount,

    COALESCE(SUM(Settlement_Amount), 0) AS total_settlement_amount,

    COALESCE(
      SUM(
        COALESCE(Claim_Amount, 0)
        - COALESCE(Settlement_Amount, 0)
      ),
      0
    ) AS outstanding_claim_amount,

    COUNTIF(Fraud_Flag = 1) AS fraud_flagged_claims

  FROM `insuranceanalytics.insurance_analytics.fact_claim`

),

renewals AS (

  SELECT

    COUNT(DISTINCT Renewal_ID) AS renewal_opportunities,

    COUNTIF(Renewed_Flag = 1) AS renewed_policies,

    COUNTIF(Renewed_Flag = 0) AS not_renewed_policies

  FROM `insuranceanalytics.insurance_analytics.fact_renewal`

),

payments AS (

  SELECT

    COALESCE(SUM(Due_Amount), 0) AS premium_billed,

    COALESCE(SUM(Paid_Amount), 0) AS premium_collected,

    COALESCE(SUM(Outstanding_Amount), 0) AS outstanding_premium,

    COUNTIF(Payment_Status = 'Paid') AS paid_transactions,

    COUNTIF(Payment_Status = 'Overdue') AS overdue_transactions,

    COUNTIF(Payment_Status = 'Failed') AS failed_transactions,

    COUNT(*) AS total_payment_transactions

  FROM `insuranceanalytics.insurance_analytics.fact_payment`

),

leads AS (

  SELECT

    COUNT(DISTINCT Lead_ID) AS total_leads,

    COUNTIF(Lead_Status = 'Qualified') AS qualified_leads,

    COUNTIF(Lead_Status = 'Quoted') AS quoted_leads,

    COUNTIF(Converted_Flag = 1) AS converted_leads,

    COALESCE(SUM(Quoted_Premium), 0) AS quoted_premium

  FROM `insuranceanalytics.insurance_analytics.fact_lead`

)

SELECT

  CURRENT_DATE() AS metric_date,

  -- POLICY KPIs
  p.total_policies,

  p.active_policies,

  p.expired_policies,

  p.cancelled_policies,

  p.gross_written_premium,

  p.average_premium,

  p.total_sum_insured,

  -- CUSTOMER KPIs
  c.total_customers,

  -- CLAIM KPIs
  cl.total_claims,

  cl.total_claim_amount,

  cl.total_settlement_amount,

  cl.outstanding_claim_amount,

  cl.fraud_flagged_claims,

  -- RENEWAL KPIs
  r.renewal_opportunities,

  r.renewed_policies,

  r.not_renewed_policies,

  SAFE_DIVIDE(
    r.renewed_policies,
    r.renewal_opportunities
  ) * 100 AS renewal_rate,

  -- CLAIM / RISK KPIs
  SAFE_DIVIDE(
    cl.total_claim_amount,
    p.gross_written_premium
  ) * 100 AS loss_ratio_proxy,

  SAFE_DIVIDE(
    cl.total_claims,
    p.total_policies
  ) * 100 AS claim_frequency,

  SAFE_DIVIDE(
    cl.total_claim_amount,
    cl.total_claims
  ) AS claim_severity,

  -- PAYMENT KPIs
  pay.premium_billed,

  pay.premium_collected,

  pay.outstanding_premium,

  SAFE_DIVIDE(
    pay.premium_collected,
    pay.premium_billed
  ) * 100 AS collection_rate,

  pay.paid_transactions,

  pay.overdue_transactions,

  pay.failed_transactions,

  SAFE_DIVIDE(
    pay.overdue_transactions,
    pay.total_payment_transactions
  ) * 100 AS overdue_rate,

  -- LEAD / ACQUISITION KPIs
  l.total_leads,

  l.qualified_leads,

  l.quoted_leads,

  l.converted_leads,

  l.quoted_premium,

  SAFE_DIVIDE(
    l.converted_leads,
    l.total_leads
  ) * 100 AS lead_conversion_rate

FROM policy p

CROSS JOIN customer c

CROSS JOIN claims cl

CROSS JOIN renewals r

CROSS JOIN payments pay

CROSS JOIN leads l