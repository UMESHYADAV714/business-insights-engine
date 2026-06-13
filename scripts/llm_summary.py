import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# Region Analysis
region_query = """
SELECT "Region",
       SUM("Sales") AS total_sales,
       SUM("Profit") AS total_profit
FROM global_superstore
GROUP BY "Region"
ORDER BY total_sales DESC;
"""

# Category Analysis
category_query = """
SELECT "Category",
       SUM("Profit") AS total_profit
FROM global_superstore
GROUP BY "Category"
ORDER BY total_profit DESC;
"""

region_df = pd.read_sql(region_query, engine)
category_df = pd.read_sql(category_query, engine)

top_region = region_df.iloc[0]
top_category = category_df.iloc[0]

summary = f"""
=====================================
AI EXECUTIVE BUSINESS SUMMARY
=====================================

Top Performing Region:
{top_region['Region']}

Total Sales:
${top_region['total_sales']:,.2f}

Total Profit:
${top_region['total_profit']:,.2f}

Most Profitable Category:
{top_category['Category']}

Category Profit:
${top_category['total_profit']:,.2f}

Strategic Recommendation:
Increase inventory and marketing efforts in the
{top_region['Region']} region while expanding
the {top_category['Category']} category.

=====================================
"""

print(summary)