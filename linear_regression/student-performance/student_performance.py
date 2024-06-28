import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import sklearn.linear_model
import sklearn.model_selection
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle

# Read in dataset (Source: https://archive.ics.uci.edu/dataset/320/student+performance)
data = pd.read_csv("student-mat.csv", sep=";")

# Trim data
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
print(data.head())

# What we want to predict - G3 is final grade
predict = "G3"

# Drops the "G3" column from the data and converts the remaining data to a NumPy array. 
# This array represents the features used for prediction.
X = np.array(data.drop([predict], axis=1))
# Extracts the "G3" column from the data and converts it to a NumPy array. 
# This array, y, represents the target values we want to predict.
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1, shuffle=True)

'''
# Multiple training iterations
best = 0
for _ in range(30):
# Splits the data into training and testing sets. 
# 10% of the data is reserved for testing while the remaining 90% is used for training
# The features are split into x_train and x_test, and the target values are split into y_train and y_test.
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1, shuffle=True)
    linear = linear_model.LinearRegression()

    # Train model
    linear.fit(x_train, y_train)
    # Accuracy
    acc = linear.score(x_test, y_test)
    if acc > best:
        best = acc
        # Save the trained model to a file so that it can be loaded and used later without needing to retrain it
        with open("studentmodel.pickle", "wb") as file:
            pickle.dump(linear, file)       # Serializes model and writes it to file
'''

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

# Method uses the trained linear regression model to make predictions on the test data (x_test). 
# The result is an array of predicted values corresponding to the input features in x_test
predictions = linear.predict(x_test)

# predictions[x]: The predicted value for the x-th test sample.
# x_test[x]: The feature values of the x-th test sample. This will be an array of feature values.
# y_test[x]: The actual target value for the x-th test sample.
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

# Can plot to see correlation between final grade 
p = "studytime"
pyplot.style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()