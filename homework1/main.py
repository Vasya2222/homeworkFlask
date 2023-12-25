from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/clothes')
def clothes():
    return render_template('clothes.html')


@app.route('/hats')
def hats():
    return render_template('hats.html')


@app.route('/jacket')
def jacket():
    return render_template('jacket.html')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html')
