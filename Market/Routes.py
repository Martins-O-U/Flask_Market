from Market import app
from flask import render_template
from Market.Modules import Item

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('Home.html')

@app.route('/about')
def about_page():
    return "<h2>This is the about page</h2>"

@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('MarketStore.html', items_name=items)
    