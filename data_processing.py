import pandas as pd

def process_input_file(file):
    df = pd.read_excel(file)
    months = df['month']
    income = df['income']
    expense = df['expense']
    return months, income, expense