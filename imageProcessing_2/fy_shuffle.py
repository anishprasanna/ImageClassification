import random

def main():
    n = input('Please input the size of the array:\n')
    int(n)
    array = input('please input array. Ex. [1,2,3] should be inputted as 123\n')
    arr = map(int,str(array))
    
    # shuffler(array_to_shuffle)
    randomizer(arr, n)

def randomizer(arr, n):                 #correct attempt
    for i in range(n-1, 0, -1):
        j = random.randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
    print(arr)

# def shuffler(array_to_shuffle):         #my attemot
#     for i in reversed(array_to_shuffle):
#         j = random.randint(0, len(array_to_shuffle))
#         array_to_shuffle[i] = j

#     print(array_to_shuffle)
    
if __name__ == '__main__':
    main()