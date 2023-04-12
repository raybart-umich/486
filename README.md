# EECS 486 Final Project - Freebie Finder
<https://www.umichfreebies.com/>

You can check out FreebieFinder at any time at the link above. However, if you wish to run FreebieFinder locally for any reason, you can simply follow our instructions below.

## Install dependencies
Before getting started, make sure you have all dependencies installed by running the following command:
```
pip3 install -r requirements.txt
```

## Run the scraping script
The first step is to execute the script that gathers events from *Happening @ Michigan* and *Sessions @ Michigan*. Be aware that this code may take a couple minutes to run. That's why it only gets executed once a day! Run the following command to scrape these events:
```
python3 get_events.py
```
After execution, *`events.json`* should now contain a JSON object with all the information we need to render FreebieFinder.

## Run the Flask app
At this point, we're ready to set up the page. You can run the following command to start our Flask app:
```
flask run
```
## Open FreebieFinder
Finally, now that our Flask app is up and running, we get to see what sort of events are being hosted at the University of Michigan! By default, the page is being run on port 5000, but feel free to change this in your Flask command. 

Open your browser of choice and navigate to *`127.0.0.1:5000/`* or *`localhost:5000/`* to check out FreebieFinder!


---

## Project files and info
FreebieFinder pulls events from Sessions @ Michigan and Happening @ Michigan, determines whether the events have free food/items offered at them, and displays those events on a calander for the next seven days.

*`static`*: The static folder contains the images and the css used in the front-end creation of the webpage that displays all of the events.

*`templates`*: The templates folder contains the html file that houses all of the content for the webpage.

*`happening.py`*: This file has functions that scrape Happening@Michigan websites for events and then filters down those events.

*`sessions.py`*: This file contains functions that scrape Sessions@Michigan.

*`get_events.py`*: This file puts together the functions in happening.py and sessions.py. For a certain date range, this file gathers and then filters the events from both websites. It then stores these results in JSON format locally in events.txt.

*`app.py`*: This file reads events.txt, which contains our scraping output. It then renders this output into our webpage. This contains the Flask app.

*`helpers.py`*: This file contains the function we use to filter through events to determine whether or not there are free things offered at said events. It also contains our use of BeautifulSoup.

*`reload_script.py`*: This script uses PythonAnywhere's API to manually reload our page with new results. The script is scheduled to execute a couple minutes after new results have been fetched.

*`requirements.txt`*: This file contains all the libraries needed to execute the code.

*`annotated_data.txt`*: This file contains the manually labelled events that we used to calculate precision and recall for our project.
