from pathlib import Path

API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall?'
KELVIN = 273.15
WEATHER_API_KEY = Path('key').read_text().replace('\n', '')
CACHE_TTL = 600 #seconds