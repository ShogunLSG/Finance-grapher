import io
import matplotlib.pyplot as plt

def plot_income_expense_over_time(first_name, last_name,months, income, expense):
    plt.plot(months, income, label='Income')
    plt.plot(months, expense, label='Expense')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Income and Expense Over Time')
    plt.legend()
    buffer = io.BytesIO()
    plot_bytes = buffer.getvalue()
    plt.savefig(buffer, format='png')
    plt.close()
    return plot_bytes
    