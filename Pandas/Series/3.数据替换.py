import pandas as pd

# transform
a = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(a)

def square(x):
    return x ** 2

a.transform(square)