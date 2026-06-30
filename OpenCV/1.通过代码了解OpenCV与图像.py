
# 使用 numpy 来创建三维数组
import numpy as np

# 使用 OpenCV 库来进行查看图像及其他操作
import cv2

# 使用 Matplotlib 来同时展示多个图像
import matplotlib.pyplot as plt

# 创建一个700 * 700的三维数组（彩色图）
# 使用zeros创建一个数值全为0的数组，对应一张黑色图
# uint8 ：无符号整数0-255
image = np.zeros((700, 700, 3),dtype=np.uint8)

# 用来代表分割出来的矩形大小
block_size = 100

# 使用一个嵌套循环来对黑色图像进行分割
# i 代表行
for i in range(0, 700, block_size):
    # j 代表列
    for j in range(0 , 700, block_size):
        # i 的取值为 0 100 200 300 400 500 600
        # j 的取值为 0 100 200 300 400 500 600
        image[i, :, :] = (255, 255, 255)
        image[:, j, :] = (255, 255, 255)

        if i != 0 and j != 0 and i != 600 and j != 600 and (i == j or i + j == 600):
            image[i:i+block_size, j:j+block_size,:] = (0, 0, 255)

# matplotlib 的颜色顺序是RGB， 所以需要进行BGR到RGB的转换
# 在image_rgb 里面存放的事RGB顺序的图像
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# 获取原图中的三个通道
# 切片方法
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]

# 第二方法：cv2.split()函数去分割
# b, g, r = cv2.split(image)

# 创建新的图像，用来展示三通道图
blue_channel = np.zeros((700, 700, 3),dtype=np.uint8)
green_channel = np.zeros((700, 700, 3),dtype=np.uint8)
red_channel = np.zeros((700, 700, 3),dtype=np.uint8)

# 将获取到的原图像的三通道的像素值，覆盖到新创建的三个图像的对应的通道
blue_channel[:, :, 0] = b
green_channel[:, :, 1] = g
red_channel[:, :, 2] = r

# 将BGR转换为RGB
blue_channel_rgb = cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB)
green_channel_rgb = cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB)
red_channel_rgb = cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB)


plt.subplot(232)
plt.imshow(image_rgb)
plt.title("Original Image")
# 不显示坐标轴
plt.axis("off")

plt.subplot(234)
plt.imshow(blue_channel_rgb)
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(235)
plt.imshow(green_channel_rgb)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(236)
plt.imshow(red_channel_rgb)
plt.title("Red Channel")
plt.axis("off")

plt.tight_layout()

plt.show()



# # imshow 用来展示图像
# plt.imshow(image_rgb)
# plt.title("Original Image")
# # 不显示坐标轴
# plt.axis("off")
# # show函数用来显示图像
# plt.show()


# cv2.imshow('image', image)
# cv2.waitKey(3000)