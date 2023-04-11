from flask import Flask, render_template
import json
from helpers import calc_precision_and_recall

app = Flask(__name__, template_folder='templates/', static_folder='static/')

@app.route('/')
def home():
    """Renders Flask app from events.json"""
    freebies = {}
    with open("events.json", "r") as f:
        freebies = json.loads(f.read())
    return render_template('index.html', freebies=freebies)
