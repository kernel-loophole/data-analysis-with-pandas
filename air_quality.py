from matplotlib.pyplot import axes
import pandas as pd
import numpy as np
from matplotlib.pyplot import plt
air_quality=pd.read_csv("NO2.csv")
air_quality=air_quality.rename(columns={"utc":"datetime"})
print(air_quality.head(5))
print(list(air_quality.columns.values))
print(air_quality["location"].unique())
air_quality["datetime"]=pd.to_datetime(air_quality["datetime"])
print("max is ")
print(air_quality["datetime"].max())
print("min")
print(air_quality["datetime"].min())
print("difference")
print(air_quality["datetime"].max()-air_quality["datetime"].min())
air_quality["Month"]=air_quality["datetime"].dt.month
air_quality["week"]=air_quality["datetime"].dt.week
print(air_quality.head(4))
x=air_quality.groupby([air_quality["datetime"].dt.weekday,"location"])["value"].mean()
print(x)
fig,axs=plt.subplots(figsize=(14,7))
x.plot(kind="bar",rot=0,ax=axs)
plt.xlabel("hours")
plt.ylabel("NO2")