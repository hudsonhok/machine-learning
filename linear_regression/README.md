# Linear Regression

## What is it?

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. The goal is to find the linear equation (i.e. line of best fit) that best predicts the dependent variable based on the values of the independent variables.

The general formula for a linear regression model is:

\[ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n + \epsilon \]

- \( y \) is the dependent variable.
- \( \beta_0 \) is the intercept.
- \( \beta_1, \beta_2, \ldots, \beta_n \) are the coefficients for the independent variables \( x_1, x_2, \ldots, x_n \).
- \( \epsilon \) is the error term.

## What Linear Regression is Good For

1. **Predictive Modeling**: Linear regression is widely used for predicting outcomes. For example, predicting sales based on advertising spend.
2. **Understanding Relationships**: It helps to understand and quantify the relationship between variables. For example, how changes in temperature affect ice cream sales.
3. **Estimation**: It provides estimates of the effects of independent variables on the dependent variable.
4. **Baseline Models**: It serves as a simple baseline model before more complex models are considered.

## What Linear Regression is Not Good For

1. **Non-linear Relationships**: Linear regression is not suitable for modeling relationships that are not linear. If the relationship between the variables is curved or more complex, other methods like polynomial regression, decision trees, or neural networks may be better.
2. **Multicollinearity**: When independent variables are highly correlated with each other, it can distort the results and make the model unreliable.
3. **Outliers**: Linear regression is sensitive to outliers, which can significantly affect the model. Robust regression techniques might be necessary in the presence of outliers.

The dataset used in this project can be found [here](https://archive.ics.uci.edu/dataset/19/car+evaluation)


