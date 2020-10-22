import pandas as pd
import os
import unicodedata

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, Float

basedir = os.path.dirname(os.path.abspath(__file__))
path = 'sqlite:///' + str(basedir) + '/data.db'

engine = sqlalchemy.create_engine(path, echo=True)  # sqlite:////absolute/path/to/database
Base = declarative_base()
session = sessionmaker(bind=engine)()

# Smaze hacky a carky:
def diakritika(input_string):
    input_string = unicodedata.normalize('NFKD', input_string)
    output = ''
    for c in input_string:
        if not unicodedata.combining(c):
            output += c
    return output 

def read_data(url):
    df = pd.read_csv(url, sep='|',skiprows=0,verbose=False,encoding ='utf-8',header=0)
    # df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])
    df.dropna(axis=0, inplace=True)
    df.columns = [diakritika(column) for column in df.columns]
    return df


if __name__ == "__main__":
    
    tables = ['loans', 'rates', 'gdp', 'cpi']

    urls = dict(
    loans_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=1538&p_uka=1%2C2%2C3&p_strid=AAD&p_od=200512&p_do=209912&p_lang=CS&p_format=2&p_decsep=.',
    rates_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=49609&p_uka=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14&p_strid=AAD&p_od=200401&p_do=209912&p_lang=CS&p_format=2&p_decsep=.',
    gdp_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=3&p_sort=1&p_des=50&p_sestuid=29930&p_uka=1%2C2%2C3%2C4%2C5&p_strid=ACL&p_od=199603&p_do=209909&p_lang=CS&p_format=2&p_decsep=.',
    cpi_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=6546&p_uka=1%2C2%2C3%2C4&p_strid=ACL&p_od=200001&p_do=209909&p_lang=CS&p_format=2&p_decsep=.'
    )
    
    data = {}

    for table, url in zip(tables, urls):
        data[table] = read_data(urls[url])
        data[table].to_sql(table, con=engine, if_exists='replace')

