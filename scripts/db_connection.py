import pandas as pd
from sqlalchemy import create_engine

username = "postgres"
password = "Umesh%40123"
host = "localhost"
port = "5432"
database = "business_insights"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

query = "SELECT * FROM global_superstore LIMIT 5"

df = pd.read_sql(query, engine)

print(df.head())