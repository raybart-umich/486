EECS 486 Final Project - Freebie Finder

This code pulls events from Sessions @ Michigan and Happening @ Michigan, determines whether the events have free food/items offered at them, and displays those events on a calander for the next seven days.

static: The static folder contains the images and the css used in the front-end creation of the webpage that displays all of the events.

templates: The templates folder contains the html file that houses all of the content for the webpage.

app.py: This file puts together the functions in happening.py. For a certain date range, this file gathers and then filters the events from both websites. This is the file accessed by the html file for the event information and links.

happening.py: This file has functions that scrape both websites for events and then filters down those events.

helpers.py: This file contains the function we use to filer through events to determine whether or not there are free things offered at said events.

requirements.txt: This file contains all the libraries needed to execute the code.