WITH policies AS (

  SELECT
    Product_ID,
    COUNT(DISTINCT Policy_ID) AS policies,
    COUNT(DISTINCT Customer_ID) AS customers,
    SUM(Premium) AS gross_written_premium,

    COUNTIF(Policy_Status = 'Active') AS active_policies,
    COUNTIF(Cancellation_Flag = 1) AS cancelled_policies

  FROM `insuranceanalytics.insurance_analytics.fact_policy`

  GROUP BY Product_ID

),

claims AS (

  SELECT
    Product_ID,
    COUNT(DISTINCT Claim_ID) AS claims,
    SUM(Claim_Amount) AS claim_amount,
    SUM(Settlement_Amount) AS settlement_amount
  FROM `insuranceanalytics.insurance_analytics.fact_claim`

  GROUP BY Product_ID

),

renewals AS (

  SELECT
    Product_ID,
    COUNT(DISTINCT Renewal_ID) AS renewal_opportunities,
    COUNTIF(Renewed_Flag = 1) AS renewed_policies
  FROM `insuranceanalytics.insurance_analytics.fact_renewal`

  GROUP BY Product_ID

)

SELECT

  pr.Product_ID,
  pr.Product_Name,
  pr.Product_Category,
  pr.Target_Customer,
  pr.Risk_Level,

  COALESCE(p.policies, 0) AS policies,
  COALESCE(p.active_policies, 0) AS active_policies,
  COALESCE(p.customers, 0) AS customers,

  COALESCE(p.gross_written_premium, 0) AS gross_written_premium,

  COALESCE(cl.claims, 0) AS claims,
  COALESCE(cl.claim_amount, 0) AS claim_amount,
  COALESCE(cl.settlement_amount, 0) AS settlement_amount,

  COALESCE(r.renewal_opportunities, 0)
    AS renewal_opportunities,

  COALESCE(r.renewed_policies, 0)
    AS renewed_policies,

  SAFE_DIVIDE(
    cl.claim_amount,
    p.gross_written_premium
  ) * 100 AS loss_ratio,

  SAFE_DIVIDE(
    cl.claims,
    p.policies
  ) * 100 AS claims_frequency,

  SAFE_DIVIDE(
    cl.claim_amount,
    cl.claims
  ) AS claims_severity,

  SAFE_DIVIDE(
    r.renewed_policies,
    r.renewal_opportunities
  ) * 100 AS renewal_rate,

  SAFE_DIVIDE(
    p.gross_written_premium,
    p.policies
  ) AS average_premium

FROM `insuranceanalytics.insurance_analytics.dim_product` pr

LEFT JOIN policies p
  ON pr.Product_ID = p.Product_ID

LEFT JOIN claims cl
  ON pr.Product_ID = cl.Product_ID

LEFT JOIN renewals r
  ON pr.Product_ID = r.Product_ID