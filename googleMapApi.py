#This program well let you input an address:
#    Young Memorial Hall 5555 South Ellis Avenue, Chicago, U.S.
#Then it will output:
#   1)The nearest station
#   2)The number of bikes currently available


# Geocoding

# Determine the geocoordinates of these famous Chicago landmarks:
#
# United Center
# Millenium Park
# Sears Tower
# Young Memorial Building
#
# You can:
# - web: http://maps.google.com combined with the "What's Here?" trick
# - webservice: https://developers.google.com/maps/documentation/geocoding/#JSON


import json
from urllib.request import urlopen
##^what does this horseMeat mean? :)


url = "https://maps.googleapis.com/maps/api/geocode/json?address=Millenium+park+Chicago"
data = urlopen(url).read().decode("utf8")
# print(data)
result = json.loads(data)

longitude = result['results'][0]['geometry']['location']['lng']
print("The longitude is", longitude)


