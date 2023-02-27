from flask import Flask, request, send_file, render_template
from importScores import importScores
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']
        # Save the file to a temporary location
        file.save('input.csv')
        # Run a Python script on the file

        input_df = pd.read_csv('input.csv')
        output_df = importScores(input_df)
        output_df.to_csv('output.csv', index=False)

        # Export the new file to the user
        return send_file('output.csv', as_attachment=True)
    return render_template('index.html')
