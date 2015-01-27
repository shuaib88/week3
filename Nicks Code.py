import json
import math
from urllib.request import urlopen

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']

response = input('\nWould you like to find the nearest station to Young? Type "yes": ')
if response.lower() == 'yes':
	coords = [41.793414, -87.600915]
elif response.lower() == 'amli':
	coords = [41.889924, -87.630693]
else:
	print("Finding the nearest station to Young Memorial Building...")
	coords = [41.793414, -87.600915]

stations_nearby = []

for station in stations:
	surface_distance = math.sqrt((coords[0] - station['latitude'])**2 + (coords[1] - station['longitude'])**2)
	stations_nearby.append([surface_distance, station['stationName'], station['availableBikes']])

stations_nearby = sorted(stations_nearby)
closest_station = stations_nearby[0]
print('The nearest station is:', closest_station[1])
print('There are', closest_station[2], 'bikes currently available.')
