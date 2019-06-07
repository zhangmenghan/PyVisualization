import numpy as np
import matplotlib.pyplot as plt

# 注释
# x = np.arange(-10,11,1)
# y = x*x
# plt.plot(x,y)
# plt.annotate('This is the bottom',xy=(0,1),xytext=(0,20),
#              arrowprops=dict(facecolor='r',headlength=10,headwidth=20,width=10))
# plt.show()

# 文字
# x = np.arange(-10,11,1)
# y = x*x
# plt.plot(x,y)
# # family 字体  style=normal/italic斜体  weight 字体粗细
# plt.text(-2,40,'function:y=x*x',family='serif',size=20,color='r',
#          style='italic',weight='bold',bbox=dict(facecolor='r',alpha=0.2))
# plt.show()

# tex公式
fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_xlim([1, 7])
ax.set_ylim([1, 5])

# r代表不转译
ax.text(2, 4, r"$\alpha_i \beta_i \pi \lambda \omega$", size=20)
ax.text(4, 4, r"$\sin(0)=\cos(\frac{\pi}{2})$", size=20)
ax.text(2, 2, r"$\lim_{x \rightarrow y}\frac{1}{x^3}$", size=20)
ax.text(4, 2, r"$\sqrt[4]{x}=\sqrt{y}$", size=20)

plt.show()