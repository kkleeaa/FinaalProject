# visualizations.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_summary(data):
    # Fix: Pass the column names as a list, not a dictionary
    df = pd.DataFrame(data, columns=["ID", "Type", "Amount", "Source", "Date"])
    df["Date"] = pd.to_datetime(df["Date"])
    income = df[df["Type"] == "Income"]["Amount"].sum()
    expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = income - expense

    st.write(f"Total Income: ${income:.2f}")
    st.write(f"Total Expenses: ${expense:.2f}")
    st.write(f"Net Balance: ${balance:.2f}")

    # Bar chart summarizing income and expenses
    st.bar_chart(df.groupby("Type")["Amount"].sum())

