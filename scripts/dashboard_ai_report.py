import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

region_query = """
SELECT "Region",
       SUM("Sales") AS total_sales,
       SUM("Profit") AS total_profit
FROM global_superstore
GROUP BY "Region"
ORDER BY total_sales DESC;
"""

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

report = f"""
=========================================
AI BUSINESS REPORT
=========================================

Top Region: {top_region['Region']}
Sales: ${top_region['total_sales']:,.2f}
Profit: ${top_region['total_profit']:,.2f}

Top Category: {top_category['Category']}
Category Profit: ${top_category['total_profit']:,.2f}

Recommendation:
Focus on expanding the {top_category['Category']}
category in the {top_region['Region']} region.

=========================================
"""

with open("Reports/ai_business_report.txt", "w") as file:
    file.write(report)

print("AI Business Report Generated Successfully!")