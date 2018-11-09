import numpy as np
import matplotlib.pyplot as plt

labels='SH','BI','SZ','GD'
fracs=[20,35,30,15]
explode=[0.15,0.1,0,0]
plt.axes(aspect=1)
plt.pie(x=fracs,labels=labels,autopct='%.0f%%',explode=explode,shadow=True)
plt.show()
