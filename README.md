# pandas
pandas
# Create DataFrame and series 

```python

import pandas as pd
data_frame=pd.DataFrame({
        "Name":["ali","zain","junaid"],
        "age":[20,15,15],
        "sex":["male","male","male"]
    })

```
# Load csv or Excel file
```python
def read_from_csv(filename):
    with open (filename) as f:
        dataset=pd.read_csv(f)
#     print(dataset.head(20))
#     print(dataset.dtypes)
    return dataset
dataset=read_from_csv("cities.csv")
dataset 
```
# Locks
```python
student_data.loc[student_data["First name"].str.len().idxmax(),"First name"]
```
