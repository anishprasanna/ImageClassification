import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
import csv

#distance formula
def euclideanDistance(testAttribute1, testAttribute2, trainingAttribute1, trainingAttribute2, testAttribute3, trainingAttribute3):
   distance = pow((trainingAttribute1 - testAttribute1), 2) + pow((trainingAttribute2 - testAttribute2), 2) + pow((trainingAttribute3 - testAttribute3), 2)
   return math.sqrt(distance)

#accuracy formula
def getAccuracy(testSet, predictions):
   correct = 0
   for x in range(len(testSet)):
      if (testSet.loc[x, 'Class'].item() == predictions[x]):
         correct += 1
   return (correct / float(len(testSet))) * 100.0



def main():


    accurrayForEachK = np.empty(10, dtype=float)

    k = 1
    print("Finding best k-value from 1-10")
    while (k <= 10):
        value = 0
        #for each row in testData
        print("Making predictions for each element in testData (this may take a while)...")
        while (value < len(testData)):
            #empty array of distances of trainingData from instance in testData
            distances = np.empty(len(trainingData), dtype=float)
            testAttribute1 = testData.loc[value, 'Attribute1'].item()
            testAttribute2 = testData.loc[value, 'Attribute2'].item()
            testAttribute3 = testData.loc[value, 'Attribute3'].item()
            num = 0
            #for each row in trainingData
            for item in trainingData.iterrows():
                #calculate distances and store them in distances array
                trainingAttribute1 = trainingData.loc[num, 'Attribute1'].item()
                trainingAttribute2 = trainingData.loc[num, 'Attribute2'].item()
                trainingAttribute3 = trainingData.loc[num, 'Attribute3'].item()
                distances[num] = euclideanDistance(testAttribute1, testAttribute2, trainingAttribute1, trainingAttribute2, testAttribute3, trainingAttribute3)
                num += 1
            #getting indexes of the k closest neighbors and store in indexes array
            index = 0
            indexes = np.empty(k, dtype=int)
            while (index < k):
                smallest = distances.min()
                location = np.where(distances == smallest)

                testTuple = location[0]
                # if there is a tie
                if (len(location[i]) > 1):
                    testList = list(testTuple)
                    testList.pop(1)
                    testTuple = tuple(testList)
                indexes[index] = int(testTuple[0])
                index += 1
                distances = distances[distances != smallest]

            cat=0
            dog=0
            value1 = 0
            #seeing if the k closest neighbors are cats or dogs
            for element in indexes:
                if (trainingData.loc[indexes[value1], 'Class'].item() == 1.0):
                    cat += 1
                else:
                    dog += 1
                value1 += 1
            #print("Cat: ", cat)
            #print("Dog: ", dog)
            #using above results, predict the test instance to be a cat or dog
            if (cat > dog):
                predictions[value] = 1.0
            elif (cat < dog):
                predictions[value] = -1.0
            else:
                predictions[value] = trainingData.loc[indexes[0], 'Class'].item()
            #print(value)
            value += 1
            print(str(value) + " out of " + str(len(testData)) + " completed")

        #print('Predictions: ' + str(predictions))
        #displays accuracy of predictions made
        print('Prediction accuracy: ' + str(getAccuracy(testData, predictions)) + "%")
        accurrayForEachK[k - 1] = getAccuracy(testData, predictions)

        k += 1

    #returning the best k-value
    highestAccuracyPercentage = accurrayForEachK.max()
    bestK = (np.where(accurrayForEachK == highestAccuracyPercentage))
    print('Best k-value = ' , bestK[0][0] + 1)


main()