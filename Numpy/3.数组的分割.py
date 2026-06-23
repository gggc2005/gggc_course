import numpy as np

arr = np.zeros((6,6))
print(arr)
print("shape:",arr.shape)

print("------------------------")
x = np.split(arr,3)
print(x)


print("------------------------")
y = np.split(arr,3,axis=1)
print(y)
