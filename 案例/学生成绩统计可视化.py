"""
使用Pandas读取准备好的学生成绩表，计算每个学生的最终成绩
最终成绩是平时成绩的百分之三十加上考试成绩的百分之七十
判断是否及格
并且最终成绩和及格率填到表格里，并保存
使用Matplotlib进行显示最终成绩和及格率
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 读取Excel文件
df = pd.read_excel("./source.xlsx")

# 将NaN值填入0
df = df.fillna(0)

# 计算总成绩
df['final_score'] = np.round(df['attendance'] * 0.3 + df['exam'] * 0.7)

# 统计及格
df['pass'] = df['final_score'].apply(lambda x:'yes' if x >= 60 else 'no')

# 保存到Excel文件中
# df.to_excel('./final_score_table.xlsx')

# 绘制直方图
# 设置直方图的区间边界从0到110，步长10
bins = np.arange(0,111,10)
print(bins)

#使用np.histogram函数计算每个区间的学生人数
hist, bin_edges = np.histogram(df['final_score'], bins=bins)
print(hist)
print(bin_edges)

# 创建一个图表实例
fig = plt.figure()

# 计算条形图的宽度
bar_width = bin_edges[1] - bin_edges[0]

# 绘制条形图，x轴是分数区间，y轴为学生人数
plt.bar(bin_edges[0:-1], hist, width=bar_width, align='edge')

# 在每个条形图上添加文本，显示该区间内的学生人数
for i in range(len(hist)):
    if hist[i]:
        plt.text(bin_edges[i] + bar_width / 2, hist[i] + 0.1, str(hist[i]), ha='center')

# 设置图表的标题和坐标轴标签
plt.title('finally')
plt.xlabel('score')
plt.ylabel("number")

# 设置x轴的刻度，显示分数区间的边界
plt.xticks(bin_edges[:-1])

# 输出直方图
plt.show()

# 绘制饼图
# 创建一个fig对象
fig = plt.figure()

# 使用value_counts方法统计通过和未通过的学生数量，返回一个Series数据
pass_data = df['pass'].value_counts()
# 绘制饼图
plt.pie(pass_data,labels=pass_data.index,autopct='%1.1f%%')
# 设置饼图的标题
plt.title('Distribution of Passing Status')
# 显示饼图
plt.show()