import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from pylab import *
target_url=("http://archive.ics.uci.edu/ml/machine-"
            "learning-databases/glass/glass.data")
glass=pd.read_csv(target_url,header=None,prefix="V")
glass.columns=['Id','Ri','Na','Mg','Al','Si','K','Ca','Ba','Fe','Type']
print(glass.head())
summary=glass.describe()
print(summary)
ncol1=len(glass.columns)
glassNormalized=glass.iloc[:,1:ncol1]
ncol2=len(glassNormalized.columns)
summary2=glassNormalized.describe()

for i in range(ncol2):
    mean=summary2.iloc[1,i]
    sd=summary2.iloc[2,i]
    glassNormalized.iloc[:,i:(i+1)]=(glassNormalized.iloc[:,i:(i+1)]-mean)/sd

array=glassNormalized.values
boxplot(array)
plt.xlabel("Attribute Index")
plt.ylabel(("Quartile Ranges-Normalized"))
plt.show()
