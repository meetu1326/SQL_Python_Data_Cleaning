import sqlite3
import pandas as pd

# 1. Read your existing dataset
df = pd.read_excel('SQL_Sales_Dataset_200_Rows.xlsx')

# 2. Create an in-memory SQL database (exists only while Python runs)
conn = sqlite3.connect(':memory:')

# 3. Dump the DataFrame into an SQL table named 'sales'
df.to_sql('sales', conn, index=False, if_exists='replace')

# 4. Now write and run standard SQL queries directly!

# Task: Find top customers and their total spend
query_top_customers = """
SELECT 
    customer_name, 
    COUNT(order_id) AS total_orders,
    SUM(total_price) AS total_spent,
    AVG(total_price) AS avg_order_value
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 5;
"""

result = pd.read_sql_query(query_top_customers, conn)
print("--- Top 5 Customers ---")
print(result)

# Task: Revenue and Average order value by Category
query_category = """
SELECT 
    category,
    COUNT(order_id) AS order_count,
    ROUND(AVG(total_price), 2) AS avg_order_value,
    SUM(total_price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;
"""

result_cat = pd.read_sql_query(query_category, conn)
print("\n--- Category Breakdown ---")
print(result_cat)