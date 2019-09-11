from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import math
import zipfile
import urllib.request
import os

original_training_file = '/Users/Carlos/data_mining/kNN/titanic-10-1tra.dat'
original_test_file = '/Users/Carlos/data_mining/kNN/titanic-10-1tst.dat'

def main():
    mode = input("please enter either 1 for baseline, 2 for good, or 3 for excellent.\n")
    
    if mode == 1:
        print('this is 1!!!')


    # url_of_zipped_data = input('Please input the url of the zipped dataset:\n')
    # zipped_filename = input('Please input the last part of the url. ex.banana-10-fold.zip:\n')
    # zipped_folder_name = input('What would you like the folder of the unzipped files to be called?\n')
    # fetch_zipped_folder(url_of_zipped_data, zipped_filename, zipped_folder_name)
    
    try:
        os.mkdir(zipped_folder_name+'/Training_Set')
        os.mkdir(zipped_folder_name+'/Test_Set')
    except OSError:
        print("Creation of the directories {0}, {1} failed".format(training_path,test_path))
    else:
        print("Successfully created directories {0}, {1}".format(training_path,test_path))

    # cleaned_tra_name = input('How would you like the cleaned training set to be called? ex. "titanic-10-1tra-cleaned.dat"\n')
    # cleaned_tst_name = input('How would you like the cleaned test set to be called? ex. "titanic-10-1tst-cleaned.dat"\n')
    # clean(original_training_file, cleaned_tra_name)
    # clean(original_training_file, cleaned_tst_name)

    
    #put cleaned files in DataFrames
    #read_csv
    # training_data = pd.read_csv('/Users/Carlos/data_mining/kNN/titanic-10-1tra-cleaned.dat',header=None)
    # test_data = pd.read_csv('/Users/Carlos/data_mining/kNN/titanic-10-1tst-cleaned.dat',header=None)
    # training_data.columns = ['Class', 'Age', 'Sex', 'Survived']
    # test_data.columns = ['Class', 'Age', 'Sex', 'Survived']
    # print(training_data.head())
    # print(test_data.head())

def fetch_zipped_folder(url_of_zipped_data, zipped_filename, zipped_folder_name):
    urllib.request.urlretrieve(url = url_of_zipped_data, filename = zipped_filename)        #use of urllib.request.retrieve given by Sarah P.
    with zipfile.ZipFile(zipped_filename, 'r') as zip_ref:                                  #used of zipfile.ZipFile, extractall by Sarah P. 
        zip_ref.extractall(zipped_folder_name)

def clean(original_file, cleaned_file_name):
    with open(original_file, 'r') as rf:
        wf = open(cleaned_file_name,'w')
        for line in rf:    
            lines = rf.readlines()
            for line in lines:
                if '@' not in line:
                    wf.write(line)
    

def euclidean_distance(x,y):
    x = (5,6,7)
    y = (8,9,9)

    distance1 = 0
    for a, b in zip(x,y):
        distance1 += ((a-b)**2)
    distance1 = math.sqrt(distance1)
    print(distance1)

if __name__ == '__main__':
    main()