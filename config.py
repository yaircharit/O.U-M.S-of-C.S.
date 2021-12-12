from mnist import MNIST
from sklearn import datasets, svm

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sys import argv

sample_size = 10000
mndata = MNIST("MNIST")
mnist = mndata.load_training()
iris = datasets.load_iris()

if len(argv) < 2:
    print('Please enter <iris / mnist> to choose dataset (default = iris)')
    argv.append('iris')
if argv[1] == 'iris':
    X,Y = (iris.data[:,:2],iris.target) 
else:
    X,Y = mnist
    X,Y = X[:sample_size],Y[:sample_size]
