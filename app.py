import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
        dcc.Tabs(id="tabs", value='tab-1', children=[
            # Tab 1
            dcc.Tab(label='Tab one', value='tab-1',children=[
                dcc.Graph(
                    id='example-graph1',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'CSOB'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Patria'},
                        ],
                        'layout': {
                            'title': 'Dash Data Visualization - Tab one'
                            }
                        }
                    )
            ]),
            # Tab 2
            dcc.Tab(label='Tab two', value='tab-2',children=[
                dcc.Graph(
                    id='example-graph2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [1, 2, 3], 'type': 'line', 'name': 'CSOB'},
                            {'x': [1, 2, 3], 'y': [3, 1, 2], 'type': 'line', 'name': 'Patria'},
                        ],
                        'layout': {
                            'title': 'Dash Data Visualization - Tab two'
                            }
                        }
                    )
                ]),   
            ]),
      
        ])


if __name__ == '__main__':
    app.run_server(debug=True)