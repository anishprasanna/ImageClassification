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
    
    # for i in range(1, num + 1):
    #     os.mkdir('/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_' + str(i) + '/')

    while last < len(cd_list):
        output.append(cd_list[int(last):int(last + avg)])
        last += avg

    # i = 0
    # for fold in output:
    #     j = 0
    #     for photo in fold[i]:
    #         print(fold)
    #         j += 1
    #         #shutil.move(photo[i][j], '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_' + str(i) + '/')
        # i += 1
    # print(len(output))
    # i = 0
    i = 0
    for l1sts in output:
        for photo in l1sts:
            print(photo[1])
            print(len(photo[1]))
            # if i in range(0,20):
            #     print('fold1')
            #     print(photo[1])
            #     # shutil.move(photo, '/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_1')
            # elif i in range(20,40):
            #     print('fold2')
            #     print(photo[1])
            # elif i in range(40, 60):
            #     print('fold3')
            #     print(photo[i])
            # elif i in range(60, 80):
            #     print('fold4')
            #     print(photo[i])
            # elif i in range(80, 100):
            #     print('fold5')
            #     print(photo[i])
            # i += 1
            

        # for subl1sts in l1sts:
        #     print(subl1sts[l1sts][1])

    # for k,v in output:
    #     if k < 21:
    #         shutil.move(v,'/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_1')
    #     elif k < 41:
    #         shutil.move(v,'/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_2')
    #     elif k < 61:
    #         shutil.move(v,'/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_3')
    #     elif k < 81:
    #         shutil.move(v,'/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_4')
    #     elif k < 101:
    #         shutil.move(v,'/Users/Carlos/Projects/Dogs_vs_Cats/photos/fold_5')

    return output
if __name__ == '__main__':
    main()