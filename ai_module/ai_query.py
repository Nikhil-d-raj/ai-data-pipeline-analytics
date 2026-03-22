import pandas as pd
from sqlalchemy import create_engine

DB_URI = "postgresql://username:password@localhost:5432/ai_pipeline"
engine = create_engine(DB_URI)

def ask_question(question):
    question = question.lower()

    if "top customers" in question:
        query = """
        SELECT name, purchase_amount
        FROM customers_processed
        ORDER BY purchase_amount DESC
        LIMIT 5;
        """

    elif "revenue by country" in question:
        query = """
        SELECT country, SUM(purchase_amount) as total_revenue
        FROM customers_processed
        GROUP BY country
        ORDER BY total_revenue DESC;
        """

    elif "total revenue" in question:
        query = """
        SELECT SUM(purchase_amount) as total_revenue
        FROM customers_processed;
        """

    else:
        return "Sorry, I can’t answer that yet."

    df = pd.read_sql(query, engine)
    return df
