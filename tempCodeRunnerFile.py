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
for table in tables:
    data[table] = pd.read_sql("SELECT * FROM {}".format(table), engine, parse_dates='Obdobi')

#print(data['loans'].iloc[:,1:])
#print(type(data['loans'].iloc[1,1]))
#print(data['loans'].iloc[1,1])
#print(data['loans']['Obdobi'])

app.layout = html.Div(children=[
        dcc.Tabs(id="tabs", value='tab-1', children=[
            
            # Tab 1
            dcc.Tab(label='Loans', value='tab-1',children=[
                dcc.Graph(
                    id='Loans absolute',
                    figure={
                        'data': [
                            dict(x= data['loans'].iloc[:,1],
                                y=data['loans'].iloc[:,2],
                                type='line',
                                name=data['loans'].columns[2]),
                            dict(x= data['loans'].iloc[:,1],
                                y=data['loans'].iloc[:,3],
                                type='line',
                                name=data['loans'].columns[3]),
                            dict(x= data['loans'].iloc[:,1],
                                y=data['loans'].iloc[:,4],
                                type='line',
                                name=data['loans'].columns[4])
                        ],
                        'layout': 
                            dict(title= 'Loans - total in CZK bil.',
                            traceorder="normal")
                            
                        }
                    ),
                dcc.Graph(
                    id='Loans relative',
                    figure={
                        'data': [
                            dict(x= data['loans'].iloc[:,1],
                                y=data['loans'].iloc[:,2],
                                type='line',
                                name=data['loans'].columns[2]),
                            dict(x= data['loans'].iloc[:,1],
                                y=data['loans'].iloc[:,3],
                                type='line',
                                name=data['loans'].columns[3]),
                            dict(x= data['loans'].iloc[:,1],
                                y=data['loans'].iloc[:,4],
                                type='line',
                                name=data['loans'].columns[4])
                        ],
                        'layout': 
                            dict(title= 'Loans - relative y/y change [%]',
                            traceorder="normal")
                            
                        }
                    )
            ]),
            
            # Tab 2
            dcc.Tab(label='Rates', value='tab-2',children=[
                dcc.Graph(
                    id='Tab2 Graph1',
                    figure={
                        'data': [
                            dict(x= data['rates'].iloc[:,1],
                                y=data['rates'].iloc[:,2],
                                type='line',
                                name=data['rates'].columns[2]),
                            dict(x= data['rates'].iloc[:,1],
                                y=data['rates'].iloc[:,3],
                                type='line',
                                name=data['rates'].columns[3]),
                            dict(x= data['rates'].iloc[:,1],
                                y=data['rates'].iloc[:,4],
                                type='line',
                                name=data['rates'].columns[4]),
                        ],
                        'layout': 
                            dict(title= 'Deposit rates [%]',
                                legend_orientation="h")
                            
                        }
                    ),
                dcc.Graph(
                    id='Tab2 Graph2',
                    figure={
                        'data': [
                            dict(x= data['rates'].iloc[:,1],
                                y=data['rates'].iloc[:,7],
                                type='line',
                                name=data['rates'].columns[7]),
                            dict(x= data['rates'].iloc[:,1],
                                y=data['rates'].iloc[:,8],
                                type='line',
                                name=data['rates'].columns[8]),
                            dict(x= data['rates'].iloc[:,1],
                                y=data['rates'].iloc[:,11],
                                type='line',
                                name=data['rates'].columns[11]),
                        ],
                        'layout': 
                            dict(title= 'Loan rates [%]',
                            )
                            
                        }
                    )
                ]),
            # Tab 3
            dcc.Tab(label='GDP', value='tab-3',children=[
                dcc.Graph(
                    id='Tab3 graph1',
                    figure={
                        'data': [
                            dict(x= data['gdp'].iloc[:,1],
                                y=data['gdp'].iloc[:,3],
                                type='line',
                                name=data['gdp'].columns[3]),
                            dict(x= data['gdp'].iloc[:,1],
                                y=data['gdp'].iloc[:,4],
                                type='line',
                                name=data['gdp'].columns[4])
                        ],
                        'layout': {
                            'title': 'GDP changes y/y [%]'
                            }
                        }
                    )
                ]),
            
            # Tab 4
            dcc.Tab(label='CPI', value='tab-4',children=[
                dcc.Graph(
                    id='Tab4 graph1',
                    figure={
                        'data': [
                            dict(x= data['cpi'].iloc[:,1],
                                y=data['cpi'].iloc[:,5],
                                type='line',
                                name=data['cpi'].columns[5])
                        ],
                        'layout': {
                            'title': 'Inflation [%]'
                            }
                        }
                    )
                ])   
            ])
      
        ])


#if __name__ == '__main__':
app.run_server(debug=True)
