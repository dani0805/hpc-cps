import tensorflow as tf
import time
from matplotlib import pyplot as plt

# generate random data
tf.random.set_seed(42)
data = tf.random.normal([1000000, 100])

@tf.function
def pca(data):
    # normalize data
    data -= tf.reduce_mean(data, axis=0)
    data /= tf.math.reduce_std(data, axis=0)
    # compute covariance matrix
    covariance_matrix = tf.linalg.matmul(tf.transpose(data), data) / tf.cast(tf.shape(data)[0], tf.float32)
    # compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = tf.linalg.eigh(covariance_matrix)
    # sort eigenvalues and corresponding eigenvectors
    sorted_index = tf.argsort(eigenvalues, direction='DESCENDING')
    sorted_eigenvectors = tf.gather(eigenvectors, sorted_index)
    # Select the first 2 principal components
    principal_components = sorted_eigenvectors[:, :2]
    return principal_components

principal_components = None

for _ in range(10):
    #time the execution
    now = time.time()

    principal_components = pca(data)

    # Print the execution time
    print(f"Tensorflow implementation took {time.time() - now} seconds") # ~ 0.04 seconds

# Project data onto the principal components
projected_data = tf.linalg.matmul(data, principal_components)

# Plot the projected data
plt.scatter(projected_data[:, 0], projected_data[:, 1], alpha=0.5)
plt.show()
