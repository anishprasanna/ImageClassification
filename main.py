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
    
    randomizer(cd_list, len(indexed_cd))

    #create a folder for every 20 images we have in the list.
    folding(cd_list, 5)

    x_validation(output_2, fold_1, fold_2, fold_3, fold_4, fold_5)

<<<<<<< HEAD
#fisher yates algorithm
def randomizer(arr, n):
    for i in range(n-1, 0, -1):
=======
    
def randomizer(arr, n): 
                  #fisher yates algorithm
    for i in range(n-1, -1, -1):
>>>>>>> 1a39beaaa42e4d3d9813fdd80551fa92ea6ade0f
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
    count = 0
    #print everything out
    # for item in foldList:
    #     print(foldList[count])

def x_validation(output_2, fold_1, fold_2, fold_3, fold_4, fold_5):
    training_set_1 = []
    validation_set_1 = fold_1
    for fold in output_2:
        if fold != validation_set_1:
            training_set_1.append(fold)

    training_set_2 = []
    validation_set_2 = fold_2
    for fold in output_2:
        if fold != validation_set_2:
            training_set_2.append(fold)

    training_set_3 = []
    validation_set_3 = fold_3
    for fold in output_2:
        if fold != validation_set_3:
            training_set_3.append(fold)
    
    training_set_4 = []
    validation_set_4 = fold_4
    for fold in output_2:
        if fold != validation_set_4:
            training_set_4.append(fold)
    
    training_set_5 = []
    validation_set_5 = fold_5
    for fold in output_2:
        if fold != validation_set_5:
            training_set_5.append(fold)

    return training_set_1, training_set_2, training_set_3, training_set_4, training_set_5

if __name__ == '__main__':
    main()