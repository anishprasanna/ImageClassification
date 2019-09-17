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

    
def randomizer(arr, n):                 #fisher yates algorithm
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def folding(cd_list, num):
    avg = len(cd_list) / float(num)
    output = []
    last = 0.0
    
    # for i in range(1, num + 1):
    #     os.mkdir('/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_' + str(i) + '/')

    while last < len(cd_list):
        output.append(cd_list[int(last):int(last + avg)])
        last += avg

    i = 0
    for l1sts in output:
        for photo in l1sts:
            if i in range(0,20):
                shutil.move(photo[1], '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_1')
            
            if i in range(20,40):
                shutil.move(photo[1], '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_2')

            if i in range(40, 60):
                shutil.move(photo[1], '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_3')
            
            if i in range(60, 80):
                shutil.move(photo[1], '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_4')
            
            if i in range(80, 100):
                shutil.move(photo[1], '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_5')
            i += 1

    return output
if __name__ == '__main__':
    main()