import numpy as np
import matplotlib.pyplot as plt

# 箱型图
np.random.seed(100)
data = np.random.normal(size=1000, loc=0.0, scale=1.0)

# sym 调整异常值的形状  whis 代表虚线长度，是一个比例值
plt.boxplot(data,sym='o',whis=1.5)
plt.show()

# 多个箱型图
data = np.random.normal(size=(100, 4), loc=0.0, scale=1.0)
labels = ['A','B','C','D']

plt.boxplot(data, labels=labels)
plt.show()

#作业
np.random.seed(100)
data = np.random.normal(size=(100, 5), loc=0.0, scale=1.0)
labels = ['A','B','C','D','E']

plt.boxplot(data, labels=labels,sym='o',whis=1.25)
plt.show()