import numpy as np

a = np.array([[1, 2, 3, -7],[4, 9, 0, 5]])
print(a)
print(a.shape)

condition = a > 4
result = np.where(condition)
print(result)