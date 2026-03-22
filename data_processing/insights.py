import pandas as pd
from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:1122@localhost:5432/ai_pipeline"
engine = create_engine(DB_URI)

# Top 5 customers by purchase
query1 = """
SELECT name, purchase_amount
FROM customers_processed
ORDER BY purchase_amount DESC
LIMIT 5;
"""

# Country-wise revenue
query2 = """
SELECT country, SUM(purchase_amount) as total_revenue
FROM customers_processed
GROUP BY country
ORDER BY total_revenue DESC;
"""

top_customers = pd.read_sql(query1, engine)
country_revenue = pd.read_sql(query2, engine)

print("\nTop Customers:\n", top_customers)
print("\nRevenue by Country:\n", country_revenue)
