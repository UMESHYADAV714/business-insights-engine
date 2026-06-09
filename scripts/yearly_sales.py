import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# Load Data
df = pd.read_sql(
    "SELECT \"Order Date\", \"Sales\" FROM global_superstore",
    engine
)

# Convert Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year
df['year'] = df['Order Date'].dt.year

# Yearly Sales
yearly_sales = (
    df.groupby('year')['Sales']
    .sum()
)

print("\nYearly Sales:\n")
print(yearly_sales)

# Plot
plt.figure(figsize=(8,5))
yearly_sales.plot(kind='bar')

plt.title("Yearly Sales Performance")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()