import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import datasets
load_data=datasets.load_boston()
data_x=load_data.data
data_y=load_data.target
print(data_x[:1])
model=LinearRegression()
model.fit(data_x,data_y)
print(model.coef_)
print(model.intercept_)
temp_x=data_x[:50]
plt.scatter(temp_x[:,:1],model.predict(temp_x),color='r',label='prediction')
plt.scatter(temp_x[:,:1],data_y[:50],color='b',label='origial_data')
print(model.score(data_x,data_y))
plt.show()








