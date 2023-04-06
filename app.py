from flask import Flask, render_template
from datetime import date, timedelta

from happening import get_events_happening
from happening import filter_events_happening

app = Flask(__name__, template_folder='templates/', static_folder='static/')


@app.route('/')
def home():
    freebies = []
    with open('events.txt', 'r') as f:
        for line in f:
            freebies.append(line.rstrip().split('\t'))

    return render_template('index.html', freebies=freebies)
