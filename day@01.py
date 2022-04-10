from operator import index
import pandas as pd
from sqlalchemy import false

from stringcolor import *
def simple_data():
    data_frame=pd.DataFrame({
        "Name":["ali","zain","junaid"],
        "age":[20,15,15],
        "sex":["male","male","male"]
    })

    print(data_frame.describe())
    print("MAX FROM Dataset",data_frame["age"].max())
def read_from_csv(filename):
    with open (filename) as f:
        dataset=pd.read_csv(f)
    print(dataset.head(10))
    print(dataset.dtypes)
    print(dataset.info())
    return dataset     
def data_set_excel(dataset):
    dataset.to_excel("excel.xlsx",sheet_name='excel',index=False)
    print("done ")
if __name__=="__main__":
    dataset=read_from_csv("cities.csv")
    data_set_excel(dataset)
    print("dataframe with lad >50")
    lad=dataset[dataset["LatD"]>30]
    lad=lad["LatD"]
    print(lad)
    