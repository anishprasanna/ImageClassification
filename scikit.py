from sklearn.neigbors import KNeighborsClassifier
from feature_extraction import *
from knn import *
    
    # sk_random_forest()
    # sk_gradient_boosting()


def sk_knn(test, training, knn_val): 
    our_model = KNeighborsClassifier(n_neighbors= knn_val)
    our_model.fit(training, test)
    # our_model.fit(x_training_data, y_training_data)
    
    # x is the values and y is just labels
    # Predict:
    # Returns a list of predicted classes - one prediction for every data point
    predictions = our_model.predict(your_x_data)
    
    # For every data point, returns a list of probabilities of each class
    probabilities = your_model.predict_proba(your_x_data)

def sk_random_forest():
    print('this method is for random forest classifier')

def sk_gradient_boosting():
    print('this method is for gradient boosting classifier')

if __name__ == '__main__':
    main()