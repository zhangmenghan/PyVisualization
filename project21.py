import numpy as np
import matplotlib.pyplot as plt

# 极坐标
r=np.arange(1, 6, 1)
theta =[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]

ax=plt.subplot(111, projection ='polar')
ax.plot(theta, r, color ='r', linewidth=3)
ax.grid(True)
plt.show()


r=np.empty(5)
r.fill(5)
theta =[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]

ax=plt.subplot(111, projection ='polar')
ax.plot(theta, r, color ='r', linewidth=3)
ax.grid(True)

plt.show()


r=np.empty(7)
r.fill(7)
theta =[0, np.pi/3, 2*np.pi/3, np.pi, 4*np.pi/3, 5*np.pi/3, 2*np.pi]

ax=plt.subplot(111, projection ='polar')
ax.plot(theta, r, color ='r', linewidth=3)
ax.grid(True)

plt.show()


r=np.empty(9)
r.fill(9)
theta =[0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2,
        7*np.pi/4, 2*np.pi]

ax=plt.subplot(111, projection ='polar')
ax.plot(theta, r, color ='r', linewidth=3)
ax.grid(True)

plt.show()
