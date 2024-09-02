import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import jaccard_score
from sklearn.metrics import classification_report, confusion_matrix
import itertools
from sklearn.metrics import log_loss

data=pd.read_csv(r"C:\Users\venki\ChurnData.csv")
print(data.head())

#Choosing the features to focus on, and changing target data type to an int
data=data[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip',   'callcard', 'wireless','churn']]
data['churn']=data['churn'].astype('int') #originally a float and now type int
print(data.head())

#printing num of rows, num of cols, and the names of cols
print(data.shape)
print(data.columns)

#Defining the X and y for the datasets
x=np.asarray(data[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip',   'callcard', 'wireless','churn']])
print(x[0:5])

y=np.asarray(data['churn'])
print(y[0:5])

#Normalizing the data (making the features comparable)
x=preprocessing.StandardScaler().fit(x).transform(x)
print(x[0:5])

#Creating Training and Testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
print("Train set: ", x_train.shape, y_train.shape)
print("Test set: ", x_test.shape, y_test.shape)

#Creating the model
LR=LogisticRegression(C=0.01, solver="liblinear").fit(x_train, y_train)
#The C is the inverse of regulization strength and is a positive float
#regularization is a techinque that prevents or minimizes overfitting, and the smaller C is, the stronger the regularization
print(LR)

#Making predictions
yhat=LR.predict(x_test)
print(yhat)

#Returns prob for classes for each row (first column is prob of class 0 and second column is prob of class 1)
yhatProb=LR.predict_proba(x_test)
print(yhatProb)

#accuracy evals

#1) Jaccard Index 
print(jaccard_score(y_test, yhat, pos_label=0)) #The pos_label decides which class label (in this case 1 or 0) is the positive label (to determine teh true positive, false positive, true negative, and false negatives)
#So, in this scenario, the class label of 0 is considered the positive and 1 is considered the negative

#2) The confusion matrix
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
       """
    if normalize:
        cm=cm.astype("float")/cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print("Confusion matrix, without normalization")
    
    print(cm)

    plt.imshow(cm, interpolation="nearest", cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks=np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

print(confusion_matrix(y_test, yhat, labels=[1,0]))

#computing confusion matrix
cnf_matrix=confusion_matrix(y_test, yhat, labels=[1, 0])
np.set_printoptions(precision=2)

#Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=["churn=1", "churn=0"], normalize=False, title="Confusion Matrix")
plt.show()

#To get the full report of true and false positives/negatives
print(classification_report(y_test, yhat))

'''
Precision is a measure of the accuracy provided that a class label has been predicted. It is defined by: precision = TP / (TP + FP)
Recall is the true positive rate. It is defined as: Recall =  TP / (TP + FN)
F1 score is the harmonic average of the precision and recall, where an F1 score reaches its best value at 1 (perfect precision and recall) and worst at 0.
'''

#3) Log loss
print(log_loss(y_test, yhatProb))






