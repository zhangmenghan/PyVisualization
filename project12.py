import matplotlib.pyplot as plt
import numpy as np

# 图例 plt方式
x=np.arange(1,11,1)
y=x*x

plt.plot(x,x*2,label='Normal')
plt.plot(x,x*3,label='Fast')
plt.plot(x,x*4,label='Faster')
# 参数 loc 位置（0：best  1：右上角 2：左上角 3：左下角 4：右下角） ncol 图例分为几列
plt.legend(loc=0,ncol=2)
# plt.legend(bbox_to_anchor=(0,1,1,0.1),loc=3,ncol=3,mode="expand")
plt.show()

# 图例 面向对象方式
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,y)

ax.legend(['ax legend'])

# line, =ax.plot(x,y,label='Inline label')

# line.set_label('label via method')
# ax.legend()

plt.show()