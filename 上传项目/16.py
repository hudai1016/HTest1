import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
target_url=("http://archive.ics.uci.edu/ml/machine-learning-""databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rocksVMines=pd.read_csv(target_url,header=None,prefix='V')
dataRow2=rocksVMines.iloc[0:208,1]
dataRow3=rocksVMines.iloc[0:208,2]
dataRow21=rocksVMines.iloc[20,0:60]
plt.scatter(dataRow2,dataRow3)
plt.xlabel("2nd Attribute")
plt.ylabel(("3rd Attribute"))
plt.show()
plt.scatter(dataRow2,dataRow21)
plt.xlabel("2nd Attribute")
plt.ylabel(("21st Attribute"))
plt.show()



