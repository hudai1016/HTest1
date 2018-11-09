import urllib.request
import sys
import matplotlib.pyplot as plt
import scipy.stats as stats
import pylab
target_url=("http://archive.ics.uci.edu/ml/machine-learning-"
            "databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data=urllib.request.urlopen(target_url)
xList=[]
labels=[]
for line in data:
    row=line.split(','.encode(encoding="utf-8"))
    xList.append(row)
nrow=len(xList)
ncol=len(xList[1])
type=[0]*3
colCounts=[]
col=3
colData=[]
for row in xList:
    colData.append(float(row[col]))

stats.probplot(colData,dist="norm",plot=pylab)
pylab.show()


