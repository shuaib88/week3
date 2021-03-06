# Divvy Bikes
#
# Here's an example of how to retrieve the list of Divvy bike stations:

##import json
##from urllib.request import urlopen
##
##webservice_url = "http://www.divvybikes.com/stations/json"
##data = urlopen(webservice_url).read().decode("utf8")
##result = json.loads(data)
##stations = result['stationBeanList']
##print(stations)

# The Young building has the following latitude and longitude: 41.793414,-87.600915.
# To measure surface distance, you can treat latitudes and longitudes like x and y coordinates, and calculate distance between locations with the usual Euclidean distance formula.
# 1. Modify the code above to display the station name and number of available bikes for the station closest to Young.
# You will likely want to consult the JSON stream from Divvy
# - http://www.divvybikes.com/stations/json


#My strategy:
#1)Append to a new a list that calculates [the distance from young,
#  station name, #of available bikes]
#2)print(station name and available bikes) of the first element of the new list
#  - which would be the shortest distance
# I know young has coordinates = 41.793414,-87.600915
# Nick Pann helped me trouble shoot my broken longitude calculation and work through
# a different strategy than my original- thanks Nick!

import json
from urllib.request import urlopen
import math

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']

print("this script will tell you the nearest station to young memorial hall and number of bikes available")
print()
confirm = input("Would you like to find closest station and number of available bikes? ")

if confirm == ("yes" or "Yes" or "YES"):
    youngLat = 41.793414
    youngLong = -87.600915
    stationsByDistance = []

    for station in stations:
        surfaceDistance = math.sqrt(((station['latitude'] - youngLat) ** 2) + ((station['longitude'])- youngLong) ** 2)
        stationsByDistance.append([surfaceDistance, station['stationName'], station['availableBikes']]) 

    stationsByDistance = sorted(stationsByDistance)

    print(stationsByDistance[0][1], "is the nearest station and it has", stationsByDistance[0][2],
          "available bikes")

else:
    print("Sorry, that's all I can do for now")


