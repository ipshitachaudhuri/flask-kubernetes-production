from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/")
def home():
    return jsonify({
        "message": "Flask API running on Kubernetes"
    })


@app.route("/info")
def info():
    return jsonify({
        "database": os.getenv("DATABASE_NAME"),
        "host": os.getenv("DATABASE_HOST")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

