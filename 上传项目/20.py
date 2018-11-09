import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
target_url=("http://archive.ics.uci.edu/ml/machine-learning-""databases/undocumented/connectionist-bench/sonar/sonar.all-data")
abalone=pd.read_csv(target_url,header=None,prefix="V")
abalone.columns=['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']
corMat=DataFrame(abalone.iloc[:,1:9].corr())
print(corMat)
plt.pcolor(corMat)
plt.show()