import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpaches

# 形状

fig,ax = plt.subplots()

xy1 = np.array([0.2,0.2])  # 圆心
xy2 = np.array([0.1,0.4])  # 左下角点的位置
xy3 = np.array([0.5,0.2])  # 圆心
xy4 = np.array([0.5,0.45])  # 圆心

circle = mpaches.Circle(xy1,0.05)
rect = mpaches.Rectangle(xy2,0.2,0.1,color='r') # 长 宽
polygon = mpaches.RegularPolygon(xy3,5,0.1,color='g') # 边数 半径长度
eclipse = mpaches.Ellipse(xy4,0.2,0.1,color='y') #长直径 宽直径

ax.add_patch(circle)
ax.add_patch(rect)
ax.add_patch(polygon)
ax.add_patch(eclipse)

plt.axis('equal')
plt.grid()
plt.show()