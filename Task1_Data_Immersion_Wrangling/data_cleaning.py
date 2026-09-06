```python
import pandas as pd
import numpy as np

# ============================================
# 1. LOAD DATASET
# ============================================

input_file = "ApexPlanet_DataAnalytics_Dataset(2).xlsx"

df = pd.read_excel(input_file)

print("Dataset loaded successfully.")
print("Original shape:", df.shape)
print(df.columns)


# ============================================
# 2. INITIAL DATA PROFILING
# ============================================

print("\n===== DATASET INFORMATION =====")
print(df.info())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print("Duplicate complete rows:", df.duplicated().sum())


# ============================================
# 3. CHECK DUPLICATE ORDER IDs
# ============================================

print("\n===== DUPLICATE ORDER IDs =====")
print(
    "Duplicate Order_ID records:",
    df['Order_ID'].duplicated().sum()
)


# ============================================
# 4. CHECK NUMERICAL VARIABLES
# ============================================

print("\n===== NUMERICAL SUMMARY =====")
print(
    df[
        ['Age', 'Quantity', 'Unit_Price', 'Total_Sales']
    ].describe()
)


# ============================================
# 5. CHECK TOTAL SALES CALCULATION
# ============================================

df['Calculated_Sales'] = (
    df['Quantity'] * df['Unit_Price']
)

sales_difference = (
    df['Calculated_Sales'] - df['Total_Sales']
).abs()

print("\n===== SALES VALIDATION =====")
print(
    "Sales calculation mismatches:",
    (sales_difference > 0.01).sum()
)

# Remove temporary validation column
df.drop('Calculated_Sales', axis=1, inplace=True)


# ============================================
# 6. CONVERT ORDER DATE
# ============================================

df['Order_Date'] = pd.to_datetime(
    df['Order_Date'],
    errors='coerce'
)

print("\nInvalid dates:",
      df['Order_Date'].isnull().sum())


# ============================================
# 7. HANDLE MISSING AGE
# ============================================

age_median = df['Age'].median()

df['Age'] = df['Age'].fillna(age_median)

print(
    "Missing Age after cleaning:",
    df['Age'].isnull().sum()
)


# ============================================
# 8. HANDLE MISSING CITY
# ============================================

df['City'] = df['City'].fillna('Unknown')
print(df['City'].isnull().sum())


# ============================================
# 9. CREATE UNIQUE TRANSACTION ID
# ============================================

df.insert(
    0,
    'Transaction_ID',
    [
        'TXN' + str(i).zfill(4)
        for i in range(1, len(df) + 1)
    ]
)


# ============================================
# 10. FINAL DATA QUALITY CHECK
# ============================================

print("\n===== FINAL DATA QUALITY CHECK =====")

print("Final rows:", len(df))
print("Final columns:", len(df.columns))

print(
    "Total missing values:",
    df.isnull().sum().sum()
)

print(
    "Duplicate complete rows:",
    df.duplicated().sum()
)

print(
    "Duplicate Transaction_ID:",
    df['Transaction_ID'].duplicated().sum()
)

print(
    "Invalid dates:",
    df['Order_Date'].isnull().sum()
)


# ============================================
# 11. SAVE CLEANED DATASET
# ============================================

output_csv = "ApexPlanet_Cleaned_Sales_Dataset.csv"
output_excel = "ApexPlanet_Cleaned_Sales_Dataset.xlsx"

df.to_csv(
    output_csv,
    index=False
)

df.to_excel(
    output_excel,
    index=False
)

print("\n===== EXPORT COMPLETE =====")
print("CSV:", output_csv)
print("Excel:", output_excel)

print("\nFirst five cleaned records:")
print(df.head())
```
df.to_csv(
    'ApexPlanet_Cleaned_Datase.csv',
    index=False
)

print("Cleaned CSV file created successfully!")
from google.colab import files

files.download('ApexPlanet_Cleaned_Datase.csv')
