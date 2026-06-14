import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Database Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

# Query
query = """
SELECT
    "Category" AS category,
    ROUND(SUM("Sales")::numeric, 2) AS total_sales,
    ROUND(SUM("Profit")::numeric, 2) AS total_profit
FROM global_superstore
GROUP BY "Category"
ORDER BY total_sales DESC;
"""

# Load Data
df = pd.read_sql(query, engine)

# Create File Name
date = datetime.now().strftime("%Y-%m-%d")
file_name = f"reports/business_report_{date}.csv"

# Export Report
df.to_csv(file_name, index=False)

print(f"Report generated successfully: {file_name}")