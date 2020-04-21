from flask import Flask
from flask import render_template
import requests


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/<name>')
def home(name):
    return requests.get("https://pythonfunctionapp2020.azurewebsites.net/api/HttpTrigger1?code=0x3ACUo0kOvRPm/tUs9U/9VNBdDe4bdx1YL/CusgkSIGgVobr37ERQ==&name="+name)

