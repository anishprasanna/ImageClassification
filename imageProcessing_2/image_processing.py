import glob
import random
import os

def main():
    #collect list of file paths from cats and dogs
    cat_photos = glob.glob('/Users/Carlos/Projects/Data_Mining/imageProcessing/photos/cats' + '/*.jpg')
    dog_photos = glob.glob('/Users/Carlos/Projects/Data_Mining/imageProcessing/photos/dogs' + '/*.jpg')
    
    #sort photos
    cat_photos.sort()
    dog_photos.sort()

    # one big list
    cats_and_dogs = cat_photos + dog_photos

    #created a dictionary with index as value
    indexed_cd = dict(zip(cats_and_dogs,range(len(cats_and_dogs))))

    #create a list of dictionary items
    cd_list = list(indexed_cd.items())
    
    randomizer(cd_list, len(indexed_cd))
    print(cd_list)




    
def randomizer(arr, n):                 #fisher yates algorithm
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return(arr)

if __name__ == '__main__':
    main()