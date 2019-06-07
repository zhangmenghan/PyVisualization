import numpy as np
import matplotlib.pyplot as plt

#散点图
height = [161,170,182,175,173,165]
weight = [50,58,80,70,69,55]

plt.scatter(height,weight)
plt.show()

#不相关
N = 1000
x = np.random.randn(N)
y1 = np.random.randn(N)
plt.scatter(x,y1)
plt.show()

#正相关
N = 1000
x = np.random.randn(N)
y2 = x + np.random.randn(N) * 0.5
plt.scatter(x,y2)
plt.show()

#负相关
N = 1000
x = np.random.randn(N)
y2 = -x + np.random.randn(N) * 0.5
plt.scatter(x,y2)
plt.show()

#股票相关  开盘价和关盘价
open,close = np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(1,4),unpack=True)
change = close - open
yesterday = change[:-1]
today = change[1:]
# s 面积  c 颜色  marker 形状  alpha  透明度
plt.scatter(yesterday,today,s=10,c='r',marker='<',alpha=0.5)
plt.show()

#股票相关  开盘价和最高价
open,maxmize = np.loadtxt('000001.csv',delimiter=',',skiprows=1,usecols=(1,2),unpack=True)
change = maxmize - open
yesterday = change[:-1]
today = change[1:]
plt.scatter(yesterday,today,s=20,c='r',marker='^',alpha=0.5)
plt.show()