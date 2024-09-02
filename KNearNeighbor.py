import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df = pd.read_csv('C:\\Users\\venki\\teleCust100t.csv')
print(df.head())

#displaying the number of customers using each service
print(df['custcat'].value_counts())

#visual display of data
df.hist(column="income", bins=50)
plt.show()

print(df.columns) #the feature sets

#Converting the Pandas data frame to a Numpy Array
#for feature set and output (or labels)
X=df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']].values
X[0:5]

y=df['custcat'].values
y[0:5]

#Normalizing Data (Data Standardization gives the data zero mean and unit variance)
X=preprocessing.StandardScaler().fit(X).transform(X.astype(float))
'''
X.astype(float) -> ensures every element within the now NumPy array is a float
StandardScalar -> used to standardize features by eliminating the mean and scaling by unit variance
fit(X) -> computes the mean and standard deviation of each feature set
transform(...) -> Scales X to have a mean of 0 and an SD of 1 using data from fit()
Overall goal is to ensure everything is on the same scale
'''
print(X[0:5])

#Train/Test Split
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=4)
print("Train set: ", X_train.shape, y_train.shape)
print("Test set: ", X_test.shape, y_test.shape)

#Training datset and creating model
k=20
neigh=KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
print(neigh)

#Predicting based on the model
yhat=neigh.predict(X_test)
print(yhat[0:5])
print(y_test[0:5])

#Accuracy Eval (uses Jaccard_score)
print("Train set accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set accuracy: ", metrics.accuracy_score(y_test, yhat))

print()

#To find the best K value, start at K=1 and test the accuracy; then, increment the K till the optimal accuracy is found
K=10
mean=np.zeros((K-1)) #can also be np.zeros(K-1), but then, shape wouldn't be tuple which is less efficient in terms of readability
std=np.zeros(K-1)

for x in range(1, K):
    neigh=KNeighborsClassifier(n_neighbors=x).fit(X_train, y_train)
    yhat=neigh.predict(X_test)
    mean[x-1]=metrics.accuracy_score(y_test, yhat)
    std[x-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])

print(mean)

#Plotting the model accuracy for a different number of neighbors
plt.plot(range(1,K),mean,'g')
plt.fill_between(range(1,K),mean - 1 * std,mean + 1 * std, alpha=0.10)
plt.fill_between(range(1,K),mean - 3 * std,mean + 3 * std, alpha=0.10,color="green")
plt.legend(('Accuracy ', '+/- 1xstd','+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()

print( "The best accuracy was with", mean.max(), "with k=", mean.argmax()+1) 