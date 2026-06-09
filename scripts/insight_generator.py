import pandas as pd
from sqlalchemy import create_engine

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# Load Data
df = pd.read_sql("SELECT * FROM global_superstore", engine)

print("\n===== BUSINESS INSIGHTS =====\n")

# Top Region
top_region = (
    df.groupby('Region')['Sales']
    .sum()
    .idxmax()
)

print(f"INSIGHT 1: {top_region} region generated the highest sales.")

# Top Category
top_category = (
    df.groupby('Category')['Profit']
    .sum()
    .idxmax()
)

print(f"INSIGHT 2: {top_category} category generated the highest profit.")

# Top Customer
top_customer = (
    df.groupby('Customer Name')['Sales']
    .sum()
    .idxmax()
)

print(f"INSIGHT 3: Top customer is {top_customer}.")

print("\n===== RECOMMENDATION =====")

print(f"Focus marketing efforts in the {top_region} region.")
print(f"Promote products from the {top_category} category.")