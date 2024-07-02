import pandas as pd
import numpy as np
import sklearn
import sklearn.model_selection
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

data = pd.read_csv("car.data")
print(data.head())

# Initialize labelencoder to convert categorical data into numerical data
le = preprocessing.LabelEncoder()
# Encoding categorical columns
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

# Target variable for prediction
predict = "class"

# Creating feature set (X - input variables used by model to make predictions) and labels (y - output variable model is trained to predict)
X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

# Splitting data into training and testing sets (10% for testing)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

# Initializing KNN classifier with 10 neighbor
model = KNeighborsClassifier(n_neighbors=10)

# Training the model on the training data
model.fit(x_train, y_train)

# Evaluating the model on the test data
acc = model.score(x_test, y_test)
print(acc)

# Making predictions on the test data
predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

# Displaying predictions, actual values, and nearest neighbors
for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    n = model.kneighbors([x_test[x]], 9, True) # Finding 9 nearest neighbors
    print("N: ", n)