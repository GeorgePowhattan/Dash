import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
])


if __name__ == '__main__':
    app.run_server(debug=True)