from flask import Flask, render_template, request
import random

app = Flask(__name__)

pastes = {}

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/generate", methods=["POST"])
def generate():
    text = request.form["text"]

    paste_id = str(random.randint(1000, 9999))

    pastes[paste_id] = text

    return f"""
    Paste created successfully!<br>
    Paste ID: {paste_id}<br>
    Open: <a href="/paste/{paste_id}">View Paste</a>
    """

@app.route("/paste/<paste_id>")
def view_paste(paste_id):
    if paste_id in pastes:
        return pastes[paste_id]

    return "Paste not found"

if __name__ == "__main__":
    app.run(debug=True)