# ApexPlanet Data Analytics Internship – Task 3

## Deep-Dive Analysis & Interactive Dashboarding

### Project Title

**Customer Segmentation Using K-Means Clustering**

---

## 1. Project Overview

This project is part of **Task 3 – Deep-Dive Analysis & Interactive Dashboarding** of the ApexPlanet Data Analytics Internship.

The objective of this task is to perform a deeper analysis of customer purchasing behaviour, identify meaningful customer segments, define important business KPIs, and create an interactive dashboard for business analysis.

For this project, **Customer Segmentation using K-Means Clustering** was selected as the deep-dive analysis area.

The analysis groups customers according to their purchasing behaviour using factors such as:

* Total Spending
* Total Quantity Purchased
* Number of Orders
* Average Order Value

The final results are presented through an interactive **Looker Studio dashboard**.

---

## 2. Objectives

The main objectives of this project are:

1. To understand customer purchasing behaviour.
2. To identify different groups of customers using K-Means clustering.
3. To define and calculate important business KPIs.
4. To compare customer segments based on spending and purchasing patterns.
5. To analyse customer segments across categories, cities, gender, and time.
6. To create an interactive dashboard for exploring the results.
7. To provide useful business insights based on the analysis.

---

## 3. Dataset Overview

The cleaned dataset used for this project contains:

* **1,000 transactions**
* **992 orders**
* **947 customers**
* **6 products**
* **5 categories**
* **9 cities**
* Date range: **1 January 2025 to 1 January 2026**

### Important Dataset Fields

| Field            | Description                   |
| ---------------- | ----------------------------- |
| Customer_ID      | Unique customer identifier    |
| Order_ID         | Unique order identifier       |
| Transaction_ID   | Unique transaction identifier |
| Order_Date       | Date of the order             |
| Gender           | Customer gender               |
| Age              | Customer age                  |
| City             | Customer city                 |
| Product          | Product purchased             |
| Category         | Product category              |
| Quantity         | Quantity purchased            |
| Unit_Price       | Price per unit                |
| Total_Sales      | Total sales amount            |
| Customer_Segment | Customer cluster/segment      |

---

## 4. Deep-Dive Analysis

### Customer Segmentation Using K-Means

Customer segmentation was selected as the deep-dive analysis because customers can have different purchasing behaviours.

The analysis uses K-Means clustering to group customers with similar purchasing characteristics.

The following customer-level features were used:

* Total Spending
* Total Quantity
* Number of Orders
* Average Order Value

The customer-level data was standardized before applying K-Means clustering so that features with different scales could be compared appropriately.

Different values of K were tested and silhouette scores were used to evaluate the clustering results.

---

## 5. Key Performance Indicators

Five major KPIs were used in the dashboard.

| KPI                 | Formula                    | Business Purpose                           |
| ------------------- | -------------------------- | ------------------------------------------ |
| Total Sales         | SUM(Total_Sales)           | Measures overall sales generated           |
| Total Customers     | DISTINCTCOUNT(Customer_ID) | Measures the customer base                 |
| Total Orders        | DISTINCTCOUNT(Order_ID)    | Measures order volume                      |
| Total Quantity      | SUM(Quantity)              | Measures total units sold                  |
| Average Order Value | Total Sales / Total Orders | Measures average value generated per order |

These KPIs provide a high-level view of overall business performance and can also be analysed using the dashboard filters.

---

## 6. K-Means Methodology

The customer segmentation process followed these steps:

### Step 1 – Data Preparation

The cleaned sales dataset was loaded and inspected.

### Step 2 – Customer-Level Aggregation

Transaction-level data was aggregated for each customer.

### Step 3 – Feature Selection

The following features were selected:

* Total Spending
* Total Quantity
* Number of Orders
* Average Order Value

### Step 4 – Standardization

The selected numerical features were standardized using StandardScaler.

### Step 5 – K-Means Clustering

K-Means clustering was applied using different values of K.

### Step 6 – Cluster Evaluation

