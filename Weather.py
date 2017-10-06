from weather import Weather
import urllib2
import json


# Automatically geolocate the connecting IP
def geolocate():
    f = urllib2.urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    # location_city = location['city']
    # location_state = location['region_name']
    # location_country = location['country_name']
    # location_zip = location['zip_code']
    return location


def getweather(location):
    weather = Weather()
    lookup = weather.lookup_by_location(location)
    condition = lookup.condition()
    return condition


if __name__ == "__main__":
    getweather('Ithaca')

