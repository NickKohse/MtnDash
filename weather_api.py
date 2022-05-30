import requests as req
import json
import time

from constants import *

global cache
cache = {}

class DataTimePair:
    def __init__(self, data, time):
        self.jsonData = data
        self.time = time

##
# Takes 2 floats representing the latitude and longitude of a location
# Returns the current temp in celcius at that location
##
def getCurrentTemp(lat, lon):
    data = getLocationData(lat,lon)
    return round(data['current']['temp'] - KELVIN, 1)

##
# Takes 2 floats representing the latitude and longitude of a location
# Returns a week worth of daily high temps in celcius in an array
##
def getWeeklyHighs(lat, lon):
    data = getLocationData(lat,lon)
    return *map(lambda obj: round(obj['temp']['max'] - KELVIN, 1), data['daily']),

##
# Takes 2 floats representing the latitude and longitude of a location
# Returns a weeks worth of rain amounts in mm(?) in an array
##
def getWeeklyPercip(lat, lon):
    data = getLocationData(lat,lon)
    return *map(lambda obj: round(obj['rain'], 1) if 'rain' in obj else 0.0, data['daily']),

##
# Takes 2 floats representing the latitude and longitude of a location
# Checks if we've done the search for this location in the last CACHE_TTL
# seconds, and if so returns the saved info, otherwise hits the api
# Returns the full json data
##
def getLocationData(lat, lon):
    location = f'{lat}{lon}'
    currentTime = int(time.time())
    print(cache)
    if location in cache:
        if (currentTime - cache[location].time) < CACHE_TTL:
            print("Hitting cache")
            return cache[location].jsonData

    print("Missed cache")    
    # If it doesn't exist in cache or it's expired we need to hit the api 
    response = req.get(f'{API_ENDPOINT}lat={lat}&lon={lon}&exclude=minutely,hourly&appid={WEATHER_API_KEY}')
    data = json.loads(response.text)
    # Update cache
    cache[location] = DataTimePair(data, currentTime)
    return data
