from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        date_of_birth = request.form.get('date_of_birth')
        file = request.files['file']
        if file.filename != '':
            df = pd.read_excel(file)
            # do something with the data in the Excel file
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)