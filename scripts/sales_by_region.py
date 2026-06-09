import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

df = pd.read_sql("SELECT * FROM global_superstore", engine)

sales_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()

plt.show()