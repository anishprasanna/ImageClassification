import glob
import random
import os
import shutil
from PIL import Image
import numpy as np

def main():
    #collect list of file paths from cats and dogs
    cat_photos = glob.glob('/Users/Carlos/Projects/Data_Mining/imageProcessing_2/photos/cats' + '/*.jpg')
    dog_photos = glob.glob('/Users/Carlos/Projects/Data_Mining/imageProcessing_2/photos/dogs' + '/*.jpg')
    
    #sort photos

    cat_photos.sort()
    dog_photos.sort()
    # print(cat_photos)

    # one big list
    cats_and_dogs = cat_photos + dog_photos

    #created a dictionary with index as value
    indexed_cd = dict(zip(cats_and_dogs,range(len(cats_and_dogs))))
    # print(indexed_cd)
    
    #create a list of dictionary items
    cd_list = list(indexed_cd.items())
    # print(cd_list)
    
    randomizer(cd_list, len(indexed_cd))
    # print(cd_list)

    #create a folder for every 20 images we have in the list.

    folding(cd_list, 5)

    im = Image.open('images/dot.jpg')
    iar = np.asarray(im)
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
    # print(num)
    
    # for i in range(1,num+1):
    #     os.mkdir('/Users/Carlos/Projects/Data_Mining/imageProcessing_2/fold_' + str(i) + '/')

    # i = 1
    while last < len(cd_list):
        twenty = cd_list[int(last):int(last + avg)]
        for i in twenty:
            shutil.move(i, '/Users/Carlos/Projects/Data_Mining/imageProcessing_2/fold_' + str(i) + '/')

        output.append(cd_list[int(last):int(last + avg)])
        # print(len(output))
        # dest = os.mkdir('/Users/Carlos/Projects/Data_Mining/imageProcessing_2/photos/fold_' + str(i) + '/')
        # for image in output:
        #     shutil.move(image, dest)
        last += avg
        # i += 1

    
    # for fold in output:
    #     print(fold)
        # fold_+i= list(fold_+str(i)).append

    # for image in output:
    #     shutil.move(image, dest)
    # return output

if __name__ == '__main__':
    main()