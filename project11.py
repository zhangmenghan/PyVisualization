import numpy as np
import matplotlib.pyplot as plt

# 网格(作为背景）
y=np.arange(1,5)
plt.plot(y,y*2)
plt.grid(True)
plt.show()

# 交互中打开关闭网格
# plt.grid()
# color 颜色  linestyle 线型  linewidth 线宽
# plt.grid(True,color='g',linestyle='-',linewidth='2')

# 面向对象的方法绘制
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l1,l2=plt.plot(x,y),plt.plot(x,x*x)
ax.grid(color='g')

plt.show()

# 作业 plt方式
y=np.arange(1,5)
plt.plot(y,y*2)
plt.grid(True,color='r',linestyle='-.',linewidth='1')
plt.show()


# 作业 面向对象方式
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,y)
ax.grid(color='r',linestyle='-.',linewidth='1')

plt.show()