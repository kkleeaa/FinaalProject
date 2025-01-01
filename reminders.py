import streamlit as st
from datetime import datetime, timedelta

# data fallco
bills = [
    {"name": "Rent", "due_date": "2024-12-01"},
    {"name": "Electricity", "due_date": "2024-12-05"},
    {"name": "Internet", "due_date": "2024-12-10"}
]

def check_bill_reminders():
    today = datetime.today()
    for bill in bills:
        due_date = datetime.strptime(bill["due_date"], "%Y-%m-%d")
        days_left = (due_date - today).days
        if days_left > 0:
            st.write(f"{bill['name']} is due in {days_left} days on {bill['due_date']}.")
        else:
            st.warning(f"{bill['name']} was due on {bill['due_date']}. Please pay it immediately!")