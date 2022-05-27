import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from datetime import datetime, timedelta

from weather_api import getCurrentTemp
from weather_api import getWeeklyHighs
from weather_api import getWeeklyPercip

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
    'pale teal': '#7185AA'
}

def gen_x_axis_labels():
    today = datetime.now()
    x_axis = []

    for _ in range(8):
        x_axis.append(today.strftime("%d/%m"))
        today += timedelta(days = 1)
 
    return x_axis

elements = [
    html.H1(
        children = 'MTNDash',
        style = {
            'textAlign': 'center',
            'color': colours['dark grey'],
            'font-family': ['Roboto', 'sans-serif'],
            'font-size': '50px'
        }
    ),
    html.Div(children = 'Condition reports for the Southern Canadian Rockies.', style = {
        'textAlign': 'center',
        'color': colours['dark grey'],
        'font-family': ['Roboto', 'sans-serif'],
    })
]

for location in locations:
    elements.append(html.H2(children = f"{location} Current Temp: {getCurrentTemp(locations[location][0], locations[location][1])}", style = {
        'textAlign': 'left',
        'color': colours['dark grey'],
        'font-family': ['Roboto', 'sans-serif'],
        'font-style': 'italic',
    }))

    x_labels = gen_x_axis_labels()
    fig = go.Figure(data=go.Scatter(
        x = x_labels,
        y = getWeeklyHighs(locations[location][0], locations[location][1]),
        name = "Temp (C)",
        line = {'color': colours['dark grey']},
    ), layout = {
        'plot_bgcolor': colours['background'],
        'paper_bgcolor': colours['background'],
    })

    fig.add_trace(go.Scatter(
        x = x_labels,
        y = getWeeklyPercip(locations[location][0], locations[location][1]),
        name = "Rain (mm)",
        line = {'color': colours['pale teal']},
    ))

    elements.append(dcc.Graph(figure = fig))

app = dash.Dash()

app.layout = html.Div(style={'backgroundColor': colours['background']}, children = elements)

if __name__ == '__main__':
    app.run_server(debug = True)
