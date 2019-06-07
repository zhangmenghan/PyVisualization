import matplotlib.pyplot as plt
import numpy as np

# 子图
x=np.arange(1,100)

plt.subplot(221) #总行数，总列数，子图所在位置
plt.plot(x,x)

plt.subplot(222)
plt.plot(x,-x)

plt.subplot(223)
plt.plot(x,x*x)

plt.subplot(224)
plt.plot(x,np.log(x))

plt.show()

# 作业
x=np.arange(1,100)

plt.subplot(121) #总行数，总列数，子图所在位置
plt.plot(x,x)

plt.subplot(122)
plt.plot(x,-x)

plt.show()