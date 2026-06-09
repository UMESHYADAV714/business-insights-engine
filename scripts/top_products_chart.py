import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# Load Data
query = "SELECT * FROM global_superstore"
df = pd.read_sql(query, engine)

# Top 10 Products by Sales
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Plot
plt.figure(figsize=(12,6))
top_products.plot(kind='bar')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()