# MTNDash

## About
A Dashboard to report weather conditions of the Southern Rockies of Canada

## TODO
- Read config from ENV, api key cache TTL, log level etc, some might have defaults.
- Get ready to deploy
- investigate why data doesnt get reloaded
- Figure out how often it calls the api, report it somehow
- Highlight the weekends in the graph somehow
- DATA only refreshews on initial load (add interval: https://dash.plotly.com/live-updates)
- Better/any error handling
- Add snow forecasts (have them switch with rain forecasts at appropriate time)
- Find a better way to add cities than changing code
- Fix white border on site to be background colour

## Setup
- Create venv
- `pip install requirements.txt`
- 
### Dev server
- `python3 mtndash.py`
### Deployment server
- `gunicorn mtndash:app.server`
- `gunicorn mtndash:server -b :8080`