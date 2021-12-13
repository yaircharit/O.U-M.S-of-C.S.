from mnist import MNIST
from sklearn import datasets, svm

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sys import argv

# Load IRIS and MNIST datasets
mndata = MNIST("MNIST")
mnist = mndata.load_training()
iris = datasets.load_iris()

# MNIST data analysis is available through the command line, enter 'mnist' as a CMD parameter
# Default dataset is IRIS
if len(argv) < 2:
    print('Please enter <iris / mnist> to choose dataset (default = iris)')
    argv.append('iris')

save_dir = f'figures/{argv[1]}/{argv[0][:3]}' # Directory to save found data e.g. figures/iris/kNN/...

sample_size = 20000     # MNIST sample size

# Set data ready for work
if argv[1] == 'iris':
    X,Y = (iris.data,iris.target) 
    sample_size = len(X)
else:
    X,Y = mnist
    X,Y = X[:sample_size],Y[:sample_size]
    save_dir += f'/S={sample_size}'

train_test_data = train_test_split(X,Y,test_size=0.2,random_state=4)
