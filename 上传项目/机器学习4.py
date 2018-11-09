import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
data=pd.read_excel('C:\\Users\\Asus\\Desktop\\featuredata.xls')
data1=data.iloc[:,:16]
target=data.iloc[:,16]
x=np.array(data1)
y=np.array(target)
train_data, test_data, train_label, test_label = train_test_split(x, y, random_state=1, test_size=0.3)

tree=DecisionTreeClassifier()

tree.fit(train_data,train_label)
      # 利用训练数据训练模型
      # 对x_test数据进行预测
hat_test_label=tree.predict(test_data)
    # precision:精准率，recall：召回率

print(classification_report(test_label,hat_test_label))









