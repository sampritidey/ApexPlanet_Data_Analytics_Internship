# ApexPlanet Data Analytics Internship – Task 4

## Data Storytelling & Statistical Validation

---

## 1. Project Overview

This project is part of the **ApexPlanet Data Analytics Internship**.

Task 4 focuses on bringing together the findings from the previous tasks and presenting them as a clear business story. It also applies statistical analysis to validate an important business finding from the customer segmentation analysis.

The project combines:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Customer Segmentation
* Statistical Hypothesis Testing
* Business Insights
* Data Storytelling
* Interactive Dashboarding
* Business Recommendations

The main objective is to move from simply describing the data to using statistical evidence to support business conclusions.

---

# 2. Project Objectives

The main objectives of Task 4 are:

1. Combine the important findings from Tasks 1, 2, and 3.
2. Present the analysis as a clear business story.
3. Formulate a testable business hypothesis.
4. Select an appropriate statistical test.
5. Perform statistical hypothesis testing.
6. Interpret the p-value.
7. Interpret confidence intervals.
8. Determine whether customer segments show statistically significant differences.
9. Translate statistical findings into business insights.
10. Provide practical business recommendations.
11. Present the complete analysis in a professional presentation.

---

# 3. Project Journey

The complete internship project follows this analytical workflow:

```text
Raw Data
   ↓
Task 1 – Data Cleaning
   ↓
Task 2 – Exploratory Data Analysis
   ↓
Task 3 – Customer Segmentation
   ↓
Task 4 – Statistical Validation & Data Storytelling
   ↓
Business Insights & Recommendations
```

Each task builds on the previous task.

---

# 4. Task 1 – Data Cleaning

Task 1 focused on preparing the raw dataset for further analysis.

The main data-cleaning activities included:

* Loading the dataset.
* Inspecting the dataset structure.
* Checking data types.
* Identifying missing values.
* Checking duplicate records.
* Checking inconsistent values.
* Converting columns into appropriate formats.
* Preparing the cleaned dataset for analysis.
* Exporting the cleaned dataset into Excel format.

The cleaned dataset was then used for the following tasks.

---

# 5. Task 2 – Exploratory Data Analysis

Task 2 focused on understanding sales and customer behaviour using exploratory data analysis.

The analysis included:

* Total sales by category.
* Total sales by city.
* Total quantity sold by product.
* Monthly sales analysis.
* Sales by gender.
* Average unit price by product.
* Identification of high-performing categories.
* Identification of high-performing cities.
* Identification of high-performing products.
* Analysis of relationships between numerical variables.

### Key findings from Task 2

### Highest-Selling Category

**Electronics** generated the highest total sales.

Total sales:

**₹50,778,581.70**

### Highest-Sales City

**Patna** recorded the highest total sales.

Total sales:

**₹19,285,966.89**

The exploratory analysis helped identify important sales patterns that were later used to support the customer segmentation analysis.

---

# 6. Task 3 – Customer Segmentation

Task 3 focused on grouping customers according to their purchasing behaviour.

The segmentation was performed using the **K-Means Clustering** algorithm.

The customer-level dataset contained **947 customers**.

The clustering analysis used customer behavioural features such as:

* Total Spending
* Total Quantity
* Number of Orders
* Average Order Value

The numerical features were standardized using **StandardScaler** before applying K-Means.

The number of clusters was selected using clustering evaluation methods including the **Silhouette Score**.

---

# 7. Customer Segments

The customer segmentation analysis produced three main clusters:

* Cluster 0
* Cluster 1
* Cluster 2

The segments showed different purchasing characteristics.

### Cluster 0

* Customers: **613**
* Total Spending: approximately **₹45.41 million**
* Average Spending per Customer: approximately **₹74.07 thousand**

Cluster 0 contains the largest number of customers.

---

### Cluster 1

* Customers: **282**
* Total Spending: approximately **₹77.82 million**
* Average Spending per Customer: approximately **₹275.96 thousand**

Cluster 1 generated the highest total spending among the three segments.

---

### Cluster 2

* Customers: **52**
* Total Spending: approximately **₹16.17 million**
* Average Spending per Customer: approximately **₹311.03 thousand**

Cluster 2 contains the smallest number of customers but has a high average spending per customer.

---

# 8. Important Task 3 Business Findings

The customer segmentation analysis identified several important findings.

### Segment with the highest number of customers

