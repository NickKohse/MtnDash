from pathlib import Path
import os

API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/'
KELVIN = 273.15
WEATHER_API_KEY = os.environ['WEATHER_API_KEY'] if 'WEATHER_API_KEY' in os.environ else Path('key').read_text().replace('\n', '')
CACHE_TTL = int(os.environ['CACHE_TTL']) if 'CACHE_TTL' in os.environ else 600 #seconds
LOG_LEVEL = os.environ['LOG_LEVEL'] if 'LOG_LEVEL' in os.environ else 'DEBUG'