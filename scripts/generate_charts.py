import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

query = """
SELECT
    "Category" AS category,
    ROUND(SUM("Sales")::numeric,2) AS total_sales
FROM global_superstore
GROUP BY "Category"
ORDER BY total_sales DESC;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8,5))
plt.bar(df["category"], df["total_sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("charts/sales_by_category.png")

# Generate profit chart
query_profit = """
SELECT
    "Category" AS category,
    ROUND(SUM("Profit")::numeric,2) AS total_profit
FROM global_superstore
GROUP BY "Category"
ORDER BY total_profit DESC;
"""

profit_df = pd.read_sql(query_profit, engine)

plt.figure(figsize=(8,5))
plt.bar(profit_df["category"], profit_df["total_profit"])
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()

#

plt.savefig("charts/monthly_sales_trend.png")
plt.savefig("charts/profit_by_category.png")
print("Chart generated successfully!")