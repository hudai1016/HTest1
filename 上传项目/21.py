import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from pylab import *
target_url=("http://archive.ics.uci.edu/ml/machine-learning-""databases/wine-quality/winequality-red.csv")
wine=pd.read_csv(target_url,header=0,sep=";")
print(wine.head())
summary=wine.describe()
print(summary)
wineNormalized=wine
ncols=len(wineNormalized.columns)
for i in range(ncols):
    mean=summary.iloc[1,i]
    sd=summary.iloc[2,i]
    wineNormalized.iloc[:,i:(i+1)]=(wineNormalized.iloc[:,i:(i+1)]-mean)/sd

array=wineNormalized.values
boxplot(array)
plt.xlabel("Attribute Index")
plt.ylabel(("Quartile Ranges-Normalized"))
plt.show()
