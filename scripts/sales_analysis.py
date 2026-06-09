import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

df = pd.read_sql("SELECT * FROM global_superstore", engine)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nTop 5 Regions by Sales:")
print(
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head()
)