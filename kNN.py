from config import KNeighborsClassifier, accuracy_score,ConfusionMatrixDisplay, classification_report, train_test_split, plt
from config import X,Y, argv

max_k = 30

scores = dict()
scores_list = []
train_x, test_x, train_y, expected = train_test_split(X,Y,test_size=0.2,random_state=4)
for k in range(1, max_k+1):
    print(f'------- K = {k} -------')
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(train_x, train_y)
    predicted = kNN.predict(test_x)
    scores[k] = accuracy_score(expected, predicted)
    scores_list.append(scores[k])
    print(classification_report(expected, predicted))
    if argv[1] == 'mnist':
            disp = ConfusionMatrixDisplay.from_predictions(expected, predicted)
            disp.figure_.suptitle(f"k={k} Confusion Matrix")
if argv[1] == 'mnist':
    print('Close all figures for next C value')
    plt.show()

print(scores)
plt.plot(range(1, max_k+1), scores_list)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.show()
