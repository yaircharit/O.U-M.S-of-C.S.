# Created by Yair Charit 207282955
from matplotlib.pyplot import subplots
from config import KNeighborsClassifier, accuracy_score,ConfusionMatrixDisplay, classification_report, train_test_split, plt
from config import train_test_data,sample_size, argv, save_dir
import os

# Initialize
max_k = 50
# save_dir += f'/max_k={max_k}'
scores_list = []
train_x, test_x, train_y, expected = train_test_data

for k in range(1, max_k+1):
    # Process kNN data for each k up to max_k
    print(f'------- K = {k} -------')
    kNN = KNeighborsClassifier(n_neighbors=k)
    kNN.fit(train_x, train_y)
    predicted = kNN.predict(test_x)
    # Save accuracy scores
    scores_list.append(accuracy_score(expected, predicted))
    # Print Classification Report
    print(f"Classification report for {argv[1]} K={k}:\n{classification_report(expected, predicted)}\n")
    # Generate Confusion Matrix
    # plt.figure(figsize=(3,1))
    fig, ax = subplots(1,2,figsize=(10,4))
    fig.suptitle(f"{argv[1]} {k}NN")
    ConfusionMatrixDisplay.from_predictions(expected, predicted,ax=ax[0])
    ax[0].set_title("Confusion Matrix")
    ax[1].set_title("Classification Report")
    ax[1].text(0,0,f"{classification_report(expected, predicted, zero_division=1)}")
    ax[1].axis('off')
    # Save generated learned data into files
    if not os.path.isdir(f'{save_dir}'):
        os.makedirs(f'{save_dir}')
    
    plt.savefig(f'{save_dir}/K={k}.png')
    plt.close()

# Observe accuracies compared to each k tested.
plt.figure().suptitle(f'{argv[1]} kNN {max_k} summery')
plt.plot(range(1, max_k+1), scores_list)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.savefig(f'{save_dir}/summery{max_k}.png')
plt.close()
