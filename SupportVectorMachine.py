import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
import itertools
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.metrics import jaccard_score

data=pd.read_csv(r"C:\Users\venki\cell_samples.csv")
print(data.head())

#Dist of classes based on Clump thickness and uniformity of cell size
ax = data[data['Class'] == 4][0:50].plot(kind='scatter', x='Clump', y='UnifSize', color='DarkBlue', label='malignant');
data[data['Class'] == 2][0:50].plot(kind='scatter', x='Clump', y='UnifSize', color='Yellow', label='benign', ax=ax);
#The ax parameter allows for the benign points to be overlayed on the malignant scatter points 
plt.show()

#columns data types
print(data.dtypes)

#Dropping cols that aren't numerical (Ex: BareNuc)
data = data[pd.to_numeric(data['BareNuc'], errors='coerce').notnull()]
#errors parameter finds the rows of BareNuc col that don't have values, and replaces them with NaN
#Then, notnull() gets rid of all the rows with NaN, and finally the whole dataset will be set equal to all the rows that have valid int values
data["BareNuc"] = data["BareNuc"].astype("int")
#This line of code above rechecks through every row in the dataset, and ensures the values of the BareNuc col are ints
print(data.dtypes)

#assigning x and y datasets
feature = data[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
x=np.asarray(feature)
print(x[0:5])

y=np.asarray(data["Class"])
print(y[0:5])

#Train/Test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
print("Train set: ", x_train.shape, y_train.shape)
print("Test set: ", x_test.shape, y_test.shape)

#Creating the model
#Can't determine which is the best high-dimensional space to use right away so multiple need to be tested
#Starting with default RBF
clf=svm.SVC(kernel="rbf")
clf.fit(x_train, y_train)

yhat=clf.predict(x_test)
print(yhat)
print(y_test)

#Evaluation

#1) Confusion Matrix
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
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

#Computing the confusion matrix
matrix=confusion_matrix(y_test, yhat, labels=[2,4])
np.set_printoptions(precision=2)

print(classification_report(y_test, yhat))

#Plotting the non-normalized matrix
plt.figure()
plot_confusion_matrix(matrix, classes=["Benign(2)", "Malignant(4)"], normalize=False, title="Confusion Matrix")
plt.show()

#2) F1_score
print(f1_score(y_test, yhat, average="weighted"))

#3) Jaccard Score
print(jaccard_score(y_test, yhat, pos_label=2))
      













