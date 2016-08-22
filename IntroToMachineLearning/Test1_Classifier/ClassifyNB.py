
from sklearn.naive_bayes import GaussianNB

def classify(features_train, labels_train):
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!
    gnb = GaussianNB()
    model = gnb.fit(features_train,labels_train);
    return model