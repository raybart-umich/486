from flask import Flask, render_template
import json

app = Flask(__name__, template_folder='templates/', static_folder='static/')

@app.route('/')
def home():
    freebies = {}
    with open("/home/martinvv/FreebieFinder/events.txt", "r") as f:
        freebies = json.loads(f.read())
    return render_template('index.html', freebies=freebies)
