from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///marketplace.db"
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False )
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=350), nullable=False)

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('Home.html')

@app.route('/about')
def about_page():
    return "<h2>This is the about page</h2>"

@app.route('/market')
def market():
    items = [
        {"id":1, "name":"Phone", "barcode": 12345, "price": 500},
        {"id":2, "name":"Laptop", "barcode": 123456, "price": 1500},
        {"id":3, "name":"Keyboard", "barcode": 1234567, "price": 100}
    ]
    return render_template('MarketStore.html', items_name=items)
    