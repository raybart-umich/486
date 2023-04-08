from helpers import check_for_freebies, get_soup
from unidecode import unidecode


def get_events_happening(url):
    """Retrieve events from URL."""
    events = []
    base = 'https://events.umich.edu'

    soup = get_soup(url)
    results = soup.find_all(True, {'class':['event-listing', 'event-listing event-single']})

    for result in results:
        href = result.find(class_='btn learn-more').attrs['href']
        url = base + href
        events.append(url)

    return events


def filter_events_happening(events):
    freebie_events = []
    for url in events:
        soup = get_soup(url)
        try:
            description = soup.find(class_='event-description-text').text
            if check_for_freebies(description):
                title = soup.find(class_='title').text
                freebie_events.append((url, unidecode(title.strip())))
        except:
            continue
    return freebie_events
