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
        surfaceDistance = math.sqrt(((station['latitude'] - youngLat) ** 2) + ((station['longitude']) ** 2)) 
        stationsByDistance.append([surfaceDistance, station['stationName'], station['availableBikes']]) 

    stationsByDistance = sorted(stationsByDistance)

    print(stationsByDistance[0][1], "is the nearest station and it has", stationsByDistance[0][2],
          "available bikes")

else:
    print("Sorry, that's all I can do for now")

##something is strange here - according to stationsByDistance - 'shore drive & 55th' is the closest
##However, when I look at google map I find the 'Ellis Ave & 58th St' is nearer,
##I double check the math
##however when i double check the math, according to coordinates spit out by divvy JSON, the result
##is correct
##Young 41.793414, -87.600915
##Ellis - 41.788838, -87.600990
##Shore - 41.795397, -87.579489
##
###shore to young
##eval(math.sqrt((41.795397 - 41.793414)**2 + (-87.579489 - -87.600915)**2)) = 
##
###ellis to shore
##eval(math.sqrt((41.788838 - 41.793414)**2 + (-87.579489 - -87.600990)**2))

