import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

df = pd.read_sql(
    "SELECT \"Sales\", \"Profit\", \"Quantity\" FROM global_superstore",
    engine
)

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
total_quantity = df['Quantity'].sum()

print("\n===== BUSINESS KPIs =====\n")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Quantity Sold: {total_quantity:,}")