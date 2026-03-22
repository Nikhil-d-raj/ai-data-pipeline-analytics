import pandas as pd
from sqlalchemy import create_engine

# Update with your credentials
DB_URI = "postgresql://postgres:1122@localhost:5432/ai_pipeline"

engine = create_engine(DB_URI)

df = pd.read_csv("data_ingestion/customer_data.csv")

df.to_sql("customers", engine, if_exists="replace", index=False)

print("Data loaded into database!")
