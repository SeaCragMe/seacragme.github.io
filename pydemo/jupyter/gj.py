
import pandas as pd
import pands.io.data as web 
import datetime as dt

start = dt.datetime(2018,9,1)
end = dt.date.today()

AAPL = web.DataReader('AAPL','yahoo',start,end)
