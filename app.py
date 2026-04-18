from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]

    # save temporarily
    filepath = "temp.jpg"
    file.save(filepath)

    # 🔥 for now dummy response
    result = {
        "status": "success",
        "message": "Image received. Model will run here."
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run()