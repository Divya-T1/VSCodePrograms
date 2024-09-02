import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn import svm

#SoftMax Regression

plot_colors="ryb" #Assigning colors to the classes (red, yellow, and blue)
plot_step=0.02 #Defining resolution of the plot (the smaller, the more points that are plotted, creating a finer grid)

#Creating a method that defines the visualization for the multiclass prediction model

def decision_boundary(X, y, model, iris, two=None):
    #The method definition:
    '''
    x: Feature matrix, y: target labels, model: the trained classfication model,
    iris: the dataset, two: optional parameter that handles a special case
    '''
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    #Calculate the min and max values for the 1st and 2nd features
    #the arange method creates an array of values from x_min to x_max with a step size of plot_step
    #the meshgrid takes the x and y array and creates a grid of points that cover the range of x and y with the given step by plot_step

    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
    #Configures the layout to ensure it is neatly arranged
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)
    #First line uses models to predict the class for each point in the grid
    #Second line reshapes the predictions from line one to match the grid shape
    #The cmap parameter colors each region a different color based on teh different classes
    #The function as a whole creates a plot that separates the plot into specific sections based on classes and plots the points that belong to each of the classes using xx and yy (their class label is determined using Z)

    if two:
        cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)
        for i, color in zip(np.unique(y), plot_colors):
            idx = np.where(y == i)
            plt.scatter(X[idx, 0], X[idx, 1], label=y, cmap=plt.cm.RdYlBu, s=15)
        plt.show()
    #Replots the decision boundary, scatter plot the data points for each class using different colors and displays the plot

    else:
        set_ = {0, 1, 2}
        print(set_)
        for i, color in zip(range(3), plot_colors):
            idx = np.where(y == i)
            if np.any(idx):
                set_.remove(i)
                plt.scatter(X[idx, 0], X[idx, 1], label=y, cmap=plt.cm.RdYlBu, edgecolor='black', s=15)
        for i in set_:
            idx = np.where(iris.target == i)
            plt.scatter(X[idx, 0], X[idx, 1], marker='x', color='black')

    '''    -Initialize a set set_ with class labels {0, 1, 2}.
        -Loop through the classes and plot the data points.
        -Remove classes from set_ if they have data points in y.
        -Plot remaining classes from iris.target with a different marker (x).
        -Display the plot.'''


#Now defining a function that will plot the prob of belonging to each class (col is the probability and row is the smaple #)
def plot_probability_array(X,probability_array):

    plot_array=np.zeros((X.shape[0],30))
    #2D array of 0's created that will store teh prob values for visualization
    col_start=0
    #The tracker for starting col index for each class's prob values
    ones=np.ones((X.shape[0],30))
    #another 2D array but of 1's and purpose unknown
    for class_,col_end in enumerate([10,20,30]):
        plot_array[:,col_start:col_end]= np.repeat(probability_array[:,class_].reshape(-1,1), 10,axis=1)
        col_start=col_end
    plt.imshow(plot_array)
    plt.xticks([])
    plt.ylabel("samples")
    plt.xlabel("probability of 3 classes")
    plt.colorbar()
    plt.show()

#Establishing the feature and target sets
pair=[1, 3] #includes Sepal Width, Petal Length, and Petal Width
iris = datasets.load_iris()
X = iris.data[:, pair]
print(X.shape) #output is 150 since it has (150,2) rows of data
y = iris.target
np.unique(y)

#Scatterplot of two features
scatter=plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu)
plt.xlabel("sepal width (cm)")
plt.ylabel("petal width")
cb=plt.colorbar(scatter)
plt.show()

#Creating and training the model
lr = LogisticRegression(random_state=0).fit(X, y)

#Generating the prob of the classes for each point
prob=lr.predict_proba(X)
print(prob)
print(len(prob))
print(prob[0])
print(prob[0].sum())

#Creating a distribution of the # of samples and the % of them being a part of a specific class
plot_probability_array(X, prob)

#Now, applying argmax to determine the class based on teh probability of the first point
print(np.argmax(prob[0]))

#Now, applying argmax to all 150 points of the sample
softmax_pred=np.argmax(prob, axis=1) #Axis=1 ensures the argmax function is applied to every row in the dataset
print(softmax_pred)

#Now, we verify if the predict function carries out this entire process of using softmax for probabilities and argmax to then identify the clas
yhat=lr.predict(X)
print(accuracy_score(yhat, softmax_pred))
#Since the output is 1.0, we know that the predict function is indeed carrying out this entire process

#Officially creating the boundary plot by using the decision_boundary method
decision_boundary(X,y,lr,iris)
plt.show()

#Or using an SVM model
model=svm.SVC(kernel="linear", gamma=0.5, probability=True)
model.fit(X,y)
decision_boundary(X,y,model,iris)
plt.show()



#One vs. All

#Creating the feature and target set
pair=[1, 3]
iris = datasets.load_iris()
X = iris.data[:, pair]
y = iris.target
print(np.unique(y)) #outputs the class labels

#Creating the dummy_class var
dummy_class=y.max()+1

#Creating a list to put the 3 classifier models that will be trained into one place
my_models=[]

#Iterating through each class label to create the classifier model for each and the dummy class for each
for class_ in np.unique(y):
    #selecting the index of our class
    select=(y==class_) #the boolean array identifies the samples belonging to the current class
    temp_y=np.zeros(y.shape) #creates an array of zeroes of size y.shape which is the # of rows in the dataset
    #All the values of the indexes in the array created in the line above that correspond to the indexes selected from the first line are set equal to the class label value
    temp_y[y==class_]=class_
    #Same idea as the line above expect this is the non-corresponding indexes, and they are set equal to the y_max()+1 value
    temp_y[y!=class_]=dummy_class
    #Now training the model after class label 0 points have been split
    model=SVC(kernel="linear", gamma=0.5, probability=True)
    my_models.append(model.fit(X, temp_y))
    #Now plotting the points for the model (red is the class we want to focus on and blue is the dummy class -> class samples are marked blue circles and dummy samples are blacks x's)
    decision_boundary(X, temp_y, model, iris)
    #plt.show()

#Now, we have to calculate the prob of each class samples belonging to each class (not the dummy samples)
#First, we create a 2D array with the same # of rows as X and 3 cols
prob_arr=np.zeros((X.shape[0],3))
#Iterates through my_models using model which will represent each of the three trained models, and j creates one col at a time as each col represents its probs
for j,  model in enumerate(my_models):
    #model.classes_ ensures each trained model is iterated, and the !=3 ensures that all the dummy class labels (3 since value was y.max()+1) are ignored
    #So, real_class identifies what the actual class label should be after avoiding the dummy class label
    real_class=np.where(np.array(model.classes_)!=3)[0]
    print(real_class)
    #Creates a jth column of all the probabilities associated with the column coresponding to the actual class (which is indiacted by [:,real_class]), and [:,0] ensures the prob values are a 1D array
    #So, the model.predict_proba essentially returns an array of all the probability estimates for each class label
    prob_arr[:,j]=model.predict_proba(X)[:,real_class][:,0]

#Prob of belonging to each class for the first sample
print()
print(prob_arr[0:,])




