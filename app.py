from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/card")
def card():
    return "THIS IS A TEST"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
