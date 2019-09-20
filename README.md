# Data Mining Homework #2 - Implementing KNN with Images
In this project we will organize and extract features from images for use with our implemented KNN algorithm. The functions necessary for the project to run are located in their respective files and folders.

Disclaimer:
Our images for use in our algorithm were taken from the [Cats & Dogs Kaggle dataset](https://www.kaggle.com/chetankv/dogs-cats-images/version/1)

Within this Project, the following people worked on the following parts:
Alex Brockman:
- Computer Vision, feature extractions (feature_extraction.py), along with editing/updating main.py/knn.py

Andrew Haisfield:
- Implementing/integrating knn to dog/cat photos (knn.py), helped with creating/updating main.py

Anish Prasanna:
- implemented sci-kit learn algorithms, helped update main for data frames, wrote latex paper (knn.py)

Carlos Samaniego:
- Created original foundation of main, including fisher-yates shuffler, folding, cross validation, directory creation (main.py)

In the ZIP file, we do not use the following scripts: fy_shuffle.py, scikit.py, and old_main.py

Running the project:
1. Before you run the project, please be sure to make an environment and pip install -r requirements.txt within the environment.
2. Run the following command, "python main.py"
You should see the following output:

```
Finding best k-value from 1-10
Making predictions for k =  1
1 out of 20 completed
2 out of 20 completed
3 out of 20 completed
4 out of 20 completed
5 out of 20 completed
6 out of 20 completed
7 out of 20 completed
8 out of 20 completed
9 out of 20 completed
10 out of 20 completed
11 out of 20 completed
12 out of 20 completed
13 out of 20 completed
14 out of 20 completed
15 out of 20 completed
16 out of 20 completed
17 out of 20 completed
18 out of 20 completed
19 out of 20 completed
20 out of 20 completed
Prediction accuracy: 55.00000000000001%
Making predictions for k =  2.... all the way to k = 10.
then it will output
Best k-value =  2
Algorithm Run Time: 3.8419430255889893 seconds 
Average cross-validated accuracy: 50.0
```

Then it will show you a graph relating to accuracy for each k value. You close the graph, another graph on the time for each scikit classification algorithm then in the console, it will add:

```
KNN scikit accuracy 0.45
KNN scikit time taken: 0.004269123077392578
Linear Kernel SVM Accuracy: 0.55
KNN Linear Kernel SVM  time taken: 0.09250092506408691
Naive Bayes Accuracy: 0.6
Naive Bayes  time taken: 0.003875255584716797
```

And then when you exit that graph, another graph will show, that will describe Scikit classification algorithm accuracies. And that is all!
