#from movies import movie_dataset,movie_lables,normalize_point
import pandas as pd
import glob

def main():
    test = pd.read_csv('/Users/Carlos/data_mining/kNN/banana-10-1tst.dat',header = None)
    train = pd.read_csv('/Users/Carlos/data_mining/kNN/banana-10-1tra.dat',header = None)

    #def datasplit()

    #df = df.drop(df.index[0:11])
    df = test.reset_index()
    df = df.drop('index', axis=1)
    labels = df[df.columns[len(df.columns)-1]]
    testlabels = labels
    testvals = df
    df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
    #print(df)

    print(classify([-1.05, 0.72],testvals,testlabels,10))
    print(classifytest(testvals,testlabels,train,trainlabels,1))

#euclidean distance
def dis(obj1,obj2):
    squarediff = 0
    for i in range(len(obj1)):
        squarediff = (obj1[i]-obj2[i])**2
    finaldis = squarediff**.5
    return finaldis
#finds k neighbors and returns prediction for one point

def classify(unknown, dataset, labels, k):

  distances = pd.DataFrame(columns=('Dist','label'))
  #Looping through all points in the dataset
  for i in range(len(dataset)):
      distances.loc[i]= list([dis(dataset.iloc[i],unknown),labels[i]])
      #print(dis(dataset.iloc[i],unknown))

  #print(distances)
  distances.sort_values('Dist')
  kneighbors = distances[0:k]
  #print(kneighbors)
  Op1 = 0
  Op2 = 0
  for i in range(len(kneighbors)):
    if kneighbors.at[i,'label']==-1:
          Op2 = Op2+1
    else:
        Op1 = Op1+1
  #if equal go with Op1
  if Op2>Op1:
      return -1
  else:
      return 1


def classifytest(train,trainlabels,test,testlabels,k):
    predictions = pd.DataFrame(columns=(['label']))
    classifications =[]
    for i in range(len(test)-510):
        #print(test.iloc[i])
        #classifications.append(classify(test.iloc[i], train,trainlabels,k))
        #print(classify(test.iloc[i], train,trainlabels,k))
        predictions.loc[i] = list([classify(test.iloc[i], train,trainlabels,k)])
        #predictions.loc[i] = list([classify([3,2], train, trainlabels, k)])
    #classifications = pd.DataFrame(classifications)
    return predictions




#repurposed from stackexchange
def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result

if __name__ == '__main__':
    main()