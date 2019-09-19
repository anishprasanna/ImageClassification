import glob
import random
import os
import shutil
from feature_extraction import *


global output_1, output_2, fold_1, fold_2, fold_3, fold_4, fold_5
output_1 = []
output_2 = []
fold_1 = []
fold_2 = []
fold_3 = []
fold_4 = []
fold_5 = []


def main():
    #collect list of file paths from cats and dogs
    cat_photos = glob.glob('/Users/Carlos/Projects/Dogs_vs_Cats/photos/cats' + '/*.jpg')
    dog_photos = glob.glob('/Users/Carlos/Projects/Dogs_vs_Cats/photos/dogs' + '/*.jpg')
    
    #sort photos
    cat_photos.sort()
    dog_photos.sort()

    # one big list
    cats_and_dogs = cat_photos + dog_photos

    #created a dictionary with index as value
    indexed_cd = dict(zip(range(len(cats_and_dogs)), cats_and_dogs))
    
    #create a list of dictionary items
    cd_list = list(indexed_cd.items())

    finaldf = createDF()
    finaldf = randomizer(finaldf, len(finaldf))

    #create a folder for every 20 images we have in the list.
    foldList = folding(finaldf, 5)
    cross_validation(foldList)
    #x_validation(output_2, fold_1, fold_2, fold_3, fold_4, fold_5)

#fisher yates algorithm
def randomizer(arr, n):
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        # arr.iloc[i], arr.iloc[j] = arr.iloc[j], arr.iloc[i]
        temp = arr.iloc[i].copy()
        arr.iloc[i] = arr.iloc[j]
        arr.iloc[j] = temp
    return arr

#make dataframe for folding algo 
finaldf = createDF()
def folding(finaldf, num):
    length = len(finaldf.index)
    print(length)
    foldlength = int(length / num)
    print("Fold length", foldlength)
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
        #test_list[i] = foldList[i]
        test_list.insert(i, foldList[i])
        j = 0
        for other in foldList:
            if not foldList[j].equals(foldList[i]):
                training_list.insert(i, foldList[j])
                if len(training_list) > 3:
                    temp = [training_list[0], training_list[1], training_list[2], training_list[3]]
                    temp = pd.concat(temp)
                    finalTraining.insert(i, temp)
                    training_list = []
            j += 1
        i += 1
    print("training list" , finalTraining)
    return finalTraining, test_list

if __name__ == '__main__':
    main()