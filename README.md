# MTNDash

## About
A Dashboard to report weather conditions of the Southern Rockies of Canada

## TODO
- Confirm that pop % works for snow as well as rain
- Also see if its possible to fetch data in parallel, initial load time is slow
- add interval: https://dash.plotly.com/live-updates - can be quiet long 20+ minutes even an hour or more
- Better/any error handling
- Add snow forecasts (have them switch with rain forecasts at appropriate time), probably want snow as volume not chance
- Find a better way to add cities than changing code

## Setup
- Create venv called mtn
- `pip install requirements.txt`

### Dev server
- `python3 mtndash.py`
### Deployment server
- `gunicorn mtndash:server -b 0.0.0.0:8000`