**Cluster 0**

Number of customers:

**613**

---

### Segment with the highest total spending

**Cluster 1**

Total spending:

**₹77,820,568.67**

---

### Segment with the highest average order value

**Cluster 1**

Average Order Value:

**₹278,926.77**

---

### Highest-Selling Category

**Electronics**

Total sales:

**₹50,778,581.70**

---

### Highest-Sales City

**Patna**

Total sales:

**₹19,285,966.89**

---

### Cluster 1 – Strongest Category

The strongest category for Cluster 1 was:

**Electronics**

Sales:

**₹28,820,495.16**

---

### Cluster 1 – Highest-Sales City

The city generating the highest sales for Cluster 1 was:

**Bengaluru**

Sales:

**₹12,204,439.65**

---

# 9. Interactive Dashboard

An interactive dashboard was created using **Looker Studio**.

The dashboard contains two major sections:

### Page 1 – Executive Dashboard

The executive dashboard provides an overall view of:

* Total Sales
* Customer Count
* Total Quantity
* Average Order Value
* Sales by Category
* Sales by City
* Sales trends

### Page 2 – Customer Segmentation Analysis

The segmentation dashboard provides:

* Customer count by segment.
* Spending by segment.
* Average spending by segment.
* Category performance by segment.
* City performance by segment.
* Customer segment comparisons.

### Dashboard Filters

Interactive filters include:

* Customer Segment
* Category
* City
* Gender
* Date Range

### Looker Studio Dashboard

Dashboard link:

https://datastudio.google.com/reporting/b951b80e-a4d5-4e9f-b801-4788e98671ff

---

# 10. Task 4 – Data Storytelling & Statistical Validation

Task 4 focuses on validating one of the important findings from the customer segmentation analysis.

The main business question is:

> **Do customer segments have statistically significant differences in customer spending?**

This question is important because the segmentation analysis showed clear differences in spending behaviour between customer groups.

Statistical testing helps determine whether these observed differences are statistically significant.

---

# 11. Business Hypothesis

The following hypotheses were formulated.

### Null Hypothesis (H₀)

There is **no statistically significant difference** in customer spending among the different customer segments.

In simple terms:

> Customer segments have similar spending behaviour.

---

### Alternative Hypothesis (H₁)

There is a **statistically significant difference** in customer spending among the different customer segments.

In simple terms:

> At least one customer segment has different spending behaviour.

---

# 12. Significance Level

The significance level was set to:

**α = 0.05**

This means that the analysis uses a 5% significance threshold.

Decision rule:

```text
If p-value < 0.05
        ↓
Reject H₀

If p-value ≥ 0.05
        ↓
Fail to reject H₀
```

---

# 13. Why Statistical Testing Was Required

The customer segmentation analysis showed differences in spending between clusters.

However, a difference in sample averages alone does not necessarily prove that the difference is statistically meaningful.

Statistical testing helps determine whether the observed differences are likely to represent genuine differences in customer behaviour rather than random variation in the sample.

---

# 14. Statistical Method

Customer spending data can be highly skewed because a small number of customers may have very large spending values.

In addition, the variance of spending can differ substantially between customer segments.

Therefore, a **non-parametric Kruskal–Wallis test** was used as the primary statistical test.

The Kruskal–Wallis test is appropriate when:

* There are more than two independent groups.
* The dependent variable is numerical.
* The data may not satisfy normality assumptions.
* Group variances may be different.

The three customer segments were treated as independent groups.

---

# 15. Variance Check

A variance check was performed before selecting the final statistical test.

The **Levene's test** indicated a very small p-value:

**p ≈ 2.57 × 10⁻⁵⁹**

This is far below the significance level of 0.05.

Therefore, the equal-variance assumption was not supported.

This provided additional justification for using a non-parametric approach rather than relying only on a standard one-way ANOVA.

---

# 16. Kruskal–Wallis Test Result

The Kruskal–Wallis test produced approximately:

**H-statistic = 600.52**

**p-value ≈ 3.97 × 10⁻¹³¹**

Since:

```text
p-value < 0.05
```

the null hypothesis was rejected.

### Statistical conclusion

There is strong statistical evidence that customer spending differs across the customer segments.

This supports the business finding that customer segments have different spending behaviour.

---

# 17. Pairwise Statistical Testing

The overall Kruskal–Wallis test tells us that at least one group differs from another.

