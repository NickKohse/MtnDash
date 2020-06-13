import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

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
    'pale teal': '#819595'
}


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
    elements.append(html.H2(children = f"{location} Current Temp: {getCurrentTemp(locations[location][0], locations[location][1])}", style = {
        'textAlign': 'left',
        'color': colours['dark grey'],
        'font-family': ['Roboto', 'sans-serif'],
        'font-style': 'italic',
    }))

    fig = go.Figure(data=go.Scatter(
        x = [1,2,3,4,5,6,7,8],
        y = getWeeklyHighs(locations[location][0], locations[location][1]),
    ), layout = {
        'plot_bgcolor': colours['background'],
        'paper_bgcolor': colours['background'],
    })

    fig.add_trace(go.Scatter(x = [1,2,3,4,5,6,7,8], y = getWeeklyPercip(locations[location][0], locations[location][1])))

    elements.append(dcc.Graph(figure = fig))

app = dash.Dash()

app.layout = html.Div(style={'backgroundColor': colours['background']}, children = elements)

if __name__ == '__main__':
    app.run_server(debug = True)
