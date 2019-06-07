import matplotlib.pyplot as plt

# 多图（同一时间生成多张图）
fig1=plt.figure()
ax1=fig1.add_subplot(111)
ax1.plot([1,2,3],[3,2,1])

fig2=plt.figure()
ax2=fig2.add_subplot(111)
ax2.plot([1,2,3],[1,2,3])

plt.show()

# 作业
fig1=plt.figure()
ax1=fig1.add_subplot(111)
ax1.plot([1,2,1],[3,2,1])

fig2=plt.figure()
ax2=fig2.add_subplot(111)
ax2.plot([1,2,3],[3,2,3])

plt.show()