# 实现K线图绘制
import matplotlib.pyplot as plt
import pandas as pd
from mpl_finance import candlestick_ochl

data = pd.read_hdf("./stock_plot/day_close.h5")[:100]
data1 = pd.read_hdf("./stock_plot/day_close.h5")[:100]
data2 = pd.read_hdf("./stock_plot/day_high.h5")[:100]
data3 = pd.read_hdf("./stock_plot/day_low.h5")[:100]

day = pd.concat([data["000001.SZ"], data1["000001.SZ"], data2["000001.SZ"], data3["000001.SZ"]], axis=1)

day.columns = ["open", "close", "high", "low"]
day = day.reset_index().values


# 画图
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(20, 8), dpi=80)

# 第一个参数axes
candlestick_ochl(axes, day, width=0.3, colorup="r", colordown="g")
plt.show()