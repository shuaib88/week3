# Divvy Bikes
#
# Here's an example of how to retrieve the list of Divvy bike stations:

import json
from urllib.request import urlopen

webservice_url = "http://shrouded-beach-2183.herokuapp.com/stations/328"
data = urlopen(webservice_url).read().decode("utf8")
#couldn't figure out how to query for a specific
#location, (I couldn't isolate the station 328 - because I didn't know
#what element it was in the list
#so i found a direct api for station 328 - the closes one to young


result = json.loads(data)
stations = result['properties']['availableDocks']

print(stations)
