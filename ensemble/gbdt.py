import sys
sys.path.append('.')
import numpy as np
from utils.dataLoader import loadIrisData
from sklearn.ensemble import GradientBoostingClassifier as gbc
from sklearn import metrics
from sklearn.model_selection import GridSearchCV


data=loadIrisData()

def split_data(data,test_size):
    c=len(data)
    if(c<=test_size):
        test_size=int(c/2)
    t=np.arange(c)
    np.random.shuffle(t)
    data_train=data[t[:c-test_size]]
    data_test=data[t[c-test_size:]]
    return data_train,data_test
data_train,data_test=split_data(data,50)

x_train=data_train[:,0:-1]
y_train=data_train[:,-1]

pgrid={'n_estimators':range(5,21,5)}
clf=GridSearchCV(estimator=gbc(n_estimators=100,verbose=1),param_grid=pgrid,cv=3)
clf.fit(x_train,y_train)
print(clf.best_estimator_)
y_pred=clf.predict(x_train)
y_proba=clf.predict_proba(x_train)
print('accuracy:{0}'.format(metrics.accuracy_score(y_train,y_pred)))
print('AUC:{0}'.format(metrics.roc_auc_score(y_train,y_proba,multi_class='ovr')))

# get the accuracy of the test data
x_test=data_test[:,0:-1]
y_test=data_test[:,-1]
yhat=clf.predict(x_test)
r=np.mean(y_test==yhat)
print(r)




