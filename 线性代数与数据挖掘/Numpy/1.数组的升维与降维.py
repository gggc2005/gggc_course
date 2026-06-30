import numpy as np

# 降维
a = np.array([[[1,2,3],[4,5,6]]])
print(a)
print("形状",a.shape)
print("-------------")
b = np.squeeze(a,axis=0)
print(b)
print("形状",b.shape)

print("--------------")
b = np.ones((1,1,2,3))
print(b)
print("形状",b.shape)
c = np.squeeze(b,axis=0)
print(c.shape)
print("+++++++++++++++++++")


# 升维
a = np.zeros((3,4))
print(a)
print("形状",a.shape)
b = np.expand_dims(a,axis=(0,2))
print(b,b.shape)


