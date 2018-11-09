import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
data = pd.read_excel('C:\\Users\\Asus\\Desktop\\traintest.xlsx')
data=data.dropna(how='any')
X=data[[""]]
km1=KMeans(n_clusters=3).fit(X)
km2=KMeans(n_clusters=2).fit(X)
km1.labels_
