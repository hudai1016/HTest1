import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
target_url=("http://archive.ics.uci.edu/ml/machine-learning-""databases/undocumented/connectionist-bench/sonar/sonar.all-data")
rocksVMines=pd.read_csv(target_url,header=None,prefix='V')
corMat=DataFrame(rocksVMines.corr())
plt.pcolor(corMat)
plt.show()