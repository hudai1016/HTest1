import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,11,1)
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(x,x*2,label='Normal')
ax1.plot(x,x*3,label='Fast')
ax1.plot(x,x*4,label='Faster')
ax1.legend()
plt.show()
