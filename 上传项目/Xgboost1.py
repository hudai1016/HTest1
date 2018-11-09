import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from xgboost import XGBClassifier
data=pd.read_excel('C:\\Users\\Asus\\Desktop\\featuredata.xls')
data1=data.iloc[:,:16]
target=data.iloc[:,16]
x=np.array(data1)
y=np.array(target)
train_data, test_data, train_label, test_label = train_test_split(x, y, random_state=1, test_size=0.3)
xgb=XGBClassifier()
eval_set=[(test_data,test_label)]
xgb.fit(train_data,train_label,early_stopping_rounds=10,eval_metric="logloss",eval_set=eval_set,verbose=True)
hat_test_label=xgb.predict(test_data)
print(classification_report(test_label,hat_test_label))
