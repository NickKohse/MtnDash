import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import logging
import flask

import weather_api

from constants import *

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.title = "MTNDash"

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
        if today.weekday() > 4:
            x_axis.append(f"<b>{today.strftime('%m/%d')}</b>")
        else:
            x_axis.append(today.strftime('%m/%d'))
        today += timedelta(days = 1)
 
    return x_axis

base_elements = [
    html.H1(
        children = 'MTNDash',
        style = {
            'textAlign': 'center',
            'marginTop': '0px',
            'color': colours['dark grey'],
            'fontFamily': ['Roboto', 'sans-serif'],
            'fontSize': '50px',
        }
    ),
    html.Div(children = 'Condition reports for the Southern Canadian Rockies.', style = {
        'textAlign': 'center',
        'color': colours['dark grey'],
        'fontFamily': ['Roboto', 'sans-serif'],
    })
]

def serve():
    elements = base_elements.copy()

    for location in locations:
        elements.append(html.H2(children = f"{location}: {weather_api.getCurrentTemp(locations[location][0], locations[location][1])}°", style = {
            'textAlign': 'left',
            'marginLeft': '10px',
            'color': colours['dark grey'],
            'fontFamily': ['Roboto', 'sans-serif'],
            'fontStyle': 'italic',
        }))

        x_labels = gen_x_axis_labels()
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.update_layout(
            plot_bgcolor = colours['background'],
            paper_bgcolor = colours['background'],
        )
        highs = weather_api.getWeeklyHighs(locations[location][0], locations[location][1])

        fig.add_trace(go.Scatter(
            x = x_labels,
            y = highs,
            name = "Temperature (°C)",
            line = {'color': colours['dark grey']},
        ),
        secondary_y = False,
        )

        fig.add_trace(go.Scatter(
            x = x_labels,
            y = weather_api.getWeeklyPercip(locations[location][0], locations[location][1]),
            name = "POP (%)",
            line = {'color': colours['pale teal']},
        ),
        secondary_y = True,
        )

        fig.update_yaxes(title_text="Temperature", range=[0 if min(highs) > 0 else min(highs), max(highs) + 1], secondary_y=False)
        fig.update_yaxes(title_text="POP", range=[0,100], secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True)


        elements.append(dcc.Graph(figure = fig))
   
    return html.Div(style={'backgroundColor': colours['background']}, children = elements)

app.layout = serve # This makes the page run the serve function on reload

if __name__ == '__main__':
    logging.basicConfig(filename='mtndash.log', level=logging.getLevelName(LOG_LEVEL), format='%(asctime)s %(message)s')
    logging.info('Starting Server...')
    app.run_server(debug = True)
