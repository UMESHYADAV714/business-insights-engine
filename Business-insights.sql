CREATE TABLE global_superstore (
row_id TEXT,
order_id TEXT,
order_date TEXT,
ship_date TEXT,
ship_mode TEXT,
customer_id TEXT,
customer_name TEXT,
segment TEXT,
city TEXT,
state TEXT,
country TEXT,
postal_code TEXT,
market TEXT,
region TEXT,
product_id TEXT,
category TEXT,
sub_category TEXT,
product_name TEXT,
sales TEXT,
quantity TEXT,
discount TEXT,
profit TEXT,
shipping_cost TEXT,
order_priority TEXT,
month TEXT
);

SELECT COUNT(*)
FROM global_superstore;

select * from global_superstore limit 5

--Total Sales
SELECT ROUND(SUM("Sales")::numeric,2) As total_sales
FROM global_superstore;

--Total Profit
SELECT ROUND(SUM("Profit")::numeric,2) As total_profit
FROM global_superstore;

--Total Order
SELECT COUNT(DISTINCT "Order ID") As total_order
FROM global_superstore;

--Total Customers
SELECT COUNT(DISTINCT "Customer ID") As total_customer
FROM global_superstore;

--Highest Sales Region
SELECT "Region",
       ROUND(SUM("Sales")::numeric,2) AS total_sales
FROM global_superstore
GROUP BY "Region"
ORDER BY total_sales DESC;

--Highest Profit Region
SELECT "Region",
       ROUND(SUM("Profit")::numeric,2) AS total_profit
FROM global_superstore
GROUP BY "Region"
ORDER BY total_profit DESC;

--Top 10 Products by Sales
SELECT "Product Name",
       ROUND(SUM("Sales")::numeric,2) AS total_sales
FROM global_superstore
GROUP BY "Product Name"
ORDER BY total_sales DESC
limit 10;

--Top 10 prodct by profit
SELECT "Product Name",
       ROUND(SUM("Profit")::numeric,2) AS total_profit
FROM global_superstore
GROUP BY "Product Name"
ORDER BY total_profit DESC
limit 10;

--Top 10 Customers by Sales
SELECT "Customer Name",
       ROUND(SUM("Sales")::numeric,2) AS total_sales
FROM global_superstore
GROUP BY "Customer Name"
ORDER BY total_sales DESC
limit 10;

--Top 10 customer name by profit
SELECT "Customer Name",
       ROUND(SUM("Profit")::numeric,2) AS total_profit
FROM global_superstore
GROUP BY "Customer Name"
ORDER BY total_profit DESC
limit 10;

--Monthly Sales Trend
SELECT
    DATE_TRUNC(
        'month',
        TO_DATE("Order Date",'MM/DD/YYYY')
    ) AS month,
    ROUND(SUM("Sales")::numeric,2) AS total_sales
FROM global_superstore
GROUP BY month
ORDER BY month;

DROP VIEW sales_dashboard_clean;

CREATE VIEW sales_dashboard_clean AS
SELECT
    "ï»¿Row ID" AS row_id,
    "Order ID" AS order_id,
    "Order Date" AS order_date,
    "Ship Date" AS ship_date,
    "Ship Mode" AS ship_mode,
    "Customer ID" AS customer_id,
    "Customer Name" AS customer_name,
    "Segment" AS segment,
    "City" AS city,
    "State" AS state,
    "Country" AS country,
    "Postal Code" AS postal_code,
    "Market" AS market,
    "Region" AS region,
    "Product ID" AS product_id,
    "Category" AS category,
    "Sub-Category" AS sub_category,
    "Product Name" AS product_name,
    "Sales" AS sales,
    "Quantity" AS quantity,
    "Discount" AS discount,
    "Profit" AS profit,
    "Shipping Cost" AS shipping_cost,
    "Order Priority" AS order_priority,
    "Month" AS month
FROM global_superstore;

SELECT * FROM sales_dashboard
LIMIT 5;

SELECT column_name
FROM information_schema.columns
WHERE table_name = 'sales_dashboard_clean'
ORDER BY ordinal_position;

SELECT *
FROM sales_dashboard_clean
LIMIT 1;