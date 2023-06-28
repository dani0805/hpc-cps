import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import time

# Function to compute best fit
@tf.function
def best_fit(X, Y):
    xbar = tf.reduce_mean(X)
    ybar = tf.reduce_mean(Y)
    n = tf.size(X, out_type=tf.float32)

    numer = tf.reduce_sum(X*Y) - n * xbar * ybar
    denum = tf.reduce_sum(X**2) - n * xbar**2

    m = numer / denum
    b = ybar - m * xbar

    return m, b

# Create a large dataset with 1M points
N = 1000000
X = np.random.rand(N)
Y = 3*X + 2 + np.random.normal(scale=0.1, size=N)  # predefined linear equation plus noise

# Convert to tensors
X = tf.constant(X, dtype=tf.float32)
Y = tf.constant(Y, dtype=tf.float32)

m, b = None, None
for _ in range(10):
    # Calculate best fit
    start_time = time.time()
    m, b = best_fit(X, Y)
    print("Time taken:", time.time() - start_time)

print('Best fit line:\ny = {:.2f}x + {:.2f}'.format(m, b))
# Plot the data and the best fit line
plt.scatter(X, Y, s=0.1, color='blue')
plt.plot(X, m*X + b, color='red')
plt.show()
