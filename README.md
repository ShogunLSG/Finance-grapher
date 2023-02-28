# Finance-grapher
Graphs finances from an excel input file.

File Upload and Visualization Project
This project allows users to upload a CSV file containing monthly income and expense data for a specific individual and generates a visualization of the data. The visualization is a line chart that shows the income and expense over time.

Getting Started
To get started with this project, you'll need to do the following:

Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Run the Flask application by running python app.py.
Navigate to http://localhost:5000/ in your web browser to access the application.
Usage
Once you've accessed the application, you can use it by following these steps:

Fill in the input fields with the appropriate information (First Name, Last Name, Date of Birth, and the CSV file containing monthly income and expense data).
Click the "Upload" button to upload the file and generate the visualization.
If the upload is successful, you'll be redirected to a success page that displays the visualization.
Notes
The CSV file must contain two columns labeled "income" and "expense", and one column labeled "month" that contains dates in the format "YYYY-MM-DD".
The visualization is generated using the Matplotlib library and saved as a PNG image. The image is then encoded as a Base64 string and embedded in the success page using a data URI.
This project uses Bootstrap for styling, and the necessary files are included in the static folder.
If there are any issues with the uploaded file, an error message will be displayed on the upload page.
Contributing
If you'd like to contribute to this project, you can do so by creating a pull request with your changes. Please make sure to include a clear description of the changes you've made and any relevant test cases.

License
This project is licensed under the MIT License - see the LICENSE file for details.



