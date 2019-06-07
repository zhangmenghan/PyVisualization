import numpy as np
import matplotlib.pyplot as plt

# 区域填充
x = np.linspace(0,5*np.pi,1000)

y1 = np.sin(x)
y2 = np.sin(2*x)

# plt.plot(x,y1)
# plt.plot(x,y2)

plt.fill(x,y1,'b',alpha=0.3)
plt.fill(x,y2,'r',alpha=0.3)

fig = plt.figure()
ax = plt.gca()
ax.plot(x,y1,color='red')
ax.plot(x,y2,color='blue')
# 由于x的取值离散的，所以需要用到interpolate进行连续的填充
ax.fill_between(x,y1,y2,where=y1>y2,facecolors='yellow',interpolate=True)
ax.fill_between(x,y1,y2,where=y1<y2,facecolors='green',interpolate=True)
plt.show()