To investigate which groups differ, pairwise **Mann–Whitney U tests** were performed.

The results were:

| Segment Comparison     | Approx. p-value | Result                        |
| ---------------------- | --------------: | ----------------------------- |
| Cluster 0 vs Cluster 1 |   1.18 × 10⁻¹²⁴ | Significant                   |
| Cluster 0 vs Cluster 2 |    4.46 × 10⁻²³ | Significant                   |
| Cluster 1 vs Cluster 2 |           0.556 | Not statistically significant |

These results indicate that:

* Cluster 0 differs significantly from Cluster 1.
* Cluster 0 differs significantly from Cluster 2.
* The difference between Cluster 1 and Cluster 2 was not statistically significant at the 5% level.

---

# 18. Confidence Intervals

Bootstrap confidence intervals were used to estimate the uncertainty around differences in average spending.

A 95% confidence interval was used.

### Cluster 0 vs Cluster 1

Approximate mean difference:

**−₹201.9K**

95% confidence interval:

**−₹212.6K to −₹191.2K**

The interval does not include zero.

---

### Cluster 0 vs Cluster 2

Approximate mean difference:

**−₹237.0K**

95% confidence interval:

**−₹287.9K to −₹188.1K**

The interval does not include zero.

---

### Cluster 1 vs Cluster 2

Approximate mean difference:

**−₹35.1K**

95% confidence interval:

**−₹88.1K to ₹15.5K**

The interval includes zero.

This is consistent with the pairwise statistical test, which did not find a statistically significant difference between Cluster 1 and Cluster 2.

---

# 19. Interpretation of the Statistical Results

The statistical analysis provides evidence that customer spending behaviour is not the same across all customer segments.

The strongest evidence of difference was observed when comparing:

* Cluster 0 and Cluster 1
* Cluster 0 and Cluster 2

However, the comparison between Cluster 1 and Cluster 2 did not show a statistically significant difference at the 5% level.

This demonstrates why statistical validation is useful: visual differences in a dashboard can be investigated using formal statistical methods.

---

# 20. Business Insights

The combined analysis from Tasks 1–4 provides several business insights.

### Insight 1 – Customer segments have different spending behaviour

The statistical test provides strong evidence that spending differs across customer segments.

Therefore, customers should not necessarily be treated as one homogeneous group.

---

### Insight 2 – Cluster 0 represents the largest customer population

Cluster 0 contains the highest number of customers.

This makes it an important segment from a customer-reach perspective.

---

### Insight 3 – Cluster 1 generates the highest total spending

Cluster 1 generated approximately:

**₹77.82 million**

in total spending.

This makes Cluster 1 important from a total-revenue perspective.

---

### Insight 4 – Cluster 2 has a small customer base but high spending per customer

Cluster 2 contains only 52 customers, but its average spending per customer is high.

This suggests that a small customer segment can still have substantial business value.

---

### Insight 5 – Electronics is the strongest category

Electronics generated the highest overall sales.

It also performed particularly strongly within Cluster 1.

---

### Insight 6 – Customer behaviour varies by segment

Different customer groups show different purchasing characteristics.

This supports the use of targeted customer strategies instead of treating all customers in exactly the same way.

---

# 21. Business Recommendations

Based on the combined analysis, the following recommendations can be considered.

### Recommendation 1 – Develop segment-specific strategies

Different customer segments demonstrate different purchasing behaviour.

Therefore, marketing campaigns and offers can be customized according to customer segment.

---

### Recommendation 2 – Focus retention efforts on high-value customers

Segments with high spending levels can be targeted with:

* Loyalty programs
* Personalized offers
* Premium products
* Early-access promotions
* Cross-selling opportunities

---

### Recommendation 3 – Increase engagement with the largest segment

Cluster 0 contains the largest number of customers.

Targeted campaigns can be used to increase:

* Purchase frequency
* Average order value
* Customer retention
* Cross-category purchases

---

### Recommendation 4 – Promote high-performing categories

Electronics is the highest-selling category.

Businesses can consider:

* Cross-selling electronics-related products.
* Creating bundles.
* Offering personalized recommendations.
* Running targeted promotions.

---

### Recommendation 5 – Use statistical validation for business decisions

Statistical testing should be used alongside dashboard analysis.

This helps distinguish between:

* Observed differences
* Statistically supported differences
* Differences that may require further investigation

