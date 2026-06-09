import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# Load Data
query = "SELECT * FROM global_superstore"
df = pd.read_sql(query, engine)

# Top Products by Sales
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:\n")
print(top_products)

# Top Products by Profit
top_profit_products = (
    df.groupby('Product Name')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Profit:\n")
print(top_profit_products)