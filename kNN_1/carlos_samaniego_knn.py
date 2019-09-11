from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import glob
# Anish Prassanna - Manipulated data frames to calculate distances, and then sort them for k nearest neighbors
# I mainly did reading in files, cleaning them, and then reading them into respective dataframes
#  Esteban M. , Alex B. - worked together with me generally
# Worked on appendicitis folder

def main():
    path_to_keel_data = input("please input the path to the specific keel data. Ex. a path including banana-10-fold\n")
    k_value = input('please input K\n')
    k_value = int(k_value)

    training_set = glob.glob(path_to_keel_data + '/*tra.dat')
    test_set = glob.glob(path_to_keel_data + '/*tst.dat')

    training_set.sort()
    test_set.sort()

    cleaned_training_set = []
    cleaned_test_set = []

    for file in training_set:
        cleaned_training_set.append(clean(file))
    
    for file in test_set:
        cleaned_test_set.append(clean(file))
    
    cleaned_test_setsdfsandlabels = []
    cleaned_training_setsdfsandlabels =[]   
                                                                    #work from lines 10-55 was primarily done by Carlos, 
    for file in cleaned_training_set:                               #Anish Prassanna added more in lines 33-59
        cleaned_training_set_df = pd.read_csv(file, header=None)
        cleaned_test_set_df = pd.read_csv(file, header=None)
       
        df = cleaned_test_set_df.reset_index()
        df = df.drop('index', axis=1)
        labels = df[df.columns[len(df.columns) - 1]]
        df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)
        
        cleaned_training_setsdfsandlabels.append(df)
        cleaned_training_setsdfsandlabels.append(labels)


    for file in cleaned_test_set:
        cleaned_test_set_df = pd.read_csv(file, header=None)
        
        df = cleaned_test_set_df.reset_index()
        df = df.drop('index', axis=1)
        labels = df[df.columns[len(df.columns) - 1]]
        df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)

        cleaned_test_setsdfsandlabels.append(df)
        cleaned_test_setsdfsandlabels.append(labels)

    testandlabel = cleaned_test_setsdfsandlabels                    #lines 61-84 were mainly done by Anish Prasanna
    trainandlabel = cleaned_training_setsdfsandlabels
    
    classificationlabs = []

    j=0
    
    classlist = list()
    
    for i in range(0, 20, 2):
        classlist.append(classifytest(trainandlabel[i], trainandlabel[i+1], testandlabel[i], testandlabel[i+1], k_value))

    for i in range(1,20,2):
        testandlabel[i]=testandlabel[i].to_frame(name = 'label')

    for i in range(0,10,1):
        classlist[i]['label'] = classlist[i]['label'].apply(pd.to_numeric)

    accuracytotal = 0
    b = 0
    print("Accuracies below for each fold (10-9)")
    for i in range(1,20,2):
        print(accuracy(testandlabel[i],classlist[j]))
        accuracytotal = accuracytotal + accuracy(testandlabel[i],classlist[j])
        j = j + 1
    print("Avg overall accuracy")
    print(accuracytotal/10)


def clean(original_file):
    with open(original_file, "r") as f:
        lines = f.readlines()
    with open(original_file, "w") as f:
        for line in lines:
            if '@' not in line:
                f.write(line)
    return original_file

#finds dis between 2 points
def dis(obj1, obj2):                                             #Credit to Anish Prasanna
    squarediff = 0
    for i in range(len(obj1)):
        squarediff = (obj1[i] - obj2[i]) ** 2
    finaldis = squarediff ** .5
    return finaldis

 # finds k neighbors and returns prediction for one point
def classify(unknown, dataset, labels, k_value):                 #Credit to Anish Prasanna
    distances = pd.DataFrame(columns=('Dist', 'label'))
    # Looping through all points in the dataset
    for i in range(len(dataset)):
        distances.loc[i] = list([dis(dataset.iloc[i], unknown), labels[i]])

    distances = distances.sort_values('Dist')
    distances = distances.reset_index()

    kneighbors = distances[0:k_value]


    Op1 = 0
    Op2 = 0
    for i in range(len(kneighbors)):
        if kneighbors.at[i, 'label'] == 1:
            Op1 = Op1 + 1
        else:
            Op2 = Op2 + 1
    # if equal go with Op1
    if Op1 > Op2:
        return 1
    else:
        return 0

#compares label sets and finds decimal
def accuracy(testlabels,classifylabels):                #Credit to Anish Prasanna
    correct = 0

    for i in range(len(testlabels)):

        if (testlabels.loc[i,'label'].item() == classifylabels.loc[i,'label'].item()):
            correct = correct +1
    return (correct/len(testlabels))

def classifytest(train, trainlabels, test, testlabels, k):  # function by Anish Prassana
    predictions = pd.DataFrame(columns=(['label']))
    classifications = []
    for i in range(len(test)):
        predictions.loc[i] = list([classify(test.iloc[i], train, trainlabels, k)])
    return predictions


if __name__ == '__main__':
    main()