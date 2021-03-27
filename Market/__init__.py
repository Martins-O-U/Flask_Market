from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///marketplace.db"
db = SQLAlchemy(app)

from Market import Routes