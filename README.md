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
# Modin for parallel computing 
# Modin uses Ray or Dask to provide an effortless way to speed up your pandas notebooks, scripts, and libraries. Unlike other distributed DataFrame libraries, Modin provides seamless integration and compatibility with existing pandas code. Even using the DataFrame constructor is identical.
```python
import modin.pandas as pd
import numpy as np
data_frame=pd.read_csv("Airbnb_Open_Data.csv")
```
