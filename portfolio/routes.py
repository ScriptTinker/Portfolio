from portfolio import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/download_cv", methods=["GET", "POST"])
def download_cv():
    return render_template("download_cv.html")


