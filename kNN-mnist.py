#   https://www.codingame.com/playgrounds/37409/handwritten-digit-recognition-using-scikit-learn

#  ROC:  https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html

from mnist import MNIST
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

print("Loading dataset...")
mndata = MNIST("MNIST")
images, labels = mndata.load_training()

scores = dict()
scores_list = []

max_k = 10
training_precent = 0.9
training_count = round(len(labels)*training_precent)
# Train on the first 10000 images:
train_x = images[:training_count]
train_y = labels[:training_count]
# Test on the next 100 images:
test_x = images[training_count:]
expected = labels[training_count:].tolist()
for k in range(1, max_k+1):
    print(f'--- k = {k} ---')
    kNN = KNeighborsClassifier(n_neighbors=k)

    print("Train model")
    kNN.fit(train_x, train_y)

    print("Compute predictions")
    predicted = kNN.predict(test_x)
    scores[k] = accuracy_score(expected, predicted)
    scores_list.append(scores[k])
    # print(expected, predicted)
    print("Accuracy: ", accuracy_score(expected, predicted))

print(scores)
plt.plot(range(1, max_k+1), scores_list)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.show()
