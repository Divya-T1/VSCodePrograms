import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

#cmd prompt to download file is:
#curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv -o FuelConsumptionCo2.csv

df=pd.read_csv("C:\\Users\\venki\\FuelConsumptionCo2.csv")
print(df.head() )
print(df.describe())

#have to establish the list of columns you want to focus on and then call the df function
cdf=df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']] 
print(cdf.head(9))
#Plotting the features
viz=cdf[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
viz.hist()
plt.show()

#plotting features to find the linear relationship
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
plt.xlabel('FUELCONSUMPTION_COMB')
plt.ylabel('CO2EMISSIONS')
plt.show()

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

#Going to utilize the train/test split method to create an accurate model for the data
#Need to randomely choose 80% of the rows for the train set, and the remainder 20% of the rows will be the test set
mask=np.random.rand(len(df))<0.8
train=cdf[mask]
test=cdf[~mask] #~ is the same as not, so rows not assigned to mask or the train set are part of the test set

#Training the data
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

#Modeling using the sklearn package
reg=linear_model.LinearRegression()
train_x=(train[['ENGINESIZE']])
train_y=(train[['CO2EMISSIONS']])
reg.fit(train_x, train_y)
#To get the coefficients produced by the model
print('Coefficients: ', reg.coef_)
print("Intercept: ", reg.intercept_)

#Now, we can plot the reg line over the data
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.plot(train_x, reg.coef_[0][0]*train_x+reg.intercept_[0],'-r')
plt.xlabel("Engine Size")
plt.ylabel("Emission")
plt.show()

#Determining the accuracy of the model vs the data
test_x=np.asanyarray(test[['ENGINESIZE']]) #asanyarray isn't required, can directly call test[['ENGINESIZE']]
test_y=np.asanyarray(test[['CO2EMISSIONS']])
predictions=reg.predict(test_x)
print("Mean absolute error: %.2f" % np.mean(np.absolute(predictions-test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((predictions-test_y)**2))
print("R2-score: %.2f" % r2_score(test_y, predictions)) 


