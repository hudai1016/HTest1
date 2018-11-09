import urllib.request
import numpy
import random
from sklearn import datasets,linear_model
from sklearn.metrics import roc_curve,auc
import pylab as p

def confusionMatrix(predicted,actual,threshold):
    if len(predicted)!=len(actual):
        return -1
    tp=0.0
    fp=0.0
    tn=0.0
    fn=0.0

    for i in range(len(actual)):
        if actual[i]>0.5:
            if predicted[i]>threshold:
                tp+=1.0
            else:
                fn+=1.0
        else:
            if predicted[i]<threshold:
                tn+=1.0
            else:
                fp+=1.0
    rtn=[tp,fn,fp,tn]
    return rtn

target_url=("http://archive.ics.uci.edu/ml/machine-learning-"
            "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data=urllib.request.urlopen(target_url)
xList=[]
labels=[]
for line in data:
    row = line.split(','.encode(encoding="utf-8"))
    if(row[-1]=='M'):
        labels.append(1.0)
    else:
        labels.append(0.0)

    row.pop()
    floatRow=[float(num) for num in row]
    xList.append(floatRow)

indices=range(len(xList))
xListTest=[xList[i] for i in indices if i%3==0]
xListTrain=[xList[i] for i in indices if i%3 !=0]
labelsTest=[labels[i] for i in indices if i%3==0]
labelsTrain=[labels[i] for i in indices if i%3!=0]

xTrain=numpy.array(xListTrain);
yTrain=numpy.array(labelsTrain)
xTest=numpy.array(xListTest)
yTest=numpy.array(labelsTest)
print("Shape of xTrain array",xTrain.shape)
print("Shape of yTrain array",yTrain.shape)
print("Shape of xTest array",xTest.shape)
print("Shape of yTest array",yTest.shape)

rocksVMinesModel=linear_model.LinearRegression()
rocksVMinesModel.fit(xTrain,yTrain)

trainingPredictions=rocksVMinesModel.predict(xTrain)
print("Some values predicted by model",trainingPredictions[0:5],trainingPredictions[-6:-11])

