import pandas as pd
import numpy as np
from datetime import datetime
import random

chapters = ['loans', 'rates', 'gdp', 'cpi']

urls = dict(
loans_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=1538&p_uka=1%2C2%2C3&p_strid=AAD&p_od=200512&p_do=209912&p_lang=CS&p_format=2&p_decsep=.',
loans_total_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=44895&p_uka=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11&p_strid=AABBAA&p_od=200501&p_do=202512&p_lang=CS&p_format=2&p_decsep=.'
rates_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=49609&p_uka=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14&p_strid=AAD&p_od=200401&p_do=209912&p_lang=CS&p_format=2&p_decsep=.',
gdp_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=3&p_sort=1&p_des=50&p_sestuid=29930&p_uka=1%2C2%2C3%2C4%2C5&p_strid=ACL&p_od=199603&p_do=209909&p_lang=CS&p_format=2&p_decsep=.',
cpi_url = 'https://www.cnb.cz/cnb/STAT.ARADY_PKG.VYSTUP?p_period=1&p_sort=1&p_des=50&p_sestuid=6546&p_uka=1%2C2%2C3%2C4&p_strid=ACL&p_od=200001&p_do=209909&p_lang=CS&p_format=2&p_decsep=.'
)
# Source: https://www.cnb.cz/cnb/STAT.ARADY_PKG.hlavni_ukazatele?p_iframe=0&p_lang=CS












