from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# load trained ML model
model = joblib.load("models/loan_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = pd.DataFrame([request.json])

    prediction = model.predict(data)

    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)