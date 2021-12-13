# Created by Yair Charit 207282955
from config import svm, ConfusionMatrixDisplay, accuracy_score, classification_report, train_test_split, plt
from config import train_test_data,sample_size, argv, save_dir
import os
import math
from matplotlib.pyplot import subplots


# Initialize
scores = dict()
X_train, X_test, y_train, expected = train_test_data
Cs = [0.0001, 0.001, 0.01, 0.1,0.5,1.0]
models_list = []
for c in Cs:
    # Create a list of all different classifiers
    models_list.append(
        [(svm.SVC(kernel="linear", C=c), 'SVC with Linear Kernal',c),
         (svm.LinearSVC(C=c, max_iter=10000), 'LinearSVC',c),
         (svm.SVC(kernel="rbf", gamma=0.7, C=c),"SVC with RBF kernel",c),
         (svm.SVC(kernel="poly", degree=3, gamma="auto", C=c),"SVC with Polynomial Kernel",c),
        ]
    )


for models in models_list:
    for clf, title,c in models:
        # Process all classifiers defined above
        print(f'------- {title} -------')
        clf.fit(X_train, y_train)
        predicted = clf.predict(X_test)
        if title not in scores:
            scores[title] = []
        # Save accuracy scores
        scores[title].append(accuracy_score(expected, predicted))
        # Print Classification Report
        print(f"Classification report for classifier {title}:\n{classification_report(expected, predicted)}\n")
        # Generate Confusion Matrix
        fig, ax = subplots(1,2,figsize=(10,4))
        fig.suptitle(f"{argv[1]} {title} C={c}")
        ConfusionMatrixDisplay.from_predictions(expected, predicted,ax=ax[0])
        ax[0].set_title("Confusion Matrix")
        ax[1].text(0,0,f"Classification report:\n{classification_report(expected, predicted, zero_division=1)}")
        ax[1].axis('off')
        # Save generated learned data into files
        if not os.path.isdir(f'{save_dir}/C={c}'):
            os.makedirs(f'{save_dir}/C={c}')
        plt.savefig(f'{save_dir}/C={c}/{title}.png')
        plt.close()

# Sum all different results and compare each classifier results' across predefined C values
fig, ax = plt.subplots(nrows=math.ceil(len(models)/2), ncols=2)
fig.suptitle(f'{argv[1]} SVM sample size {sample_size} summery')
plt.subplots_adjust(wspace=0.6, hspace=0.8)
for score,i in zip(scores, range(len(models))):
    ax.flat[i].plot(Cs, scores[score])
    ax.flat[i].set_xlabel('C')
    ax.flat[i].set_ylabel('Accuracy')
    ax.flat[i].set_title(f'{score}')

plt.savefig(f'{save_dir}/summery{len(models)}.png')
plt.close()