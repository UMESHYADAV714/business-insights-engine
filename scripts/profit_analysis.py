import pandas as pd
from sqlalchemy import create_engine

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# Load Data
query = "SELECT * FROM global_superstore"
df = pd.read_sql(query, engine)

# Top 10 Most Profitable Products
top_profit = (
    df.groupby('Product Name')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 MOST PROFITABLE PRODUCTS\n")
print(top_profit)

# Top 10 Least Profitable Products
least_profit = (
    df.groupby('Product Name')['Profit']
    .sum()
    .sort_values(ascending=True)
    .head(10)
)

print("\nTOP 10 LEAST PROFITABLE PRODUCTS\n")
print(least_profit)