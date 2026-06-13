import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

query = """
SELECT "Region",
       SUM("Sales") AS total_sales,
       SUM("Profit") AS total_profit
FROM global_superstore
GROUP BY "Region"
ORDER BY total_sales DESC;
"""

df = pd.read_sql(query, engine)

top_region = df.iloc[0]

print("\n===== AI BUSINESS INSIGHTS =====\n")

print(
    f"The {top_region['Region']} Region generated the highest sales "
    f"of ${top_region['total_sales']:,.2f}."
)

print(
    f"The same region generated a profit of "
    f"${top_region['total_profit']:,.2f}."
)

print("\nRecommendation:")
print(
    f"Increase marketing and inventory investment "
    f"in the {top_region['Region']} region."
)