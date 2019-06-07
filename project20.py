import numpy as np
import matplotlib.pyplot as plt

# 形状美化
fig, axes = plt.subplots(ncols=2, nrows=2)

ax1, ax2, ax3, ax4 = axes.ravel()

x = np.random.normal(size=100)
y = np.random.normal(size=100)

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
ncolors = len(colors)

ax1.plot(x,y,'o')

x=np.arange(0,10)
y=np.arange(0,10)

shift = np.linspace(0,10,ncolors)

for s in shift:
    ax2.plot(x,y+s,"-")

x=np.arange(5)

y1,y2,y3=np.random.randint(1,25,size =(3,5))

width =0.25

ax3.bar(x,y1,width)
ax3.bar(x+width,y2,width,color=colors[1])
ax3.bar(x+width*2,y3,width,color=colors[2])

i=0
for i in range(0,ncolors):
    xy=np.random.normal(size=2)
    ax4.add_patch(plt.Circle(xy,radius =0.3,color= colors[i]))
    ax4.axis('equal')


plt.style.use('fivethirtyeight')

plt.show()
