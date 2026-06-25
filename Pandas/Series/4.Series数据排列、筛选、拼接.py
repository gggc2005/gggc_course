import numpy as np
import pandas as pd

# Series.sort_index()
index = [np.array(["qux","qux","foo","foo",
                   "baz","baz","bar","bar"]),
         np.array(["one","two","one","two",
                   "one","two","one","two"])]

a = pd.Series([1,2,3,4,5,6,7,8],index=index)

print(a)
print("+++++++++++")

b = a.sort_index(level=1,ascending=False,na_position="first",sort_remaining=True)
print(b)