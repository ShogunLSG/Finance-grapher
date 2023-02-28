import matplotlib.pyplot as plt

def plot_income_expense_over_time(first_name, last_name,months, income, expense):
    plt.plot(months, income, label='Income')
    plt.plot(months, expense, label='Expense')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Income and Expense Over Time')
    plt.legend()
    filename = f'{first_name}_{last_name}_temporal_graph.png'
    plt.savefig(filename)
    plt.close()
    return f'statis/{filename}'
    