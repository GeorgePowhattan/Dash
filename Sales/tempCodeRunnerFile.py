import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

# Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__) #external_stylesheets=external_stylesheets

basedir = os.path.dirname(os.path.abspath(__file__))
path_to_basedir = str(basedir) + '/data.csv'

# Tables
df = pd.read_csv(path_to_basedir)
df['datetime'] = pd.to_datetime(df['datetime'])
df['month'] = df['datetime'].dt.month

app.layout = html.Div([
    html.Div([
        html.H1('Sales data 2019-2020')],
        style={'width': 500, 'padding': 10} ),
    
    html.Div(children=[
        html.Div([
            html.H3('Total earned:'),
            html.H1('{:,d} Kc'.format(df['FX'].sum()).replace(',',' '))
        ], style={'padding': 10}),
        html.Div([
            html.H3('Total earned (selected month):'),
            html.H1(id='info-sum-month')
        ], style={'padding': 10}),
        html.Div([
            html.H3('Total deals:'),
            html.H1(id='info-count') 
        ], style={'padding': 10})
    ], style={'columnCount': 3}),
    
    html.Br(),
    
    dcc.Slider(
            id='month-slider',
            min=0,
            max=12,
            step=1,
            value=1,
            marks={
                1: 'Jan',
                2: 'Feb',
                3: 'Mar',
                4: 'Apr',
                5: 'May',
                6: 'Jun',
                7: 'Jul',
                8: 'Aug',
                9: 'Sep',
                10: 'Oct',
                11: 'Nov',
                12: 'Dec'
            },
            
        ),
    dcc.Graph('graph'),
    html.Br(),
    html.Div('Some more charts...')

], style={'font-family': 'verdana'})

@app.callback(
    Output('graph', 'figure'),
    [Input('month-slider', 'value')])
def update_figure(selected_month):
    df_group = df[df['month'] == selected_month]
    df_group = df_group.groupby('Region').sum()

    fig = px.bar(df_group, x=df_group.index, y="FX",
        title="Celkove poplatky v danem mesici podle kraje "
        )

    fig.update_layout()

    return fig


@app.callback(
    Output('info-sum-month', 'children'),
    [Input('month-slider', 'value')])
def infoFigure(selected_month):
    df_filtered = df[df['month'] == selected_month]
    return ('{:,d} Kc'.format(df_filtered['FX'].sum()).replace(',',' '))


@app.callback(
    Output('info-count', 'children'),
    [Input('month-slider', 'value')])
def infoCount(selected_month):
    df_filtered = df[df['month'] == selected_month]
    return ('{:,d} x'.format(df_filtered['FX'].count()).replace(',',' '))


if __name__ == '__main__':
    app.run_server(debug=True)
