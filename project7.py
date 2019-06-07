import numpy as np
import matplotlib.pyplot as plt

#默认情况
y=np.arange(1,5)
plt.plot(y)
plt.show()

'''
#调整颜色
y=np.arange(1,5)
plt.plot(y,'y');
plt.plot(y+1,color=(0.1,0.2,0.3));
plt.plot(y+2,'#FF00FF');
plt.plot(y+3,color='0.5')

plt.show()
'''

'''
#线型

y=np.arange(1,5)
plt.plot(y,'--');
plt.plot(y+1,'-.');
plt.plot(y+2,':');

plt.show()

'''
#点形状

'''
y=np.arange(1,5)
plt.plot(y,'o');
plt.plot(y+1,'D');
plt.plot(y+2,'^');
plt.plot(y+3,'s');
plt.plot(y+4,'p');
plt.plot(y+5,'x');

plt.show()
'''

y=np.arange(1,5)
plt.plot(y,'cx--');
plt.plot(y+1,'kp:');
plt.plot(y+2,'mo-.');

plt.show()

# 作业
y=np.arange(1,5)
plt.plot(y,'cx--');
plt.plot(y+1,'kp:');
plt.plot(y+2,'mo-.');

plt.show()