import matplotlib.pyplot as plt

# 饼状图
labels = 'A','B','C','D'
fracs = [15,30,45,10]
explode = [0,0,0.05,0]
plt.pie(x = fracs,labels = labels,autopct='%.0f%%',explode=explode,shadow=True)
plt.show()


#作业
labels = 'SH','BJ','SZ','GD'
fracs = [20,10,30,25]
explode = [0,0,0.05,0]
plt.pie(x = fracs,labels = labels,autopct='%.1f%%',explode=explode,shadow=True)
plt.show()