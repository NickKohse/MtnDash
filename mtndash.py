import dash
import dash_core_components as dcc
import dash_html_components as html
import requests as req
import json

weather_api_key = '75b76641c30c59ca0b51812fc7b1edd0'
api_endpoint = 'https://api.openweathermap.org/data/2.5/onecall?'
kelvin = 273.15

locations = {
    'Canmore': [51.07, -115.34],
    'Banff': [51.18, -115.57],
    'Bragg Creek': [50.95, -114.57],
    'Lake Louise': [51.42, -116.17],
    'Radium': [50.61, -116.07],
}

colours = {
    'background': '#B1B6A6',
    'text': '#7FDBFF',
    'dark grey': '#363946',
    'light grey': '#696773',
    'pale teal': '#819595'
}

def getLocationData(lat, lon):
    response = req.get(f'{api_endpoint}lat={lat}&lon={lon}&exclude=minutely,hourly&appid={weather_api_key}')
    data = json.loads(response.text)
    return data['current']['temp']


#response = req.get(f'{api_endpoint}lat={50}&lon={-114}&exclude=minutely,hourly&appid={weather_api_key}')
#temp = json.loads(response.text)
#temp = temp['current']['temp']

elements = [
    html.H1(
        children = 'MTNDash',
        style = {
            'textAlign': 'center',
            'color': colours['dark grey'],
            'font-family': ['Roboto', 'sans-serif'],
        }
    ),
    html.Div(children = 'Condition reports for the Southern Canadian Rockies.', style = {
        'textAlign': 'center',
        'color': colours['dark grey'],
        'font-family': ['Roboto', 'sans-serif'],
    })
]

for location in locations:
    elements.append(html.H2(children = f"{location} Current Temp: {round(getLocationData(locations[location][0], locations[location][1]) - kelvin, 1)}", style = {
        'textAlign': 'left',
        'color': colours['dark grey'],
        'font-family': ['Roboto', 'sans-serif'],
        'font-style': 'italic',
    }))

app = dash.Dash()

app.layout = html.Div(style={'backgroundColor': colours['background']}, children = elements)

if __name__ == '__main__':
    app.run_server(debug = True)
