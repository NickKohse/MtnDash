# MTNDash

## About
A Dashboard to report weather conditions of the Southern Rockies of Canada

## TODO
- switch rain mm chart to bar graph of pop
- Read host/port from env for start.sh file
- Script updating of server (i.e. pull newest code and restart service)
- Somewhat inefficient, seems to call serve funtion 2x per load (possibly only for dev server)
- Figure out how often it calls the api, report it somehow
- add interval: https://dash.plotly.com/live-updates - can be quiet long 20+ minutes even an hour or more
- Better/any error handling
- Add snow forecasts (have them switch with rain forecasts at appropriate time), probably want snow as volume not chance
- Find a better way to add cities than changing code
- Fix white border on site to be background colour

## Setup
- Create venv called mtn
- `pip install requirements.txt`

### Dev server
- `python3 mtndash.py`
### Deployment server
- `gunicorn mtndash:server -b 0.0.0.0:8000`