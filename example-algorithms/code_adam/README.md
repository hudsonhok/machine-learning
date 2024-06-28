# Adam Optimization Algorithm

The Adam optimization algorithm is a gradient-based optimization algorithm used in deep learning that incorporates two techniques: adaptive learning rates and momentum. It’s the extended version of the stochastic gradient descent algorithm, which is used to update the parameters of a model in the direction of the negative gradient of the loss function.

## Step-by-Step Process:

1. **Initialize the model parameters** (weights and biases) with small random values.
2. **Initialize two variables** `m` and `v` to keep track of the first and second moments of the gradient.
3. **Initialize a variable** `t` as an iteration counter.
4. Calculate the gradient of the loss function with respect to the weights and biases using backpropagation.
5. Update the first moment `m` using a moving average of the gradient. The equation for this is:
    - `m(t) = beta1 * m(t-1) + (1 – beta1) * g(t)`
    - where `beta1` is the decay factor for first momentum and `g(t)` is the gradient (partial derivatives).
6. Update the second moment `v` using a moving average of the squared gradient. The equation for this is:
    - `v(t) = beta2 * v(t-1) + (1 – beta2) * g(t)^2`
    - where `beta2` is the decay factor for the infinity norm (it’s a hyperparameter that controls the weighting given to the previous value of `v`).
7. Compute bias-corrected moments (since the first and second moments are biased towards zero at the beginning of training). The equations for this are as follows:
    - `mhat(t) = m(t) / (1 – beta1^t)`
    - `vhat(t) = v(t) / (1 – beta2^t)`
8. Update the model parameters using the bias-corrected moments and a learning rate, `alpha`. The equation for this is as follows:
    - `x(t) = x(t-1) – alpha * mhat(t) / (sqrt(vhat(t)) + eps)`
    - where `x(t)` is the value for the parameter and `epsilon` is a small constant added to the denominator to prevent division by zero.
9. Increment the iteration counter `t` by 1.

## Repeat:
Steps 4-9 are repeated until the specified number of iterations is reached or the convergence criterion is met.
