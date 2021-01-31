# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/comparisons")
def comparisons():
    return render_template("comparisons.html")

@app.route("/cloudiness")
def cloudiness():
    return render_template("cloudiness.html")

@app.route("/humidity")
def humidity():
    return render_template("humidity.html")

@app.route("/temp")
def temp():
    return render_template("temp.html")

@app.route("/windspeed")
def windspeed():
    return render_template("windspeed.html")


if __name__ == "__main__":
    app.run(debug=True)
