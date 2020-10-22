import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

import os
import pandas as pd

# Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=external_stylesheets)

# Tables
data['loans_rel'] = pd.read_csv()


app.layout = html.Div(children=[
        
      
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
