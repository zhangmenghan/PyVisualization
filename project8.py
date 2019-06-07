#pyplot
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
plt.plot(x,y)
plt.title('pyplot')
plt.show()


#pylab
from pylab import *
x=arange(0,10,1)
y=randn(len(x))
plot(x,y)
title('random numbers')
show()


#Object Oriented
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,1)
y=np.random.randn(len(x))
fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,y)
t=ax.set_title('object oriented')
plt.show()
