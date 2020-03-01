import pandas as pd
import numpy as np
from datetime import datetime
import random

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, Float


engine = sqlalchemy.create_engine('sqlite:///site.db', echo=True)  # sqlite:////absolute/path/to/database
Base = declarative_base()
session = sessionmaker(bind=engine)()

# Scrape the data from web into dataframe:
def read_data(url):
    df = pd.read_csv(url, sep='|',skiprows=0,verbose=False,encoding ='utf-8',header=0)
    df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])
    df.dropna(axis=0, inplace=True)
    return df

# Database:
class Loans(Base):
    id = Column(Integer, primary_key=True)
    datum = Column(Date)
    spotreba = Column(Float)
    bydleni = Column(Float)
    ostatni = Column(Float)
    def __repr__(self):
        return("Loans: {}, {}, {}, {}".format(self.datum,self.spotreba,self.bydleni,self.ostatni))

if __name__ == '__main__':

    url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=1538&p_uka=1%2C2%2C3&p_strid=AAD&p_od=200512&p_do=209912&p_lang=CS&p_format=2&p_decsep=.'

    # Get the df:
    loans = read_data(url)

    # Nasypat df do db: Jak manipulovat s celymi radky?
    for 