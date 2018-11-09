from sklearn.learning_curve import learning_curve
from sklearn.datasets import load_iris
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

iris=load_iris()
X=iris.data
y=iris.target
train_sizes,train_loss,test_loss=learning_curve(SVC(gamma=0.001),X,y,cv=5,scoring='mean_squared_error')
train_loss_mean=-np.mean(train_loss,axis=1)
test_loss_mean=-np.mean(test_loss,axis=1)
plt.plot(train_loss_mean,'o-',color='r',label="Training")
plt.plot(test_loss_mean,'o-',color='g',label="Cross-validation")
plt.xlabel("Training examples")
plt.ylabel("Loss")
plt.legend(loc="best")
plt.show()
