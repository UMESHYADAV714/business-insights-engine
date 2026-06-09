import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Umesh%40123@localhost:5432/business_insights"
)

query = "SELECT * FROM global_superstore"

df = pd.read_sql(query, engine)

print("Rows:", len(df))
print("Columns:", len(df.columns))