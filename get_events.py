from datetime import date, timedelta
import json

from happening import get_events_happening
from happening import filter_events_happening
from sessions import get_events_sessions
from sessions import filter_events_sessions


def get_events():
    """
    Uses functions from happening.py, sessions.py, and helpers.py to
    retrieve relevant events and store them in our intended format.
    """
    events_happening = {}
    events_sessions = []
    freebies = {}
    for day in (date.today() + timedelta(n) for n in range(7)):
        if day not in events_happening:
            events_happening[day] = []
        events_happening[day].extend(get_events_happening('https://events.umich.edu/day/' + str(day)))
    for day in events_happening:
        dayo = day.strftime("%A %B %d")
        if dayo not in freebies:
            freebies[dayo] = []
        freebies[dayo].extend(filter_events_happening(events_happening[day]))
    
    events_sessions = filter_events_sessions(get_events_sessions('https://sessions.studentlife.umich.edu/list'))
    for session in events_sessions:
        dayo = session[2].strftime("%A %B %d")
        if dayo not in freebies:
            freebies[dayo] = []
        if not any(event[1] == session[1] for event in freebies[dayo]):
            freebies[dayo].append((session[0], session[1]))

    with open("events.json", "w") as f:
        f.write(json.dumps(freebies))
if __name__ == "__main__":
    get_events()