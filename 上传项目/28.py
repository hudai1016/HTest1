import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
import sklearn.datasets as datasets
from sklearn.metrics import r2_score
boston=datasets.load_boston()
data=boston.data
target=boston.target

x_train=data[:480]
y_train=target[:480]

x_test=data[480:]
y_true=target[480:]

line=LinearRegression()
lasso=Lasso()
ridge=Ridge()
tree=DecisionTreeRegressor()
svr=SVR()

line.fit(x_train,y_train)
lasso.fit(x_train,y_train)
ridge.fit(x_train,y_train)
tree.fit(x_train,y_train)
svr.fit(x_train,y_train)

line_y_pre=line.predict(x_test)
lasso_y_pre=lasso.predict(x_test)
ridge_y_pre=ridge.predict(x_test)
tree_y_pre=tree.predict(x_test)
svr_y_pre=svr.predict(x_test)

line.score=r2_score(y_true,line_y_pre)
lasso.score=r2_score(y_true,lasso_y_pre)
ridge.score=r2_score(y_true,ridge_y_pre)
tree.score=r2_score(y_true,tree_y_pre)
svr.score=r2_score(y_true,svr_y_pre)
print(line.score)
print(lasso.score)
print(ridge.score)
print(tree.score)
print(svr.score)


import matplotlib.pyplot as plt
plt.plot(y_true,label='True')
plt.plot(line_y_pre,label='Line')
plt.plot(lasso_y_pre,label='Lasso')
plt.plot(ridge_y_pre,label='Ridge')
plt.plot(tree_y_pre,label='DecisionTreeRegressor')
plt.plot(svr_y_pre,label='SVR')

plt.legend()
plt.show()
