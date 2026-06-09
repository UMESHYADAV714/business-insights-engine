import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
import numpy as np

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

# Monthly Sales
monthly_sales = (
    df.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales']
    .sum()
    .reset_index()
)

# Create Time Index
monthly_sales['month_index'] = np.arange(len(monthly_sales))

# Features and Target
X = monthly_sales[['month_index']]
y = monthly_sales['Sales']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predict Next 12 Months
future_months = np.arange(
    len(monthly_sales),
    len(monthly_sales) + 12
).reshape(-1, 1)

future_predictions = model.predict(future_months)

print("\nPredicted Sales for Next 12 Months:\n")
print(future_predictions)

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales['month_index'],
    monthly_sales['Sales'],
    label='Historical Sales'
)

plt.plot(
    future_months,
    future_predictions,
    label='Forecast'
)

plt.title("Sales Forecast")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.show()