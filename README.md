# MTNDash

## About
A Dashboard to report weather conditions of the Southern Rockies of Canada

## TODO
- Get ready to deploy -specifically making a real service
- switch rain mm chart to bar graph of pop
- Script updating of server (i.e. pull newest code and restart server process)
- Somewhat inefficient, seems to call serve funtion 2x per load (possibly only for dev server)
- Figure out how often it calls the api, report it somehow
- Highlight the weekends in the graph somehow
- add interval: https://dash.plotly.com/live-updates - can be quiet long 20+ minutes
- Better/any error handling
- Add snow forecasts (have them switch with rain forecasts at appropriate time), probably want snow as volume not chance
- Find a better way to add cities than changing code
- Fix white border on site to be background colour

## Setup
- Create venv
- `pip install requirements.txt`
- 
### Dev server
- `python3 mtndash.py`
### Deployment server
- `gunicorn mtndash:server -b 0.0.0.0:8000`