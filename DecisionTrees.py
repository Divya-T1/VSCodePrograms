import sys
import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree as tree
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz

my_data=pd.read_csv("C:\\Users\\venki\\drug200.csv")
print(my_data.head())
print(my_data.shape)

#Declaring the Features
x=my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
print(x[0:5])

#sklearn decision trees doesn't handle categorical values, so LabelEncoder() method needs to be used to convert the categorical values into dummy/indicator value
le_sex=preprocessing.LabelEncoder()
le_sex.fit(["F", "M"])
x[:,1]=le_sex.transform(x[:,1])
'''
preprocessing.LabelEncoder() -> intializes the LabelEncoder() to switch categorical variable to numerical variable
x[:,1] -> tells the computer to focus on the second column (the sex column)
le_sex.fit(...) -> assigns the possible categorical values to numeric values (F=0 and M=1)
transfrom -> officially changes the data in the sex column to follow the pattern set by the fit method
'''

le_BP=preprocessing.LabelEncoder()
le_BP.fit(["LOW", "NORMAL", "HIGH"])
x[:,2]=le_BP.transform(x[:,2])

#In the le_BP scenario, Low=1, Normal=2, and High=0 because the order of the label is given alphabetically

le_Chol=preprocessing.LabelEncoder()
le_Chol.fit(["NORMAL", "HIGH"])
x[:,3]=le_Chol.transform(x[:,3])

print(x[0:5])

#Declaring the target variable
y = my_data["Drug"]
print(y[0:5])



#Splitting the data into test and train sets
X_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.3, random_state=3)

#Modeling the data
drugTree=DecisionTreeClassifier(criterion="entropy", max_depth=4)
print(drugTree)

drugTree.fit(X_train, y_train)

#Predictions
predTree=drugTree.predict(x_test)

print(predTree[0:5])
print(y_test[0:5])

#Evaluation
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_test, predTree))
#always true variables first and then the predicted values

#Visualization
export_graphviz(drugTree, out_file='tree.dot', filled=True, feature_names=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])













