ApexPlanet Data Analytics Internship – Task 4

Data Storytelling & Statistical Validation

Project Title

Customer Segmentation and Spending Behaviour

1. Project Overview

Task 4 combines the results from Tasks 1, 2 and 3 into a single business story and statistically validates an important finding from customer segmentation.

The main objective is to determine whether customer spending differs significantly across the customer segments identified in Task 3.

The analysis uses customer-level spending data and an appropriate statistical testing approach to interpret the observed differences.

2. Business Objective

The business objective is to:

understand differences in spending across customer segments;

statistically validate whether those differences are meaningful;

interpret p-values and confidence intervals;

convert statistical results into business insights and recommendations.

3. Dataset Overview

The analysis is based on the ApexPlanet cleaned and customer segmentation data.

Metric

Value

Transactions

1,000

Unique Customers

947

Customer Segments

3

Products

6

Categories

5

Cities

9

Analysis Period

1 Jan 2025 – 1 Jan 2026

Important Fields

Customer_ID

Order_ID

Transaction_ID

Order_Date

Gender

Age

City

Product

Category

Quantity

Unit_Price

Total_Sales

Customer_Segment

4. Summary of Previous Tasks

Task 1 – Data Cleaning

The dataset was cleaned and prepared for analysis. Data quality checks included missing values, duplicates and data types.

Task 2 – Exploratory Data Analysis

The cleaned dataset was explored to identify patterns in sales, products, categories, cities, gender and time.

Task 3 – Customer Segmentation

K-Means clustering was used to identify customer segments based on purchasing behaviour.

The main segmentation features were:

Total Spending

Total Quantity Purchased

Number of Orders

Average Order Value

Three customer segments were identified:

Cluster 0

Cluster 1

Cluster 2

5. Business Question

Do customer segments have statistically significant differences in customer spending?

6. Hypotheses

Null Hypothesis (H₀)

There is no statistically significant difference in customer spending among the customer segments.

Alternative Hypothesis (H₁)

There is a statistically significant difference in customer spending among at least some of the customer segments.

Significance Level

α = 0.05

Decision rule:

If p-value < 0.05 → Reject H₀.

If p-value ≥ 0.05 → Fail to reject H₀.

7. Customer-Level Data Preparation

The original data is transaction-level, so the statistical analysis was performed at customer level.

For each customer:

Total Spending = sum of Total_Sales

Total Quantity = sum of Quantity

Number of Orders = number of unique Order_ID values

Average Order Value = Total Spending / Number of Orders

Customer Segment = assigned segment from Task 3

This produced 947 customer-level observations.

8. Descriptive Statistics

Segment

Customers

Total Spending

Average Spending

Cluster 0

613

₹45,405,069.44

₹74,070.26

Cluster 1

282

₹77,820,568.67

₹275,959.46

Cluster 2

52

₹16,173,801.54

₹311,034.64

Observations

Cluster 0 is the largest segment.

Cluster 1 has the highest total segment spending.

Cluster 2 has the highest observed average spending per customer.

Cluster 2 is the smallest segment.

9. Statistical Method

Variance Check

Levene's test was used to check the equality of group variances.

Approximate p-value:

2.57 × 10⁻⁵⁹

This is below 0.05, indicating substantial evidence of unequal variances.

Primary Test

The Kruskal–Wallis H test was selected because the analysis compares three independent groups and the spending data have substantially unequal variances.

Pairwise Test

Pairwise Mann–Whitney U tests were used to identify which segment pairs differed.

10. Overall Statistical Result

Kruskal–Wallis result:

H statistic ≈ 600.52

p-value ≈ 3.97 × 10⁻¹³¹

α = 0.05

Since the p-value is much smaller than 0.05:

Reject H₀.

Interpretation

There is strong statistical evidence that customer spending distributions differ across the customer segments.

11. Pairwise Results

Comparison

Approx. p-value

Result

Cluster 0 vs Cluster 1

1.18 × 10⁻¹²⁴

Significant

Cluster 0 vs Cluster 2

4.46 × 10⁻²³

Significant

Cluster 1 vs Cluster 2

0.556

Not statistically significant

The pairwise results show that Cluster 0 differs significantly from both other clusters. The difference between Cluster 1 and Cluster 2 is not statistically significant at the 5% significance level.

12. 95% Bootstrap Confidence Intervals

Comparison

Mean Difference

95% Bootstrap CI

Cluster 0 − Cluster 1

≈ −₹201,889

≈ −₹212,576 to −₹191,200

Cluster 0 − Cluster 2

≈ −₹236,964

≈ −₹287,880 to −₹188,070

Cluster 1 − Cluster 2

≈ −₹35,075

≈ −₹88,102 to ₹15,490

The first two intervals do not include zero, while the Cluster 1 vs Cluster 2 interval includes zero.

13. Business Insights

Cluster 0 is the largest customer segment.

Cluster 1 contributes the highest total segment spending.

Cluster 2 has the highest observed average spending per customer.

The overall statistical test provides strong evidence that spending distributions differ across segments.

Cluster 0 differs significantly from both Cluster 1 and Cluster 2 in pairwise analysis.

Cluster 1 and Cluster 2 are not statistically significantly different in spending at α = 0.05.

14. Business Recommendations

Recommendation 1 – Increase value from Cluster 0

Cluster 0 contains the majority of customers. The business can investigate cross-selling, upselling, loyalty programs and personalized recommendations to increase value from this large population.

Recommendation 2 – Protect high-value customers

Cluster 2 has the highest observed average spending per customer. Retention and personalized-service strategies can be considered for this smaller high-value segment.

Recommendation 3 – Understand Cluster 1

Cluster 1 generates the highest total segment spending. Further analysis of its products, categories, cities and ordering behaviour can help identify the drivers of its contribution.

Recommendation 4 – Use differentiated strategies

The statistical evidence supports treating the segments as distinct groups for business analysis rather than assuming that all customers behave identically.

15. Limitations

The analysis uses historical observational data and does not establish causation.

The Kruskal–Wallis test identifies distributional differences but does not explain their business causes.

Pairwise results should be interpreted with awareness of multiple-comparison considerations.

Confidence intervals describe uncertainty in the observed sample and do not guarantee future customer behaviour.

16. Tools Used

Python

Pandas

NumPy

SciPy

Matplotlib

Seaborn

Google Colab

Microsoft Excel

Microsoft PowerPoint

GitHub

17. Project Files

Task4/
│
├── README.md
├── Final_Presentation.pptx
├── Hypothesis_Testing_Summary.pdf
├── Task4_Statistical_Results.xlsx
├── Task4_Segment_Statistical_Summary.xlsx
│
├── Python_Code/
│   └── Hypothesis_Testing.py
│
└── Screenshots/
    ├── customer_segment_summary.png
    ├── spending_distribution.png
    ├── spending_by_segment.png
    └── statistical_results.png

18. Conclusion

The Task 4 analysis statistically validates the customer segmentation findings from Task 3.

The Kruskal–Wallis test provides strong evidence that customer spending distributions differ across the three customer segments. Pairwise analysis shows statistically significant differences involving Cluster 0, while the difference between Cluster 1 and Cluster 2 is not statistically significant at the 5% level.

The combined use of descriptive statistics, statistical testing, confidence intervals and business interpretation provides a stronger foundation for customer-focused decision making.
