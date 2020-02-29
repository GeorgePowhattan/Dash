import pandas as pd
import numpy as np
from datetime import datetime
import random

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


engine = sqlalchemy.create_engine('sqlite:///site.db', echo=True)

Base = declarative_base()

session = sessionmaker(bind=engine)()


def read_data(url):
    df = pd.read_csv(url, sep='|',skiprows=0,verbose=False,encoding ='utf-8',header=0)
    df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])
    return df

# db tables:
class Loans(Base):
    id = Column(Integer,primary_key=True)
    date = Column(Float,)
    date = Column(Float,)


if __name__ == '__main__':

    url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=1538&p_uka=1%2C2%2C3&p_strid=AAD&p_od=200512&p_do=209912&p_lang=CS&p_format=2&p_decsep=.'

    # Get the df:
    loans = read_data(url)

    # Nasypat df do db: Jak manipuovat s celymi radky?
