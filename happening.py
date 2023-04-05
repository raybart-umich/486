from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from helpers import check_for_freebies

def get_events_happening(url):
    """Retrieve events from URL."""
    events = []
    base = 'https://events.umich.edu'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')
    results = soup.findAll(True, {'class':['event-listing', 'event-listing event-single']})

    for result in results:
        href = result.find(class_='btn learn-more').attrs['href']
        url = base + href
        events.append(url)

    return events


def filter_events_happening(events):
    freebie_events = []
    for url in events:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        try:
            description = soup.find(class_='event-description-text').text
            if check_for_freebies(description):
                title = soup.find(class_='title').text
                freebie_events.append((url, title))
        except:
            continue
    return freebie_events
