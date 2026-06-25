import matplotlib.pyplot as plt


# plt.figure用来创建画板
plt.figure()
plt.subplot(2,2,1)
plt.plot([1,2],[2,3])
plt.subplot(2,2,4)
plt.plot([1,2],[3,2])
plt.figure(num=2)
plt.show()

# plt.subplots 用来创建画板和画布
fig, axe = plt.subplots(2,2)

print(fig)
print(axe)
axe[0,0].plot([1,2],[1,2])

plt.show()



# plt.subplots()
fig, axe = plt.subplots()
print(fig)
print(axe)
print(type(axe))