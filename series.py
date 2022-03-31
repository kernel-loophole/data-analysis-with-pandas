import pandas as pd
import numpy as np
def data_frame():
    dict_data={'a':[1,2,3,4,5],'b':[6,7,8,9,10],'c':[11,12,13,14,15]}
    s=pd.DataFrame(dict_data)
    print(s)
    print(s.iloc[1])
    # print(s.iloc[1:3,2:4])
    print(s.iloc[[0,1],[0,2]])

    # print(s.iloc[1:3,2:4].values)
    # print(s.iloc[1:3,2:4].values.tolist())
    # print(s.iloc[1:3,2:4].values.tolist()[0][0])
    for i in s.iloc[1:3,2:4].values.tolist():
        print(i[0])
    
if __name__=="__main__":
    data_frame()