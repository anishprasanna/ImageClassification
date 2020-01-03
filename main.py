import random
from sklearn.naive_bayes import MultinomialNB
from feature_extraction import *
from knn import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm, metrics


def main():

    finaldf = createDF()
    finaldf = randomizer(finaldf, len(finaldf))

    #create a folder for every 20 images we have in the list.
    foldList = folding(finaldf, 5)
    cv_list = cross_validation(foldList)
    training = cv_list[0]
    test = cv_list[1]
    test = test[0]
    training = training[0]

    bestk  = findBestK(test, training)

    your_model = KNeighborsClassifier()
    trainingDataVals = training[['Corners','Keypoints','Edges']]
    trainingDataLabs = training[['Label']]
    testDataVals = test[['Corners','Keypoints','Edges']]
    testDataLabs = test[['Label']]

    trainingDataVals = trainingDataVals.reset_index()
    trainingDataLabs = trainingDataLabs.reset_index()
    testDataVals = testDataVals.reset_index()
    testDataLabs = testDataLabs.reset_index()

    trainingDataVals = trainingDataVals[['Corners', 'Keypoints', 'Edges']]
    trainingDataLabs = trainingDataLabs[['Label']]
    testDataVals = testDataVals[['Corners', 'Keypoints', 'Edges']]
    testDataLabs = testDataLabs[['Label']]


    start = time.time()
    knn = KNeighborsClassifier(n_neighbors = bestk, weights='distance')
    knn.fit(trainingDataVals, trainingDataLabs.values.ravel())

    # Returns a list of predicted classes - one prediction for every data point
    predictions2 = knn.predict(testDataVals)
    print('KNN scikit accuracy ' + str(metrics.accuracy_score(testDataLabs, predictions2)))
    end = time.time()
    print('KNN scikit time taken: ' + str(end - start))

    # Creates a svm Classifier
    start1 = time.time()
    clf = svm.SVC(kernel='linear')  # Linear Kernel

    # Trains the model using the training sets
    clf.fit(trainingDataVals, trainingDataLabs.values.ravel())

    # Predict the response for test dataset
    y_pred1 = clf.predict(testDataVals)
    print("Linear Kernel SVM Accuracy:", metrics.accuracy_score(testDataLabs, y_pred1))
    end1 = time.time()
    print('Linear Kernel SVM  time taken: ' + str(end1 - start1))
    start2 = time.time()
    NB = MultinomialNB()



    NB.fit(trainingDataVals, trainingDataLabs.values.ravel())

    # Returns a list of predicted classes - one prediction for every data point
    predictions1 = NB.predict(testDataVals)
    print("Naive Bayes Accuracy:", metrics.accuracy_score(testDataLabs, predictions1))
    end2 = time.time()
    print('Naive Bayes  time taken: ' + str(end2 - start2))

    # Plot showing accuracies for each K-Value
    bars = ('KNN', 'SVM','Naive Bayes')
    y_pos = np.arange(len(bars))
    # Create bars
    plt.bar(y_pos, [end-start,end1-start1,end2-start2])
    # Create names on the x-axis
    plt.xticks(y_pos, bars)
    # Add title and axis names
    plt.title('Time for each SciKit Classification Algorithm')
    plt.xlabel('Classification Algorithm')
    plt.ylabel('Time taken (s)')
    plt.savefig('Time_AlgAnalysis.png', bbox_inches='tight')
    plt.close()
    bars = ('KNN', 'SVM','Naive Bayes')
    y_pos = np.arange(len(bars))
    # Create bars
    plt.bar(y_pos, [metrics.accuracy_score(testDataLabs, predictions2),metrics.accuracy_score(testDataLabs, y_pred1),metrics.accuracy_score(testDataLabs, predictions1)])
    # Create names on the x-axis
    plt.xticks(y_pos, bars)
    # Add title and axis names
    plt.title('SciKit Classification Algorithm Accuracies')
    plt.xlabel('Classification Algorithm')
    plt.ylabel('Accuracy %')
    plt.savefig('AlgAccuracyComparison.png', bbox_inches='tight')
    plt.close()

#fisher yates algorithm
def randomizer(arr, n):
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        # arr.iloc[i], arr.iloc[j] = arr.iloc[j], arr.iloc[i]
        temp = arr.iloc[i].copy()
        arr.iloc[i] = arr.iloc[j]
        arr.iloc[j] = temp
    return arr

#make dataframe for folds
finaldf = createDF()
def folding(finaldf, num):
    length = len(finaldf.index)
    # print(length)
    foldlength = int(length / num)
    # print("Fold length", foldlength)
    foldList = []
    x = 0
    for i in range(0, num):
        fold = finaldf.iloc[x:(x + 20)]
        foldList.append(fold)
        x += foldlength
    return foldList

def cross_validation(foldList):
    training_list = []
    test_list = []
    finalTraining = []
    i = 0
    for fold in foldList:
        test_list.insert(i, foldList[i])
        j = 0
        for other in foldList:
            if not foldList[j].equals(foldList[i]):
                training_list.insert(i, foldList[j])
                if len(training_list) > 3:
                    temp = [training_list[0], training_list[1], training_list[2], training_list[3]]
                    temp = pd.concat(temp)
                    temp.reset_index()
                    finalTraining.insert(i, temp)
                    training_list = []
            j += 1
        i += 1
        return [finalTraining, test_list]

if __name__ == '__main__':
    main()
    