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

# Convert to Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Month-Year
df['month_year'] = df['Order Date'].dt.to_period('M')

# Monthly Sales
monthly_sales = (
    df.groupby('month_year')['Sales']
    .sum()
)

# Plot
plt.figure(figsize=(12,6))
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()