# SQL for Data Analysis – Sales Dataset Analysis

## Project Overview
This project demonstrates end-to-end data analysis workflows using Python, Pandas, and an embedded SQL environment. Designed to fulfill the **Week 2: SQL for Data Analysis** curriculum, this implementation queries and derives business intelligence metrics from transactional sales data without requiring external database server installations (such as MySQL or PostgreSQL).

Using Python's native `sqlite3` engine alongside `pandas`, raw tabular sales records are loaded into an in-memory SQL database where relational queries are executed directly to identify customer purchasing behaviors, transaction values, and product performance.

---

## Key Objectives & Deliverables
* **Serverless SQL Pipeline:** Load `.xlsx` sales datasets into Pandas and stream them directly into an in-memory SQLite database instance (`:memory:`).
* **Customer Value Analysis:** Aggregate transactional spend using `SUM()`, `AVG()`, and `COUNT()` to isolate top-spending customers and compute Average Order Value (AOV).
* **Category Breakdown:** Group sales figures by product category to calculate overall revenue contribution and order volumes using `GROUP BY` and `ORDER BY` operations.
* **Data Cleaning & Multi-Column Sorting:** Preprocess raw datasets by removing duplicates, managing null values, and ordering records hierarchically across categorical and numerical features.

---

## Dataset Schema
The project analyzes transactional records with the following structural layout:

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_id` | `INTEGER` | Unique transaction identifier |
| `customer_name` | `TEXT` | Customer full name |
| `order_date` | `DATETIME` | Timestamp of the purchase |
| `category` | `TEXT` | Primary product category |
| `sub_category` | `TEXT` | Specific product sub-segment |
| `product_name` | `TEXT` | Item title / description |
| `quantity` | `INTEGER` | Number of units purchased |
| `unit_price` | `INTEGER` | Individual unit price |
| `total_price` | `INTEGER` | Line-item total transaction value |
| `region` | `TEXT` | Geographic sales territory |

---

## SQL Queries Implemented

### 1. Identifying Top 5 Customers by Spend
```sql
SELECT 
    customer_name, 
    COUNT(order_id) AS total_orders,
    SUM(total_price) AS total_spent,
    AVG(total_price) AS avg_order_value
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 5;
