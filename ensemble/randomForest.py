import numpy as np
from sklearn.ensemble import RandomForestClassifier

X=np.array([
    [25,179,15,0],
    [33,190,19,0],
    [28,180,18,2],
    [25,178,18,2],
    [46,100,100,2],
    [40,170,170,1],
    [34,174,20,2],
    [36,181,55,1],
    [35,170,25,2],
    [30,180,35,1],
    [28,174,30,1],
    [29,176,36,1]
])
Y=np.array([0,1,1,1,0,0,1,0,1,1,0,1])

classifier=RandomForestClassifier(n_estimators=10).fit(X,Y)

test_labels=classifier.predict(X)
print(test_labels)
error_rate=np.sum(Y!=test_labels)/len(Y)
print("error_rate=",error_rate)