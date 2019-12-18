from flask import Flask, render_template, Response

from engine import getExpectationsData
from sales_prediction import save_prediction

import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sales-expectations')
def sales_expectations():
    graphData = getExpectationsData()

    return Response(
        json.dumps(graphData),
        mimetype="application/json"
    )

@app.route('/save-prediction-to-csv')
def save_prediction_to_csv():
    save_prediction()
    return render_template("saved.html")

if __name__ == '__main__':
    app.run(debug=True)
