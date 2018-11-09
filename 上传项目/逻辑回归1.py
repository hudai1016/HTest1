from numpy import *  # 常用包
import xlrd  # 读excel使用的包
from sklearn.model_selection import train_test_split  # 将数据分开
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


def split_feature(row):
    app = []  # 定义列表
    for i in range(16):
        app = app + [row[i]]
    return app

def loadDataSet(path, training_sample, colnameindex=0, by_name=u'sheet1'):
    dataMat = []  # 定义数据列表
    labelMat = []  # 定义标签列表
    filename = path + training_sample  # 形成特征数据的完整路径
    data = open_excel(filename)  # 打开文件获取数据
    table = data.sheet_by_name(by_name)  # 获得数据表
    nrows = table.nrows  # 得到表数据总行数
    for rownum in range(1, nrows):  # 也就是从Excel第二行开始，第一行表头不算
        row = table.row_values(rownum)  # 取一行数据
        if row:
            app = split_feature(row)  # 将特征值转化为列表
            dataMat.append(app)
            labelMat.append(float(row[16]))  # 获取类别标签
    return dataMat, labelMat
def main():
    """
    主函数
    :return: null
    """
    path = "C:\\Users\\Asus\\Desktop\\"
    training_sample = 'featuredata.xls'

def sigmoid(x):
    return 1.0/(1+exp(-x))

#最简单直接的梯度上升法
def gradAscent(dataMatIn,classLabels):
    dataMatrix=mat(dataMatIn);labelList=mat(classLabels).transpose()
    m,n=shape(dataMatIn)
    weights=ones([n,1])
    alpha=0.001
    maxCycle=500
    error=mat([m,1])
    for i in range(maxCycle):
        h=sigmoid(dataMatrix*weights)#h:[m,n]*[n,1]=[m,1]
        #print type(h),h[0,0],labelList[0,0]
        error= labelList-h#labelList:[m,1]
        weights=weights+alpha*dataMatrix.transpose()*error
    print(type(weights))
    return weights
def stocGradAscent(dataMatIn,classLabels):
    m,n=shape(dataMatIn)
    weights=ones(n)
    alpha=0.001
    for j in range(200):#多次重复迭代过程
        for i in range(m):
            h=sigmoid(sum(dataMatIn[i]*weights))
            error=classLabels[i]-h
            weights=weights+alpha*error*array(dataMatIn[i])
    return weights

def stocGradAscent1(dataMatIn,classLabels,numIter=150):
    dataMat=dataMatIn
    m,n= shape(dataMat)
    weights=ones(n)
    for i in range(numIter):
        dataInx=range(m)
        for j in range(m):
            alpha=4/(i+j+1.0)+0.01
            randInx=int(random.uniform(0,len(dataInx)))#注意理解这句中的dataInx
            h=sigmoid(sum(dataMat[randInx]*weights))
            error=classLabels[randInx]-h
            weights=weights+alpha*error*array(dataMat[randInx])
            del(dataInx[randInx])
    return weights

def plotBestFit(weights):
    dataMat,labelMat=loadDataSet()
    dataArr=array(dataMat)
    n=shape(dataArr)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        if int(labelMat[i])==1:
            xcord1.append(dataArr[i,1]);ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]);ycord2.append(dataArr[i,2])

    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x=arange(-4.0,4.0,0.1)
    y=(-1*float(weights[0])-float(weights[1])*x)/float(weights[2])
    ax.plot(x,y)
    plt.xlabel('x1');plt.ylabel('x2')
    plt.legend()
    plt.show()