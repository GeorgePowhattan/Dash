import dash
import dash_html_components as html
import dash_core_components as dcc

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, Float
import os
import time
from datetime import datetime
import pandas as pd

# Database
basedir = os.path.dirname(os.path.abspath(__file__))
path = 'sqlite:///' + str(basedir) + '/data.db'

engine = sqlalchemy.create_engine(path, echo=True)  # sqlite:////absolute/path/to/database
Base = declarative_base()
session = sessionmaker(bind=engine)()

# Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=external_stylesheets)

# Tables
tables = ['loans', 'rates', 'gdp', 'cpi']
data = {}
'''
for table in tables:
    data[table] = engine.execute("SELECT * FROM {}".format(str(table))).fetchall()
    data[table] = pd.DataFrame(data[table])
'''
data['loans'] = pd.read_sql("SELECT * FROM loans", engine)
#print(data['loans'].iloc[:,1])
#print(data['loans'].iloc[:,1:])
time.sleep(5)

app.layout = html.Div(children=[
        dcc.Tabs(id="tabs", value='tab-1', children=[
            # Tab 1
            dcc.Tab(label='Tab one', value='tab-1',children=[
                dcc.Graph(
                    id='example-graph1',
                    figure={
                        'data': [
                            dict(x= data['loans'].iloc[:,1], # [ datetime.strptime(data['loans'].iloc[:,1], '%d.%m.%Y') for row in data['loans'] ]
                                y=data['loans'].iloc[:,2],
                                type='line',
                                name='loans'),
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


#if __name__ == '__main__':
app.run_server(debug=True)