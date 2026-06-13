import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

query = """
SELECT "Category",
       SUM("Sales") AS total_sales,
       SUM("Profit") AS total_profit
FROM global_superstore
GROUP BY "Category"
ORDER BY total_profit DESC;
"""

df = pd.read_sql(query, engine)

best_category = df.iloc[0]

print("\n===== SMART RECOMMENDATIONS =====\n")

print(
    f"The most profitable category is {best_category['Category']} "
    f"with profit of ${best_category['total_profit']:,.2f}"
)

print("\nBusiness Recommendation:")
print(
    f"Focus marketing campaigns on {best_category['Category']} products "
    f"to maximize profitability."
)