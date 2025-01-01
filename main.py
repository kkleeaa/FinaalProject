import streamlit as st
from database import Database
from visualizations import plot_summary
from reminders import check_bill_reminders
from goals import manage_financial_goals

st.title("Finance Management App")
st.sidebar.title("Navigation")
menu= st.sidebar.radio("Go to", ["Add Entry", "Visualize Data", "Bill Reminders"])

db=Database("finance.db")
if menu=="Add Entry":
    st.header("Add Income or Expense")
    entry_type=st.radio("Type",["Income", "Expense"])
    amount= st.number_input("Amount", min_value=0.0, format="%.2f")
    source=st.text_input("Source/Description")
    date=st.date_input("Date")
    if st.button("Add entry"):
        db.add_entry(entry_type, amount, source,date)
        st.success(f"{entry_type} added successfully!")
elif menu=="Visualize Data":
    st.header("Financial Summary")
    data=db.get_all_entries()
    if data:
        plot_summary(data)
    else:
        st.info("No data available. Add some entries to visualize.")
elif menu=="Bill Reminders":
    st.header("Upcoming Bills")
    check_bill_reminders()
elif menu=="Financial Goals":
    st.header("Manage Your Financial Goals")
    manage_financial_goals(db)


