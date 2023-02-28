import base64
import io
import matplotlib.pyplot as plt

def plot_income_expense_over_time(first_name, last_name, months, income, expense):
    # Create the figure and axis objects
    fig, ax = plt.subplots()

    # Plot the income and expense over time
    ax.plot(months, income, label='Income')
    ax.plot(months, expense, label='Expense')

    # Add labels and title to the plot
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount')
    ax.set_title(f'Income and Expense over Time for {first_name} {last_name}')

    # Add legend to the plot
    ax.legend()

    # Save the plot to a bytes object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_bytes = buffer.getvalue()

    # Close the plot
    plt.close()

    return plot_bytes
