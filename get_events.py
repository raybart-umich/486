from datetime import date, timedelta

from happening import get_events_happening
from happening import filter_events_happening

if __name__ == "__main__":
    events = []
    freebies = []
    for day in (date.today() + timedelta(n) for n in range(7)):
        events.extend(get_events_happening('https://events.umich.edu/day/' + str(day)))
        print("got new event")
    freebies.extend(filter_events_happening(events))
    with open("events.txt", "w") as f:
        for freebie in freebies:
            f.write(f"{freebie[0]}\t{freebie[1]}\n")
