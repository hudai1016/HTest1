from sklearn import svm
from sklearn import datasets
import pickle
clf=svm.SVC()
iris=datasets.load_iris()
X,y=iris.data,iris.target
clf.fit(X,y)
with open('save/clf.pickle','wb') as f:
    pick.dump(clf,f)
