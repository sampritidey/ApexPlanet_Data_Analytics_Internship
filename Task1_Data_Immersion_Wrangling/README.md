# ApexPlanet-Task1-Data-Wrangling
ApexPlanet 60-Day Data Analytics Internship – Task 1: Data Immersion &amp; Wrangling
# ApexPlanet Data Analytics Internship – Task 1

## Data Immersion & Wrangling

This project is part of the **ApexPlanet Software Pvt. Ltd. 60-Day Data Analytics Internship**.

The objective of Task 1 is to understand the provided sales dataset, assess its data quality, clean and transform the data, and prepare a final analysis-ready dataset.

## Dataset

The dataset contains sales transaction information including order details, customer information, product information, quantity, unit price, and total sales.

### Dataset Size

* Original records: 1,000
* Original columns: 12
* Final columns: 16
* Data source: ApexPlanet Internship Dataset
* Dataset type: Sales Transaction Data

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Google Colab
* Microsoft Excel
* GitHub

## Data Quality Assessment

The initial profiling identified the following issues:

| Data Quality Issue             |       Finding | Action Taken                                                  |
| ------------------------------ | ------------: | ------------------------------------------------------------- |
| Missing Age                    |    20 records | Filled using the median age                                   |
| Missing City                   |    13 records | Filled using the mode                                         |
| Duplicate complete rows        |             0 | No action required                                            |
| Duplicate Order_ID values      |       Present | Original IDs retained and a unique Transaction_ID was created |
| Order_Date data type           | Object/String | Converted to datetime                                         |
| Total_Sales outliers           |       Present | Retained because the values are plausible sales transactions  |
| Total_Sales calculation errors |             0 | No correction required                                        |

## Data Cleaning & Transformation

The following steps were performed:

1. Loaded the Excel dataset using Pandas.
2. Inspected the dataset structure, columns, and data types.
3. Checked for missing values.
4. Checked for duplicate records.
5. Investigated duplicate Order_ID values.
6. Checked categorical variables for consistency.
7. Checked numerical variables and potential outliers.
8. Verified that Total_Sales was consistent with Quantity × Unit_Price.
9. Converted Order_Date to datetime format.
10. Filled missing Age values using the median.
11. Filled missing City values using the mode.
12. Created a unique Transaction_ID for transaction-level identification.
13. Performed final data-quality validation.
14. Exported the cleaned dataset.

## Data Dictionary

The `Data_Dictionary.xlsx` file contains the definition, data type, example, and business relevance of every field in the dataset.

## Files in This Repository

```text
ApexPlanet-Task1/
│
├── README.md
├── data_cleaning.py
├── Data_Dictionary.xlsx
├── ApexPlanet_Cleaned_Sales_Dataset.csv
├── ApexPlanet_Cleaned_Sales_Dataset.xlsx
└── ApexPlanet_Task1_Data_Wrangling.ipynb
```

## Final Dataset

After cleaning, the dataset contains:

* 1,000 records
* 16 columns
* 0 missing values
* 0 duplicate complete rows
* 0 duplicate Transaction_ID values
* Valid datetime values in Order_Date

The resulting dataset is ready for further exploratory data analysis and business intelligence tasks.

## Key Learning Outcomes

Through this task, I practiced:

* Data loading and inspection
* Data profiling
* Missing-value handling
* Duplicate detection
* Data-type conversion
* Categorical data validation
* Outlier identification
* Data validation
* Feature creation
* Data transformation
* Exporting analysis-ready datasets
* Documentation using a data dictionary

## Conclusion

The raw sales dataset was successfully assessed, cleaned, transformed, and validated. The final dataset is structured and ready for the next stage of the internship, which involves Exploratory Data Analysis and Business Intelligence.
