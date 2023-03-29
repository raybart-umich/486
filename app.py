import os

from flask import Flask, render_template
from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates/', static_folder='static/')


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
                title = soup.find(class_='title').text
                freebie_events.append((url, title))
        except:
            continue
    return freebie_events


def check_for_freebies(description):
    if 'free' in str(description):
        return True
    return False


@app.route('/')
def home():
    events = get_events('https://events.umich.edu/day/2023-03-29')
    freebies = filter_events(events)

    return render_template('index.html', freebies=freebies)