import numpy as np
import matplotlib.pyplot as plt

# 调整坐标轴范围
x = np.arange(-10,11,1)

plt.plot(x,x*x)
# axis参数：x轴最小坐标，x轴最大坐标，y轴最小坐标，y轴最大坐标
# plt.axis([-5,5,20,60])
# xlim参数：x轴最小坐标，x轴最大坐标
plt.xlim([-5,5])
# plt.xlim(xmin = -5)
# plt.xlim(xmax = 5)
#plt.ylim([0,60])
plt.show()