---

# 22. Tools and Technologies Used

The project used the following tools and technologies:

### Python

Used for:

* Data cleaning
* Data analysis
* Customer aggregation
* K-Means clustering
* Statistical testing
* Visualization

### Pandas

Used for:

* Data manipulation
* Data cleaning
* Grouping
* Aggregation

### NumPy

Used for:

* Numerical calculations
* Statistical analysis

### Scikit-learn

Used for:

* Feature scaling
* K-Means clustering
* Silhouette score analysis

### SciPy

Used for:

* Levene's test
* Kruskal–Wallis test
* Mann–Whitney U test

### Matplotlib / Seaborn

Used for:

* Data visualization
* Distribution plots
* Segment comparisons

### Excel

Used for:

* Dataset storage
* Statistical results
* Analysis outputs

### Looker Studio

Used for:

* Interactive dashboard creation
* Business visualization
* Customer segmentation analysis

### GitHub

Used for:

* Version control
* Project documentation
* Deliverable submission

---

# 23. Repository Structure

The Task 4 folder contains the following files:

```text
Task4/
│
├── README.md
│
├── Final_Presentation.pptx
│
├── Hypothesis_Testing_Summary.pdf
│
├── Task4_Statistical_Results.xlsx
│
├── Hypothesis_Testing.py
│
└── Screenshots/
    ├── spending_by_segment.png
    ├── spending_distribution.png
    ├── statistical_results.png
    └── dashboard.png
```

---

# 24. Task 4 Deliverables

The main deliverables for Task 4 are:

### 1. Final Presentation

`Final_Presentation.pptx`

The presentation summarizes:

* Project journey
* Business problem
* Customer segmentation
* Hypothesis
* Statistical methodology
* Statistical results
* Confidence intervals
* Business insights
* Recommendations
* Conclusion

---

### 2. Hypothesis Testing Summary

`Hypothesis_Testing_Summary.pdf`

This report documents:

* Business question
* Null hypothesis
* Alternative hypothesis
* Significance level
* Statistical methodology
* Variance testing
* Kruskal–Wallis test
* Pairwise testing
* Confidence intervals
* Interpretation
* Business conclusions

---

### 3. Statistical Results

`Task4_Statistical_Results.xlsx`

This file contains the statistical analysis results and supporting calculations.

---

### 4. Python Code

`Hypothesis_Testing.py`

This file contains the Python code used to perform the statistical analysis.

---

# 25. Limitations

The analysis has some limitations:

1. The results are based on the available dataset.
2. Statistical significance does not automatically imply business causation.
3. Customer spending can be highly skewed.
4. The analysis identifies differences between segments but does not establish why those differences occur.
5. Additional variables could be included in future analysis.
6. The results should be combined with business context before making operational decisions.

---

# 26. Future Scope

Future analysis could include:

* Customer Lifetime Value prediction.
* Churn prediction.
* Purchase frequency prediction.
* Recommendation systems.
* Customer response prediction.
* Time-series sales forecasting.
* Advanced customer segmentation.
* A/B testing of marketing campaigns.
* Predictive analytics.
* Machine learning-based customer targeting.

---

# 27. Final Conclusion

Task 4 combines the findings from data cleaning, exploratory analysis, customer segmentation, and statistical validation into one complete business story.

The customer segmentation analysis identified three distinct customer groups with different purchasing characteristics.

Statistical testing provided strong evidence that customer spending differs across customer segments. The overall Kruskal–Wallis test produced a very small p-value, leading to rejection of the null hypothesis at the 5% significance level.

Pairwise testing further showed statistically significant differences between Cluster 0 and the other two clusters, while the difference between Cluster 1 and Cluster 2 was not statistically significant at the 5% level.

The analysis demonstrates how data analytics can move beyond simple visualization and use statistical evidence to support business understanding.

The final outcome combines:

```text
Data Cleaning
      ↓
Exploratory Analysis
      ↓
Customer Segmentation
      ↓
Statistical Validation
      ↓
Business Insights
      ↓
Business Recommendations
```

This provides a complete data-driven approach to understanding customer behaviour and supporting business decision-making.

---

# 28. Author

**ApexPlanet Data Analytics Internship**

**Task 4 – Data Storytelling & Statistical Validation**

---

## Project Status

**Task 4 Completed**

**Internship Project: ApexPlanet Data Analytics**
