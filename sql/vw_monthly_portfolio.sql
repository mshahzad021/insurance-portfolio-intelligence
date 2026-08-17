WITH months AS (

  SELECT DISTINCT
    DATE_TRUNC(date, MONTH) AS month_start
  FROM `insuranceanalytics.insurance_analytics.dim_date`

),

policy_monthly AS (

  SELECT
    DATE_TRUNC(Policy_Start_Date, MONTH) AS month_start,

    COUNT(DISTINCT Policy_ID) AS new_policies,

    SUM(Premium) AS gross_written_premium,

    COUNTIF(Policy_Status = 'Cancelled') AS cancelled_policies

  FROM `insuranceanalytics.insurance_analytics.fact_policy`

  GROUP BY month_start

),

claim_monthly AS (

  SELECT
    DATE_TRUNC(Claim_Date, MONTH) AS month_start,

    COUNT(DISTINCT Claim_ID) AS claims,

    SUM(Claim_Amount) AS claim_amount,

    SUM(Settlement_Amount) AS settlement_amount

  FROM `insuranceanalytics.insurance_analytics.fact_claim`

  GROUP BY month_start

),

payment_monthly AS (

  SELECT
    DATE_TRUNC(Payment_Date, MONTH) AS month_start,

    SUM(Due_Amount) AS premium_billed,

    SUM(Paid_Amount) AS premium_collected,

    SUM(Outstanding_Amount) AS outstanding_premium

  FROM `insuranceanalytics.insurance_analytics.fact_payment`

  GROUP BY month_start

),

renewal_monthly AS (

  SELECT
    DATE_TRUNC(Renewal_Date, MONTH) AS month_start,

    COUNT(DISTINCT Renewal_ID) AS renewal_opportunities,

    COUNTIF(Renewed_Flag = 1) AS renewed_policies

  FROM `insuranceanalytics.insurance_analytics.fact_renewal`

  GROUP BY month_start

)

SELECT

  m.month_start,

  EXTRACT(YEAR FROM m.month_start) AS year,

  EXTRACT(MONTH FROM m.month_start) AS month,

  FORMAT_DATE('%Y-%m', m.month_start) AS year_month,

  COALESCE(p.new_policies, 0) AS new_policies,

  COALESCE(p.gross_written_premium, 0)
    AS gross_written_premium,

  COALESCE(p.cancelled_policies, 0)
    AS cancelled_policies,

  COALESCE(c.claims, 0) AS claims,

  COALESCE(c.claim_amount, 0) AS claim_amount,

  COALESCE(c.settlement_amount, 0)
    AS settlement_amount,

  COALESCE(pay.premium_billed, 0)
    AS premium_billed,

  COALESCE(pay.premium_collected, 0)
    AS premium_collected,

  COALESCE(pay.outstanding_premium, 0)
    AS outstanding_premium,

  COALESCE(r.renewal_opportunities, 0)
    AS renewal_opportunities,

  COALESCE(r.renewed_policies, 0)
    AS renewed_policies,

  SAFE_DIVIDE(
    r.renewed_policies,
    r.renewal_opportunities
  ) * 100 AS renewal_rate,

  SAFE_DIVIDE(
    c.claim_amount,
    p.gross_written_premium
  ) * 100 AS loss_ratio_proxy,

  SAFE_DIVIDE(
    pay.premium_collected,
    pay.premium_billed
  ) * 100 AS collection_rate

FROM months m

LEFT JOIN policy_monthly p
  ON m.month_start = p.month_start

LEFT JOIN claim_monthly c
  ON m.month_start = c.month_start

LEFT JOIN payment_monthly pay
  ON m.month_start = pay.month_start

LEFT JOIN renewal_monthly r
  ON m.month_start = r.month_start