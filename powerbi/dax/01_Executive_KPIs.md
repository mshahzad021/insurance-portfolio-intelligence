# Executive KPI Measures

This document defines the core executive measures used on the Executive Portfolio dashboard.

> Column names should match the final Power BI semantic model.

---

## Gross Written Premium

### Business Definition

Total premium generated from insurance policies.

### DAX Pattern

```DAX
Gross Written Premium =
SUM(fact_policy[Premium_Amount])