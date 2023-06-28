import numpy as np
import matplotlib.pyplot as plt

# Seed for reproducibility
np.random.seed(0)

# Generate random data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add a column of ones for the bias term
X_b = np.c_[np.ones((100, 1)), X]

# Initialize weights randomly
weights = np.random.randn(2, 1)

# Learning rate
eta = 0.1

# Maximum iterations
max_iter = 1000

# Tolerance for stopping criterion
tol = 1e-6

# Variable to store the loss
prev_loss = np.inf

loss_history = []
# Gradient descent loop
for iteration in range(max_iter):
    # Compute predictions
    preds = np.dot(X_b, weights)
    print(preds[:3])

    # Compute error
    error = preds - y

    # Compute loss
    loss = (error ** 2).mean()

    # If the improvement in loss is less than the tolerance, stop
    if prev_loss - loss < tol:
        print(f'Stopping after {iteration} iterations.')
        break

    # Compute gradients
    gradients = 2 * np.dot(X_b.T, error) / len(X_b)

    # Update weights
    weights -= eta * gradients

    # Update previous loss
    prev_loss = loss

    # Store the loss
    loss_history.append(loss)


print('Weights:', weights)

# Plot the data and the model prediction
plt.scatter(X, y)
plt.plot(X, np.dot(X_b, weights), color='red')
plt.show()

# transform the loss history logaritmically
loss_history = np.log(loss_history)
# Plot the loss over iterations
plt.plot(loss_history)
plt.xlabel('Iteration')
plt.ylabel('Loss (log)')
plt.show()