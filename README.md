EECS 486 Final Project - Freebie Finder

This code pulls events from Sessions @ Michigan and Happening @ Michigan, determines whether the events have free food/items offered at them, and displays those events on a calander for the next seven days.

static: The static folder contains the images and the css used in the front-end creation of the webpage that displays all of the events.

templates: The templates folder contains the html file that houses all of the content for the webpage.

happening.py: This file has functions that scrape Happening@Michigan websites for events and then filters down those events.

sessions.py: This file contains functions that scrape Sessions@Michigan.

get_events.py: This file puts together the functions in happening.py and sessions.py. For a certain date range, this file gathers and then filters the events from both websites. It then stores these results in JSON format locally in events.txt.

app.py: This file reads events.txt, which contains our scraping output. It then renders this output into our webpage. This contains the Flask app.

helpers.py: This file contains the function we use to filter through events to determine whether or not there are free things offered at said events. It also contains our use of BeautifulSoup.

reload_script.py: This script uses PythonAnywhere's API to manually reload our page with new results. The script is scheduled to execute a couple minutes after new results have been fetched.

requirements.txt: This file contains all the libraries needed to execute the code.

annotated_data.txt: This file contains the manually labelled events that we used to calculate precision and recall for our project.
