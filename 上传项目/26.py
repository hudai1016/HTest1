import urllib.request
import sys
import matplotlib.pyplot as plt
from sklearn import linear_model
fr=open('C:\\Users\\Asus\\Desktop\\1.txt','r')
data=fr.readlines()
datasets_X=[]
datasets_Y=[]
for line in data:
    row = line.strip().split(',')
    datasets_X.append(row[0])
    datasets_Y.append(row[1])

length=len(datasets_X)
datasets_X=np.array(datasets_X).reshape([length,1])
datasets_Y=np.array(datasets_Y)
minX=min(datasets_X)
maxX=max(datasets_X)
X=np.arange(minX,maxX).reshape([-1,1])
linear=linear_model.LinearRegression()
linear.fit(datasets_X,datasets_Y)
plt.scatter(datasets_X,datasets_Y,color='red')
plt.plot(X,linear.predict(X),color='blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()