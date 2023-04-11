from datetime import date, timedelta
import re
from unidecode import unidecode
from helpers import check_for_freebies, get_soup


def get_events_sessions(url):
    """Retrieve events from URL."""
    events = []

    soup = get_soup(url)

    regex = re.compile('.*panel panel-default track track-.*')
    results = soup.find_all("div", {"class" : regex})

    for result in results:
        date_header = result.contents[3].text.strip()
        for day in (date.today() + timedelta(n) for n in range(7)):
            date_string = day.strftime("%B %-d, %Y")
            if date_string in date_header:
                events.append((result, day))
                break
    return events


def filter_events_sessions(events):
    """Limits events to those that are relevant."""
    freebie_events = []
    base = 'https://sessions.studentlife.umich.edu'
    for event in events:
        description = event[0].find_all("div", {"class" : "description"})[0].text.strip()
        if check_for_freebies(description):
            title = event[0].find("h3", {"class": "panel-title"}).text.strip()
            url = str(event[0].find("a")['href'])
            url = base + url
            freebie_events.append((url, unidecode(title.strip()), event[1]))
    return freebie_events

