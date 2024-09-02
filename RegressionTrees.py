# Pandas will allow us to create a dataframe of the data so it can be used and manipulated
import pandas as pd
# Regression Tree Algorithm
from sklearn.tree import DecisionTreeRegressor
# Split our data into a training and testing data
from sklearn.model_selection import train_test_split
from sklearn import metrics

my_data=pd.read_csv("C:\\Users\\venki\\real_estate_data.csv")
print(my_data.head())
print(my_data.shape)

#Data has missing values, and the isna() identifies the missing values for each column and returns a boolean value
#the sum() method in the line below adds up all the True returned by isna() for each column
print(my_data.isna().sum())

#Dropping the rows with the missing values
my_data.dropna(inplace=True) #the dropna method permanently drops the entire row if a missing value is present if the inplace parameter is equal to True; if False, a new DataFrame is created with the original row, but excluding the missing values; the data itself remains unchanged

#Recheck to ensure missing info rows have been removed
print(my_data.isna().sum())

#Creating the feature and target sets
x=my_data.drop(columns=["MEDV"])
y=my_data["MEDV"] #Only 1 column so don't need second set of square brackets
#Using single brackets makes the result a Pandas series, but using doubles brackets results in Pandas DataFrame
print(x[0:5])
print(y[0:5])

#Splitting the test and train data
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=1)

#Creating the Regression Tree
regTree=DecisionTreeRegressor(criterion="squared_error")

#Creating the model
regTree.fit(x_train, y_train)

#Evaluation
print(regTree.score(x_test, y_test)) #will provide the R^2 value

pred=regTree.predict(x_test)

print("$", (pred-y_test).abs().mean()*1000)













