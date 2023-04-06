from flask import Flask, render_template
from datetime import date, timedelta

from happening import get_events_happening
from happening import filter_events_happening

app = Flask(__name__, template_folder='templates/', static_folder='static/')


@app.route('/')
def home():
    events = {}
    freebies = {}
    for day in (date.today() + timedelta(n) for n in range(7)):
        if day in events:
            events[day].extend(get_events_happening('https://events.umich.edu/day/' + str(day)))
        else:
            events[day] = [get_events_happening('https://events.umich.edu/day/' + str(day))]
    for day in events:
        dayo = day.strftime("%A %B %d")
        if dayo in freebies:
            freebies[dayo].extend(filter_events_happening(events[day][0]))
        else:
            freebies[dayo] = [filter_events_happening(events[day][0])]

    return render_template('index.html', freebies=freebies)