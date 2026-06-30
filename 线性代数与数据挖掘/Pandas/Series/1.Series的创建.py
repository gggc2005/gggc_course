import pandas as pd

"""
pd.Series(data,index,name,dtype)
    data -> 标量值、列表、元组、字典、一维Ndarray
    index -> 列表、元组
"""
data = {"a":1,"b":2,"c":"c"}
a = pd.Series(data,name="test")
print(a)



# 1d-Ndarray
import numpy as np
data = np.array([1,2,3])
b = pd.Series(data)
print(b)
