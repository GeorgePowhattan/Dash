import sqlite3
import os
import pandas as pd

basedir = os.path.dirname(os.path.abspath(__file__))
path = str(basedir)+'/data.db'

conn = sqlite3.connect(path)
c = conn.cursor()

url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=1538&p_uka=1%2C2%2C3&p_strid=AAD&p_od=200512&p_do=204912&p_lang=CS&p_format=2&p_decsep=.'


def read_data(url):
    
    df = pd.read_csv(url, sep='|',skiprows=0,verbose=False,encoding ='utf-8',header=0)
    df.dropna(axis=0, inplace=True)
    return df


def data_entry():
    
    c.execute('DELETE from loans')

    loans = read_data(url)
    cols = list(loans.columns)

    for index, row in loans.iterrows():
    
        datum, spotreba, bydleni, ostatni = row[cols[0]],row[cols[1]],row[cols[2]],row[cols[3]]

        c.execute('INSERT INTO loans (datum, spotreba, bydleni, ostatni) VALUES (?,?,?,?)', (datum, spotreba, bydleni, ostatni))
    
    conn.commit()
    c.close()
    conn.close()


if __name__ == "__main__":
    
    data_entry()