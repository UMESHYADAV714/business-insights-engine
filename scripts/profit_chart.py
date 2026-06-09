import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

df = pd.read_sql("SELECT * FROM global_superstore", engine)

top_profit = (
    df.groupby('Product Name')['Profit']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
top_profit.plot(kind='bar')

plt.title("Top 10 Products by Profit")
plt.xlabel("Product")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()