#   https://dmkothari.github.io/Machine-Learning-Projects/SVM_with_MNIST.html

from mnist import MNIST
from sklearn.svm import SVC, LinearSVC
from sklearn.metrics import accuracy_score

print("Loading dataset...")
mndata = MNIST("MNIST")
images, labels = mndata.load_training()

clf = LinearSVC(C=0.0100)
training_count = 50000
# Train on the first 10000 images:
train_x = images[:training_count]
train_y = labels[:training_count]

print("Train model")
clf.fit(train_x, train_y)

# Test on the next 100 images:
test_x = images[training_count:]
expected = labels[training_count:].tolist()

print("Compute predictions")
predicted = clf.predict(test_x)
# print(expected, predicted)
print("Accuracy: ", accuracy_score(expected, predicted))

