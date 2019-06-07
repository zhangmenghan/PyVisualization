import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib as mpl

# 调整坐标轴的刻度
x = np.arange(1, 11, 1)

plt.plot(x,x)
plt.locator_params('x', nbins=20)
# 获取当前图像的坐标轴  面向对象方法
# ax = plt.gca()
# ax.locator_params('x',nbins=20)
plt.show()

# 调整日期
fig = plt.figure()
start = datetime.datetime(2015, 1, 1)
stop = datetime.datetime(2016, 1, 1)
delta = datetime.timedelta(days=1)

dates = mpl.dates.drange(start,stop,delta)

y = np.random.rand(len(dates))
# date_format = mpl.dates.DateFormatter('%Y-%m-%d')
# ax = plt.gca()
# ax.xaxis.set_major_formatter(date_format)
# ax.plot_data(dates,y,linestyle='-',marker='')

plt.plot_date(dates,y,linestyle='-',marker='')
fig.autofmt_xdate()
plt.show()