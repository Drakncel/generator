from flask import Flask
from flask_cors import CORS
from app.generator import generateCreatures

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    response = {
        "message": "Welcome to the API, please use the /generate route in order to generate data"
    }
    return response

@app.route("/generate")
def generate():
    response = {
        "result": generateCreatures()
    }
    return response


# app.run(debug=True, host="0.0.0.0", port="80")