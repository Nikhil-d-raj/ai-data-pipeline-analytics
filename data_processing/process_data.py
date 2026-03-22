import pandas as pd
from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:1122@localhost:5432/ai_pipeline"
engine = create_engine(DB_URI)

# Load data
df = pd.read_sql("SELECT * FROM customers", engine)

# Clean data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Transform
df["purchase_category"] = df["purchase_amount"].apply(
    lambda x: "Low" if x < 1000 else "Medium" if x < 5000 else "High"
)
# Add ranking
df["rank"] = df["purchase_amount"].rank(ascending=False)

# Save processed data back
df.to_sql("customers_processed", engine, if_exists="replace", index=False)

print("Data cleaned and processed!")
