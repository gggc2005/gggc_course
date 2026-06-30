import numpy as np


a = np.zeros((2,2))
b = np.ones((2,3))

print(a)
print("a形状：",a.shape)
print("b形状：",b.shape)
print("______________")
c = np.concatenate((a,b),axis=1)
print(c)
print("水平方向，列关系连接：",c.shape)


d = np.concatenate((a,b.T),axis=0)
print(d)
print("垂直方向，行关系连接：",d.shape)

print("+++++++++++++++++++++++++++++++++++++++++++")

a1 = np.array([1,2,3])
b1 = np.array([4,5,6])
print(a1)
print(a1.shape)
print(b1)
print(b1.shape)
print("___________________")
x = np.stack((a1,b1),axis=0)
print(x)
print(x.shape)
print("____________________")
y = np.stack((a1,b1),axis=1)
print(y)
print(y.shape)