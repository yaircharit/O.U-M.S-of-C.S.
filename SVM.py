from config import svm, ConfusionMatrixDisplay, accuracy_score, classification_report, train_test_split, plt
from config import X,Y, argv

Cs = [0.0001, 0.001, 0.01, 0.1,1.0]
models_list = []
for c in Cs:
    models_list.append(
        [(svm.SVC(kernel="linear", C=c), 'SVC with Linear Kernal'),
         (svm.LinearSVC(C=c, max_iter=10000), 'LinearSVC'),
         (svm.SVC(kernel="rbf", gamma=0.7, C=c),"SVC with RBF kernel"),
         (svm.SVC(kernel="poly", degree=3, gamma="auto", C=c),"SVC with Polynomial Kernel")],
    )

scores = dict()
for models in models_list:
    for clf, title in models:
        scores[title] = []
X_train, X_test, y_train, expected = train_test_split(X, Y, test_size=0.2, random_state=4)

for models in models_list:
    for clf, title in models:
        print(f'------- {title} -------')
        clf.fit(X_train, y_train)
        predicted = clf.predict(X_test)
        scores[title].append(accuracy_score(expected, predicted))
        print(f"Classification report for classifier {title}:\n{classification_report(expected, predicted)}\n")
        if argv[1] == 'mnist':
            disp = ConfusionMatrixDisplay.from_predictions(expected, predicted)
            disp.figure_.suptitle(f"{title} Confusion Matrix")
    if argv[1] == 'mnist':
        print('Close all figures for next C value')
        plt.show()
        
print(scores)
fig, ax = plt.subplots(nrows=2, ncols=2)
plt.subplots_adjust(wspace=0.6, hspace=0.8)
for score,i in zip(scores, range(4)):
    ax[i%2][i//2].plot(Cs, scores[score])
    ax[i%2][i//2].set_xlabel('C')
    ax[i%2][i//2].set_ylabel('Accuracy')
    ax[i%2][i//2].set_title(f'{score}')
plt.show()
