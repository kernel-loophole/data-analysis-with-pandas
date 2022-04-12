from pydoc import describe
import pandas as pd
import numpy as np
from stringcolor import *
import openaq as op
from sympy import limit
api=op.OpenAQ()
data=api.measurements(id=["bc,co,no2"],limit=100,df=True)
print(list(data.columns.values))
data_pm25=pd.read_csv("pm25.csv",parse_dates=True)
data_no2=pd.read_csv("NO2.csv",parse_dates=True)
data_pm25=data_pm25[["location","city","utc","parameter","value"]]

data_no2=data_no2[["location", "city","utc","parameter","value"]]

# print(data_pm25.head(6))
# print(data_no2.head(5))
air_quality=pd.concat([data_no2,data_pm25],axis=0,keys=["no2","pm25"])
print(cs("shape of PM25:","red"),data_pm25.shape)
print(air_quality)
print(cs("shape of NO2:","red"),data_no2.shape)
print(cs("shape of total:","red"),air_quality.shape)
print("after sorting the data")
air_quality=air_quality.sort_values("utc")
print(air_quality)