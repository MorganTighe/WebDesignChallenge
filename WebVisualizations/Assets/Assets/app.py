# import necessary libraries
from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy

session = Session(bind=db)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db, reflect=True)

# Save reference to the table
Country = Base.classes.wh20

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("startercode.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/life_map")
def life():
    return render_template("life_map.html")




if __name__ == "__main__":
    app.run(debug=True)
