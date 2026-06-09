import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

df = pd.read_sql("SELECT * FROM global_superstore", engine)

top_customers = (
    df.groupby("Customer Name")
      .agg({
          "Sales": "sum",
          "Profit": "sum"
      })
      .sort_values("Sales", ascending=False)
      .head(10)
)

print("\nTop 10 Customers:")
print(top_customers)