import numpy as np
import matplotlib.pyplot as plt

# 直方图
N=5
y=[20,10,30,25,15]
index = np.arange(N)
# bottom 指的是最底层坐标
p1 = plt.bar(x=index, height=y,width=0.5,bottom=100,color='red')
plt.show()
p2 = plt.bar(x=0, bottom=index, width=y,height=0.5,orientation='horizontal')
plt.show()


# 双直方图
index= np.arange(4)

sales_BJ = [52,55,63,53]
sales_SH = [44,66,55,41]

bar_width = 0.3

plt.bar(index,sales_BJ,bar_width,color = 'b')
plt.bar(index + bar_width,sales_SH,bar_width,color = 'r')
plt.show()


# 层叠图
index= np.arange(4)

sales_BJ = [52,55,63,53]
sales_SH = [44,66,55,41]

bar_width = 0.3

plt.bar(index,sales_BJ,bar_width,color = 'b')
plt.bar(index,sales_SH,bar_width,color = 'r',bottom = sales_BJ)
plt.show()


# 水平双直方图
index= np.arange(4)

sales_BJ = [52,55,63,53]
sales_SH = [44,66,55,41]

bar_width = 0.3

plt.bar(x=0,bottom=index,width=sales_BJ,height=bar_width,color = 'b',orientation='horizontal')
plt.bar(x=0,bottom=index+bar_width,width=sales_SH,height=bar_width,color = 'r',orientation='horizontal')
plt.show()


# 水平层叠图
index= np.arange(4)

sales_BJ = [52,55,63,53]
sales_SH = [44,66,55,41]

bar_width = 0.3

plt.bar(x=0,bottom=index,width=sales_BJ,height=bar_width,color = 'b',orientation='horizontal')
plt.bar(x=sales_BJ,bottom=index,width=sales_SH,height=bar_width,color = 'r',orientation='horizontal')
plt.show()

