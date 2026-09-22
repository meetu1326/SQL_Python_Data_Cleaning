import numpy as np
import pandas as pd

# 1. Load data
df = pd.read_excel('SQL_Sales_Dataset_200_Rows.xlsx')

# 2. Clean data
df = df.drop_duplicates()
df = df.dropna()

# 3. Overall Total Revenue
total_revenue = df['total_price'].sum()

# 4. Group data by category and find total revenue per category
category_revenue = (
    df.groupby('category')['total_price'].sum().reset_index()
)

# 5. Sort by category and total_price (highest sales first within each category)
df_sorted = df.sort_values(
    by=['category', 'total_price'], ascending=[True, False]
)

# 6. Correlation matrix for numerical columns (order_id, quantity, unit_price, total_price)
correlation_matrix = df.corr(numeric_only=True)

# 7. Print all outputs
print(f"Overall Total Revenue: {total_revenue:,}\n")

print("--- Revenue by Category ---")
print(category_revenue)

print("\n--- Correlation Matrix ---")
print(correlation_matrix)