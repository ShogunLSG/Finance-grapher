import base64
from flask import Flask, render_template, request
import pandas as pd
import os
from plotting import plot_income_expense_over_time
import sqlite3
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('date_of_birth')
        file = request.files['file']
        if file.filename != '':

            file_contents = file.read()
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS data 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             first_name TEXT NOT NULL,
                             last_name TEXT NOT NULL,
                             date_of_birth TEXT NOT NULL,
                             filename TEXT NOT NULL)''')
            
            cursor.execute('''INSERT INTO data (first_name, last_name, date_of_birth, filename)
                              VALUES (?, ?, ?, ?)''',
                              (first_name, last_name, date_of_birth))
            
            data_id = cursor.lastrowid

            df = pd.read_excel(file_contents)
            months = df['Month']
            income = df['Income']
            expense = df['Expense']

            plot_bytes = plot_income_expense_over_time(first_name, last_name, months, income, expense)
            cursor.execute('UPDATE data SET graph=? WHERE id=?', (plot_bytes, data_id))
            conn.commit()
            conn.close()

             # Encode the graph bytes as base64 and create the data URI for the image
            plot_data_uri = base64.b64encode(plot_bytes).decode('ascii')
            plot_data_uri = f"data:image/png;base64,{plot_data_uri}"
            
            return render_template('success.html', plot_data_uri=plot_data_uri)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)