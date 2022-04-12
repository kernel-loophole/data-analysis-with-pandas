import pandas as pd
import numpy as np
from sqlalchemy import column
import matplotlib.pyplot as plt
air_quality=pd.read_csv("NO2.csv")
print(air_quality)
# london_data=air_quality.groupby("city")
london=air_quality[air_quality["city"]=="London"]
print(london)
# df.columns=[col[2:-1] for col in df.columns]
# change_col=df.columns[0]
# change_col1=df.columns[1]
# change_col3=df.columns[3]
# df=df.rename(columns={change_col:"last name",change_col3:"Test1"})
# print(df["Final"].mean)

# # isin check for either vlaue is 41,30,34,37 and height > 60
# age_30=df[(df["Age"].isin([41,30,34,37])) &  (df["Height (in)"]>60) ]
# get_name=df.loc[df["Age"]>41,["Name","Height (in)"]]
# print(age_30)
# print("#######")
# print((get_name))
# print("row and cloumns")
# # from row 2 to 9 and colum 3 to 4
# print(df.iloc[2:10,3:5])
# print(get_name.plot())

