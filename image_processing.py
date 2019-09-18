import glob
import random
import os
import shutil

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

    
def randomizer(arr, n):                 #fisher yates algorithm
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def folding(cd_list, num):
    avg = len(cd_list) / float(num)
    last = 0.0
    
    for i in range(1, num + 1):
        os.mkdir('/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_' + str(i) + '/')

    global output_1
    output_1 = []

    global output_2
    output_2 = []

    global fold_1
    fold_1 = []

    global fold_2
    fold_2 = []

    global fold_3
    fold_3 = []

    global fold_4
    fold_4 = []

    global fold_5
    fold_5 = []

    for photo in cd_list:
        output_1.append(photo[1])

    while last < len(output_1):
        output_2.append(output_1[int(last):int(last + avg)])
        last += avg

    i = 0
    for l1sts in output_2:
        for photo in l1sts:
            if i in range(0,20):
                fold_1.append(photo)             #I DON'T KNOW IF WE SHOULD DO THIS!!! Just add photo not index
                shutil.copy(photo, '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_1')
            
            if i in range(20,40):
                fold_2.append(photo)
                shutil.copy(photo, '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_2')

            if i in range(40, 60):
                fold_3.append(photo)
                shutil.copy(photo, '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_3')
            
            if i in range(60, 80):
                fold_4.append(photo)
                shutil.copy(photo, '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_4')
            
            if i in range(80, 100):
                fold_5.append(photo)
                shutil.copy(photo, '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_5')
            i += 1

    return output_2, fold_1, fold_2, fold_3, fold_4, fold_5

def x_validation(output_2, fold_1, fold_2, fold_3, fold_4, fold_5):
    # for fold in output_2:
    #     fold.sort()
    #     print(fold)

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

    print('validation set is:\n {0}'.format(validation_set_1))
    print('training set is:\n {0}'.format(training_set_1))

if __name__ == '__main__':
    main()