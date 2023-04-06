from datetime import date, timedelta
import json

from happening import get_events_happening
from happening import filter_events_happening

if __name__ == "__main__":
    events = {}
    freebies = {}
    for day in (date.today() + timedelta(n) for n in range(7)):
        if day not in events:
            events[day] = []
        events[day].extend(get_events_happening('https://events.umich.edu/day/' + str(day)))
    for day in events:
        dayo = day.strftime("%A %B %d")
        if dayo not in freebies:
            freebies[dayo] = []
        freebies[dayo].extend(filter_events_happening(events[day]))
    with open("events.txt", "w") as f:
        f.write(json.dumps(freebies))
