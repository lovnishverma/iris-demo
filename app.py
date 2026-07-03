from flask import Flask, render_template, request
from datetime import datetime
import joblib
import pytz

app = Flask(__name__)  # Initilize the Flask app

# Load the trained model and scaler
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")


@app.route('/')
def index():
    current_timedate = datetime.now(pytz.timezone('Asia/Kolkata'))
    return render_template("index.html", ct=current_timedate)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the HTML form
    sepal_length = float(request.form.get("sl"))
    sepal_width = float(request.form.get("sw"))
    petal_length = float(request.form.get("pl"))
    petal_width = float(request.form.get("pw"))

    # Create feature vector
    features = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Scale the input
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)

    return render_template("index.html", pred=prediction[0], ct=datetime.now(pytz.timezone('Asia/Kolkata')))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
