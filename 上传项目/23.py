import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from pylab import *
target_url=("http://archive.ics.uci.edu/ml/machine-"
            "learning-databases/glass/glass.data")
glass=pd.read_csv(target_url,header=None,prefix="V")
glass.columns=['Id','Ri','Na','Mg','Al','Si','K','Ca','Ba','Fe','Type']
glassNormalized=glass
ncols=len(glassNormalized.columns)
nrows=len(glassNormalized.index)
summary=glassNormalized.describe()
nDataCol=ncols-1
for i in range(ncols-1):
    mean=summary.iloc[1,i]
    sd=summary.iloc[2,i]
glassNormalized.iloc[:,i:(i+1)]=(glassNormalized.iloc[:,i:(i+1)]-mean)/sd
for i in range(nrows):
    dataRow=glassNormalized.iloc[i,1:nDataCol]
    labelColor=glassNormalized.iloc[i,nDataCol]/7.0
    dataRow.plot(color=plt.cm.RdYlBu(labelColor),alpha=0.5)

plt.xlabel("Attribute Index")
plt.ylabel(("Attritube values"))
plt.show()
