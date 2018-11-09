import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from pylab import *
target_url=("http://archive.ics.uci.edu/ml/machine-"
            "learning-databases/abalone/abalone.data")
abalone=pd.read_csv(target_url,header=None,prefix="V")
abalone.columns=['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']
print(abalone.head())
print(abalone.tail())
summary=abalone.describe()
print(summary)
array=abalone.iloc[:,1:9].values
boxplot(array)
plt.xlabel("Attribute Index")
plt.ylabel(("Quartile Ranges"))
plt.show()
array2=abalone.iloc[:,1:8].values
boxplot(array2)
plt.xlabel("Attribute Index")
plt.ylabel(("Quartile Ranges"))
plt.show()


abaloneNormalized=abalone.iloc[:,1:9]
for i in range(8):
    mean=summary.iloc[1,i]
    sd=summary.iloc[2,i]
    abaloneNormalized.iloc[:,i:(i+1)]=(abaloneNormalized.iloc[:,i:(i+1)]-mean)/sd

array3=abaloneNormalized.values
boxplot(array3)
plt.xlabel("Attribute Index")
plt.ylabel(("Quartile Ranges-Normalized"))
plt.show()