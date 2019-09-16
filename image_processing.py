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
    # print(cat_photos)

    # one big list
    cats_and_dogs = cat_photos + dog_photos

    #created a dictionary with index as value
    indexed_cd = dict(zip(range(len(cats_and_dogs)), cats_and_dogs))
    # print(indexed_cd)
    
    #create a list of dictionary items
    cd_list = list(indexed_cd.items())
    # print(cd_list)
    
    randomizer(cd_list, len(indexed_cd))
    # print(cd_list)

    #create a folder for every 20 images we have in the list.

    folding(cd_list, 5)
    # list(im.getdata()) without numpy
    
def randomizer(arr, n):                 #fisher yates algorithm
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def folding(cd_list, num):
    avg = len(cd_list) / float(num)
    output = []
    last = 0.0
    
    while last < len(cd_list):
        output.append(cd_list[int(last):int(last + avg)])
        last += avg
    print(output)

if __name__ == '__main__':
    main()