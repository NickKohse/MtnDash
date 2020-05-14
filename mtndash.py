import dash
import dash_core_components as dcc
import dash_html_components as html
import requests as req
import json

weather_api_key = '75b76641c30c59ca0b51812fc7b1edd0'
api_endpoint = 'https://api.openweathermap.org/data/2.5/onecall?'

locations = {
    'Canmore': [51.07, -115.34],
    'Banff': [51.18, -115.57],
    'Bragg Creek': [50.95, -114.57],
    'Lake Louise': [51.42, -116.17],
    'Radium': [50.61, -116.07],
}

response = req.get(f'{api_endpoint}lat={50}&lon={-114}&exclude=minutely,hourly&appid={weather_api_key}')
temp = json.loads(response.text)
temp = temp['current']['temp']

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children = 'Hello Dash',
        style = {
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children = 'Dash: A web application framework for Python.', style = {
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id = 'Graph1',
        figure = {
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    dcc.Textarea(
        id = 'textarea-example',
        value = f'{round(temp - 273.15, 1)}',
        style = {'width': '100%', 'height': 300},
    ),
])

if __name__ == '__main__':
    app.run_server(debug = True)