Silhouette scores were calculated for the tested cluster values.

### Step 7 – Customer Segmentation

Customers were assigned to their respective clusters.

### Step 8 – Business Analysis

The resulting customer segments were analysed by spending, category, city, gender, and time.

---

## 7. Customer Segment Results

The final cluster results are summarized below.

| Customer Segment | Number of Customers | Total Spending | Average Order Value |
| ---------------- | ------------------: | -------------: | ------------------: |
| Cluster 0        |         [FILL THIS] |    [FILL THIS] |         [FILL THIS] |
| Cluster 1        |         [FILL THIS] |    [FILL THIS] |         [FILL THIS] |
| Cluster 2        |         [FILL THIS] |    [FILL THIS] |         [FILL THIS] |

> Replace the above values with the actual values from `Cluster_Summary.xlsx`.

---

## 8. Dashboard

The interactive dashboard was created using **Looker Studio**.

The dashboard contains two main pages.

### Page 1 – Executive Dashboard

The Executive Dashboard contains:

* Total Sales
* Total Customers
* Total Orders
* Total Quantity
* Average Order Value
* Total Sales by Customer Segment
* Number of Customers by Segment
* Sales by Category
* Sales by City
* Monthly Sales Trend
* Sales by Gender

### Page 2 – Customer Segmentation Analysis

The Customer Segmentation Analysis page contains:

* Customer count by segment
* Total spending by segment
* Sales by category and customer segment
* Sales by city and customer segment
* Monthly sales by customer segment
* Interactive filters

### Dashboard Filters

Users can interact with the dashboard using:

* Customer Segment
* Category
* City
* Gender
* Date Range

These filters allow users to explore specific portions of the dataset.

---

## 9. Key Findings

The main findings from the customer segmentation analysis are:

1. The customers were divided into distinct groups based on their purchasing behaviour.
2. The customer segments show differences in spending, quantity purchased, number of orders, and average order value.
3. The distribution of sales differs across customer segments.
4. Customer segments can also be compared across product categories and cities.
5. Monthly sales trends provide an additional view of how different customer segments contribute to sales over time.

### Specific Findings

**Highest-spending segment:** [FILL THIS]

**Segment with the highest number of customers:** [FILL THIS]

**Segment with the highest average order value:** [FILL THIS]

**Category with the highest sales:** [FILL THIS]

**City with the highest sales:** [FILL THIS]

**Important segment/category observation:** [FILL THIS]

**Important segment/city observation:** [FILL THIS]

---

## 10. Tools and Technologies

The following tools were used:

* **Python**
* **Google Colab**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**
* **Microsoft Excel**
* **Google Sheets**
* **Looker Studio**
* **GitHub**

---

## 11. Project Files

The Task 3 project contains the following files:

```text
Task3/
│
├── Task3_Customer_Segmentation_Dataset.xlsx
├── Customer_Segmentation_Results.xlsx
├── Cluster_Summary.xlsx
│
├── Python_Code/
│   └── Customer_Segmentation.py
│
├── Deep_Dive_Report/
│   └── Deep_Dive_Report.pdf
│
└── README.md
```

---

## 12. Dashboard Link

### Live Looker Studio Dashboard

**[PASTE YOUR LIVE LOOKER STUDIO LINK HERE]**

---

## 13. Conclusion

This project used K-Means clustering to perform a deep-dive customer segmentation analysis.

Customers were grouped according to purchasing behaviour using Total Spending, Total Quantity, Number of Orders, and Average Order Value.

The analysis was then presented through an interactive Looker Studio dashboard containing KPIs, charts, segment analysis, and filters.

The dashboard provides an easy way to explore customer behaviour and compare different customer segments across categories, cities, gender, and time.

---

## 14. Internship

**Program:** ApexPlanet Data Analytics Internship

**Task:** Task 3 – Deep-Dive Analysis & Interactive Dashboarding

**Deep-Dive Area:** Customer Segmentation

**Dashboard Tool:** Looker Studio

**Analysis Tool:** Python / Google Colab

