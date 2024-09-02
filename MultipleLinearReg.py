import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model

df=pd.read_csv("C:\\Users\\venki\\FuelConsumptionCo2.csv")
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']] 
#creating the cdf and utilizing this rather than the df allows less memory usage as the program only focuses on the specified subset of columns
print(cdf.head(9))

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine Size")
plt.ylabel("Emission")
plt.show()

#Train/Test Split Method
rand=np.random.rand(len(df)) < 0.8
train=cdf[rand]
test=cdf[~rand]

#Creating a plot of the training data
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.xlabel("Engine Size")
plt.ylabel("Emissions")
plt.show()

#Creating the multiple regression model
reg=linear_model.LinearRegression()
x=train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']]
y=train[['CO2EMISSIONS']]
reg.fit(x, y)
print("Coefficients: ", reg.coef_) #getting the parameters
#The Ordinary Least Squares (OLS) method is used to produce these parameters; essentially, OLS tries to minimize the MSE to determine these coefficients and uses methods such as optimization algorithm

#Predictions
predictions=reg.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
x=test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']]
y=test[["CO2EMISSIONS"]]
#Determining the Accuracy
print("Mean Squared Error(MSE): %.2f" % np.mean((predictions-y)**2))
#Determining Variance Score (1=perfect prediction)
print("Variance Score: %.2f" % reg.score(x, y))





