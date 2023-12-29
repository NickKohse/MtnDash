# MTNDash

## About
A Dashboard to report weather conditions of the Southern Rockies of Canada

## TODO
- Confirm that pop % works for snow as well as rain
- Also see if its possible to fetch data in parallel, initial load time is slow
- Make the chart uneditable
- add interval: https://dash.plotly.com/live-updates - can be quiet long 20+ minutes even an hour or more
- Better/any error handling
- Add snow forecasts (have them switch with rain forecasts at appropriate time), probably want snow as volume not chance
- Find a better way to add cities than changing code
- Ability to drill down in the weekly forcast graph to overlay an hour by hour for a given day when clicked

## Setup
- Create venv called mtn `python3 -m venv mtn`
- Activate it `source mtn/bin/activate`
- `pip install -r requirements.txt`
- Set the WEATHER_API_KEY env var or place the api key in a file called key, this must be a valid api key for: `api.openweathermap.org`

### Dev server
- `python3 mtndash.py`

### Deployment server
- `gunicorn mtndash:server -b 0.0.0.0:8000`
