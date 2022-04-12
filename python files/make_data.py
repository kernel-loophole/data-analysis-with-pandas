import pandas as pd
from sympy import print_jscode

def make_data(file_name):
    df = pd.read_csv(file_name)
    # print(df.all())
    # print(df.head())
    # print(df.tail())
    # print(df.describe())
    # print(df.info())
    # print(df.columns)
    # print(df.index)
    # print(df.values)
    # print(df.iloc[0])
    print(df.iloc[[0,2],2:5])
    print(df)
    
    
    # return df
print(make_data('/home/hiader/Downloads/sample.csv'))
