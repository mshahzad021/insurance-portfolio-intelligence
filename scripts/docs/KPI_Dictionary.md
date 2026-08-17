# UAE Insurance Portfolio Intelligence
## KPI Dictionary

## 1. Portfolio KPIs

### Total Customers
Definition:
Count of unique Customer_ID.

Formula:
COUNT_DISTINCT(Customer_ID)

### Total Policies
Definition:
Count of unique Policy_ID.

Formula:
COUNT_DISTINCT(Policy_ID)

### Gross Written Premium (GWP)
Definition:
Total written policy premium.

Formula:
SUM(Premium)

### Average Premium
Definition:
Average premium per policy.

Formula:
SUM(Premium) / COUNT_DISTINCT(Policy_ID)


## 2. Claims KPIs

### Total Claims
Definition:
Count of unique claims.

Formula:
COUNT_DISTINCT(Claim_ID)

### Total Claim Amount
Definition:
Total reported claim amount.

Formula:
SUM(Claim_Amount)

### Average Claim Severity
Definition:
Average claim amount per claim.

Formula:
SUM(Claim_Amount) / COUNT_DISTINCT(Claim_ID)

### Claim Frequency
Definition:
Number of claims relative to policy exposure.

Primary proxy:
COUNT_DISTINCT(Claim_ID) / COUNT_DISTINCT(Policy_ID)

Note:
This is a policy-count proxy because direct exposure units are not available.

### Settlement Rate
Definition:
Percentage of claim amount settled.

Formula:
SUM(Settlement_Amount) / SUM(Claim_Amount)


## 3. Profitability KPIs

### Loss Ratio
Definition:
Claims relative to premium.

Formula:
SUM(Claim_Amount) / SUM(Premium)

Note:
This is a portfolio proxy, not a formal actuarial earned-premium loss ratio.


## 4. Renewal KPIs

### Eligible Renewals
Definition:
Count of renewal records.

Formula:
COUNT_DISTINCT(Renewal_ID)

### Renewed Policies
Definition:
Number of successful renewals.

Formula:
SUM(Renewed_Flag)

### Renewal Rate
Definition:
Percentage of eligible renewals successfully renewed.

Formula:
SUM(Renewed_Flag) / COUNT_DISTINCT(Renewal_ID)

### Churn Rate
Definition:
Percentage of eligible renewals that were not renewed.

Formula:
1 - Renewal Rate

### Premium Retention
Definition:
New premium retained from renewed policies compared with previous premium.

Formula:
SUM(New_Premium) / SUM(Previous_Premium)


## 5. Payment KPIs

### Total Due Amount
Formula:
SUM(Due_Amount)

### Total Paid Amount
Formula:
SUM(Paid_Amount)

### Outstanding Amount
Formula:
SUM(Outstanding_Amount)

### Collection Rate
Definition:
Percentage of amount due that has been collected.

Formula:
SUM(Paid_Amount) / SUM(Due_Amount)

### Overdue Payment Rate
Definition:
Percentage of payment records marked overdue.

Formula:
COUNT(Payment_ID where Payment_Status = "Overdue")
/
COUNT_DISTINCT(Payment_ID)


## 6. Customer KPIs

### Customer Lifetime Value Proxy
Definition:
Estimated customer value based on observed premium contribution.

Formula:
SUM(Premium) by Customer_ID

Note:
This is an observed-value proxy, not a predictive CLV model.

### Multi-Policy Customer Rate
Definition:
Percentage of customers holding more than one policy.

Formula:
Customers with Policy Count > 1
/
Total Customers


## 7. Lead KPIs

### Total Leads
Formula:
COUNT_DISTINCT(Lead_ID)

### Converted Leads
Formula:
SUM(Converted_Flag)

### Lead Conversion Rate
Formula:
SUM(Converted_Flag) / COUNT_DISTINCT(Lead_ID)

### Quoted Premium
Formula:
SUM(Quoted_Premium)

### Average Quoted Premium
Formula:
SUM(Quoted_Premium) / COUNT_DISTINCT(Lead_ID)


## 8. Interaction KPIs

### Total Interactions
Formula:
COUNT_DISTINCT(Interaction_ID)

### Average Satisfaction Score
Formula:
AVG(Satisfaction_Score)

### Resolution Rate
Formula:
SUM(Resolved_Flag) / COUNT_DISTINCT(Interaction_ID)

### Average Response Time
Formula:
AVG(Response_Time_Hours)