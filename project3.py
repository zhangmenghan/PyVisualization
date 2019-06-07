import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 折线图
x = np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)
plt.show()


# 股票时间序列(开盘，闭盘）
date,open,close=np.loadtxt('000001.csv',delimiter=',',converters={0:mdates.bytespdate2num('%m/%d/%Y')},
                           skiprows=1,usecols=(0,1,4),unpack=True)

plt.plot_date(date,open,linestyle = '--', color='green',marker = '<')
plt.plot_date(date,close,linestyle = '-', color='red',marker = 'o')
plt.show()


# 正弦图像
plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
S = np.sin(X)

plt.plot(X, S, color="red", linewidth=2.5, linestyle="-",  label="sine",
         zorder=-2)

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, +1],
           [r'$-1$', r'$+1$'])

plt.legend(loc='upper left', frameon=False)

t = 2*np.pi/3

plt.plot([t,t],[0,np.sin(t)],
         color ='red',  linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)),  xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

plt.show()


# Open,High,Low,Close
date,open,high,low,close=np.loadtxt('000001.csv',delimiter=',',converters={0:mdates.bytespdate2num('%m/%d/%Y')},
                           skiprows=1,usecols=(0,1,2,3,4),unpack=True)

plt.plot_date(date,open,linestyle = '--', color='yellow',marker = '<')
plt.plot_date(date,high,linestyle = '-.', color='red',marker = '^')
plt.plot_date(date,low,linestyle = ':', color='green',marker = '2')
plt.plot_date(date,close,linestyle = '-', color='blue',marker = 'o')
plt.show()