from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)
CORS(app)

# 🔥 Load model once (IMPORTANT)
model = YOLO("yolov8n.pt")  # small model for free tier

@app.route("/")
def home():
    return "Backend running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]

    filepath = "temp.jpg"
    file.save(filepath)

    # 🔥 Run YOLO
    results = model(filepath)

    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls]

            detections.append({
                "class": name,
                "confidence": round(conf, 2)
            })

    return jsonify({
        "detections": detections
    })

if __name__ == "__main__":
    app.run()