def main():
    sensitivity_calc(3,2)
    specificity_calc(4,3)
    accuracy_calc(3,4,3,2)

def sensitivity_calc(TP, FN):
    #some kind of for loop
    sensitivity = float(TP) / float(TP + FN)
    print("Sensitivity = {0}".format(sensitivity))

def specificity_calc(TN, FP):
    #some kind of for loop perhaps
    specificity = float(TN) / float(TN + FP)
    print("Specificity = {0}".format(specificity))

def accuracy_calc(TP, TN, FP, FN):
    sum = FN + FP + TN + TP
    accuracy = float(TP + TN) / float(sum) 
    print("Accuracy = {0}".format(accuracy))

#compares label sets and finds decimal
def accuracy(testlabels,classifylabels):                #Credit to Anish Prasanna
    correct = 0

    for i in range(len(testlabels)):
        if (testlabels.loc[i,'label'].item() == classifylabels.loc[i,'label'].item()):
            correct = correct +1
    return (correct/len(testlabels))
    
if __name__ == '__main__':
    main()