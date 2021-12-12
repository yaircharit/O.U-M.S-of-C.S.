#   https://medium.com/@vibrant_linen_snake_505/knn-classification-using-python-scikit-learn-iris-dataset-725afed12633

#   https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
#   https://towardsdatascience.com/k-nn-on-iris-dataset-3b827f2591e

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# load IRIS dataset
iris = datasets.load_iris()
# Take the first two features.
X = iris.data[:, :2]
y = iris.target

scores = dict()
scores_list = []
X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=0.2,random_state=4)
max_k = 30
for k in range(1, max_k+1):
    print(f'--- k = {k} ---')
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(X_train,Y_train)
    y_pred = kNN.predict(X_test)
    scores[k] = accuracy_score(Y_test, y_pred)
    scores_list.append(scores[k])
    print("Accuracy: ", accuracy_score(Y_test, y_pred))
    
print(scores)
plt.plot(range(1, max_k+1), scores_list)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.show()