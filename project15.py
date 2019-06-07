import numpy as np
import matplotlib.pyplot as plt

# 添加一个坐标轴，形成双坐标轴
x = np.arange(2,20,1)

y1 = x*x
y2 = np.log(x)
plt.plot(x,y1)
plt.twinx()
plt.plot(x,y2,'r')
plt.show()

plt.plot(x,y1)
plt.twiny()
plt.plot(y2,x,'r')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x,y1)
ax1.set_ylabel('Y1')
ax2 = ax1.twinx()
ax2.plot(x,y2,'r')
ax2.set_ylabel('Y2')
ax1.set_xlabel('Compare Y1 and Y2')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x,y1)
ax1.set_xlabel('X1')
ax2 = ax1.twiny()
ax2.plot(y2,x,'r')
ax2.set_xlabel('X2')
ax1.set_ylabel('Compare X1 and X2')
plt.show()