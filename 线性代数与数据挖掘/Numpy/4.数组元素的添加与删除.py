import numpy as np

# append
a = np.array([1,2,3])
b = np.array([[4,5],[7,8]])
c = np.append(a,b)
print(c)

a = np.zeros((2,3))
b = np.ones((2,4))
c = np.append(a,b,axis=1)
print(c)
print(c.shape)
print("++++++++++++++++++++++++++++")

# insert
a = np.zeros((5,5))
b = np.insert(a,2,2,axis=0)
print(b)
print(b.shape)

# delete
c = np.delete(b,2,axis=1)
print(c)
print(c.shape)