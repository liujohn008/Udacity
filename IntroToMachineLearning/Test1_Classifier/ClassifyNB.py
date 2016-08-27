
from sklearn.naive_bayes import GaussianNB

from sklearn import svm

def classify(features_train, labels_train):
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!
  ## Use Naive Bayes Model
    #gnb = GaussianNB()
    #model = gnb.fit(features_train,labels_train);
    #return model
  ## Use SVM Model
    clf = svm.SVC(kernel='rbf',C=1)
    clf.fit(features_train,labels_train)
    return clf
