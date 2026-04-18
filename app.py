from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    filepath = "temp.jpg"
    file.save(filepath)

    return jsonify({
        "status": "success",
        "message": "Image received. Model will run here."
    })