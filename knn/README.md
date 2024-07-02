# K-Nearest Neighbors (KNN)

## Overview

K-Nearest Neighbors (KNN) is a learning algorithm used for classification and regression tasks in machine learning. It operates on the principle that similar instances exist in close proximity to each other.

### How it Works

1. **Data Storage**: KNN stores all available cases and classifies new cases based on a similarity measure (e.g., distance functions).
2. **Distance Calculation**: For a new instance, KNN computes the distance from the new instance to all stored instances. One common distance measure is the Euclidean distance.
3. **Selection of Neighbors**: The algorithm selects the `k` nearest instances to the new instance. The value of `k` is a user-defined constant.
4. **Voting (Classification)**: In a classification task, the class labels of the `k` nearest neighbors are gathered, and the most frequent class label among them is assigned to the new instance.
5. **Averaging (Regression)**: In a regression task, the average value of the `k` nearest neighbors is computed and assigned to the new instance.

### Advantages of KNN

- **Simplicity**: Easy to implement and understand.
- **No Training Phase**: KNN does not involve a training phase, making it fast for smaller datasets.
- **Adaptability**: Can be used for both classification and regression problems.

### Disadvantages of KNN

- **Computationally Intensive**: Becomes slow as the size of the dataset increases because it computes the distance for each query instance to all instances in the training data.
- **Storage Requirements**: Needs to store all training data.
- **Sensitive to Irrelevant Features**: Performance can be degraded by irrelevant features.

## KNN in the Context of Car Evaluation

In the context of the Car Evaluation dataset, KNN can be used to classify cars into different categories of acceptability (unacceptable, acceptable, good, very good) based on their features (buying price, maintenance cost, number of doors, passenger capacity, luggage boot size, and safety).

### Steps Involved

1. **Data Preprocessing**: Encode categorical data into numerical values using `LabelEncoder`.
2. **Feature Extraction**: Combine the encoded features into a single feature set using `zip`.
3. **Data Splitting**: Split the dataset into training and testing sets using `train_test_split`.
4. **Model Training**: Instantiate the KNN classifier with a chosen value of `k` (e.g., `k=10`) and train it using the training data.
5. **Model Evaluation**: Evaluate the model on the test data by measuring its accuracy.
6. **Prediction**: Use the trained model to predict the class of new car instances.

The dataset used in this project can be found [here](https://archive.ics.uci.edu/dataset/19/car+evaluation)