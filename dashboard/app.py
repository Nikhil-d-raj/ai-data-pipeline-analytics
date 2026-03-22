import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:1122@localhost:5432/ai_pipeline"
engine = create_engine(DB_URI)

st.title("📊 Customer Analytics Dashboard")

# Load data
df = pd.read_sql("SELECT * FROM customers_processed", engine)

# Sidebar filter
country = st.sidebar.selectbox("Select Country", df["country"].unique())

filtered_df = df[df["country"] == country]

# Show data
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Top customers
st.subheader("Top 5 Customers")
top5 = df.sort_values(by="purchase_amount", ascending=False).head(5)
st.dataframe(top5)

# Revenue by country
st.subheader("Revenue by Country")
revenue = df.groupby("country")["purchase_amount"].sum().reset_index()
st.bar_chart(revenue.set_index("country"))

st.sidebar.title("Filters")
st.write("### Total Records:", len(filtered_df))

st.metric("Total Revenue", f"{filtered_df['purchase_amount'].sum():.2f}")

st.subheader("🤖 Ask Questions (AI)")

#user_question = st.text_input("Ask something about the data")

#if user_question:
 #   from ai_module.ai_query import ask_question
 #   result = ask_question(user_question)
 #   st.write(result)

st.download_button(
    label="Download CSV",
    data=filtered_df.to_csv(index=False),
    file_name="report.csv",
    mime="text/csv"
)
