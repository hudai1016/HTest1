import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
boston=datasets.load_boston()
data=pd.DataFrame(boston.data)
data.columns=boston.feature_names
data['PRICE']=boston.target
x=data.loc[:,'RM'].as_matrix(columns=None)
y=data.loc[:,'PRICE'].as_matrix(columns=None)

x=np.array([x]).T
y=np.array([y]).T
line=LinearRegression()
line.fit(x,y)
plt.scatter(x,y,s=10,alpha=0.5,color='blue')
plt.plot(x,line.predict(x),color='green',linewith='1')
plt.xlabel('RM')
plt.ylabel('Price')
plt.show()


