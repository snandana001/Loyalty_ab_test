# 🎯 Loyalty A/B Test: Cashback vs No Offer

## Objective
To test whether offering 10% cashback to new users increases the 30-day repeat purchase rate.

## Dataset
- 10,000 users (5,000 per group)
- Group A: No offer
- Group B: 10% cashback offer
- Binary outcome: Made repeat purchase in 30 days or not

## Key Findings

| Metric | Group A | Group B |
|--------|---------|---------|
| Repeat Rate | 22.4% | 30.6% |
| Lift | +8.2% | ✅ Significant |
| P-value | 0.001 | ✔️ Statistically significant |

## Conclusion
Offering 10% cashback led to a significant **8.2% lift** in repeat purchases (p < 0.01). This suggests the loyalty offer positively influenced early user retention.

> 📊 Recommended Action: Roll out cashback as a controlled feature to more new users while continuing to monitor long-term value.

## Tools Used
- Python (Pandas, SciPy, Seaborn)
- A/B Testing (Z-test for proportions)
- Data Visualization (Matplotlib)

