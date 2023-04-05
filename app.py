from flask import Flask, render_template
from datetime import date, timedelta

from happening import get_events_happening
from happening import filter_events_happening

app = Flask(__name__, template_folder='templates/', static_folder='static/')


@app.route('/')
def home():
    events = []
    freebies = []
    for day in (date.today() + timedelta(n) for n in range(7)):
        events.extend(get_events_happening('https://events.umich.edu/day/' + str(day)))
    freebies.extend(filter_events_happening(events))

    return render_template('index.html', freebies=freebies)