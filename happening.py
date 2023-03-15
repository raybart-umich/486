"""A scheduled task that runs every night, overwriting scores_2020s.py with updated scores."""
import os

from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup


title_scores = {}
file_path = 'happening_freebies.py'


def get_events(url):
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


def filter_events(events):
    freebie_events = []
    for url in events:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')
        try:
            description = soup.find(class_='event-description-text').text
            if check_for_freebies(description):
                freebie_events.append(url)
        except:
            continue
    return freebie_events


def check_for_freebies(description):
    if 'free' in str(description):
        return True
    return False


if __name__ == '__main__':
    events = get_events('https://events.umich.edu/day/2023-03-15')
    output = filter_events(events)

    # TEMP
    for event in output:
        print(event)