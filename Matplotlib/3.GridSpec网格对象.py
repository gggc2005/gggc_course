from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,4))

# 创建网格对象
gs = GridSpec(3,3)
print(gs)

# 创建画布
ax1 = fig.add_subplot(gs[0:2,0])
ax2 = fig.add_subplot((gs[0:2,1:3]))
ax3 = fig.add_subplot(gs[2,0:2])
ax4 = fig.add_subplot(gs[2,2])

plt.show()