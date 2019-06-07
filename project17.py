import numpy as np
import matplotlib.pyplot as plt

# 工具栏使用
N=1000
x = np.random.randn(N)
y = np.random.randn(N)
colors = np.random.randn(N)
area = np.pi*(15*np.random.randn(N))**2  # 0 to 15 的点半径

plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.show()