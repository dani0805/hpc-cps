import numpy as np
import matplotlib.pyplot as plt
import time

# generate random data
np.random.seed(42)
data = np.random.randn(1000000, 100)

#time the execution
now = time.time()

# normalize data
data -= np.mean(data, axis=0)
data /= np.std(data, axis=0)

# compute covariance matrix
covariance_matrix = np.cov(data, rowvar=False)

# compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# sort eigenvalues and corresponding eigenvectors
sorted_index = np.argsort(eigenvalues)[::-1]
sorted_eigenvectors = eigenvectors[:, sorted_index]

# Select the first 2 principal components
principal_components = sorted_eigenvectors[:, :2]

# Print the execution time
print(f"Numpy implementation took {time.time() - now} seconds") # ~ 0.5 seconds

# Project data onto the principal components
projected_data = np.dot(data, principal_components)

# Plot the projected data
plt.scatter(projected_data[:, 0], projected_data[:, 1], alpha=0.5)
plt.show()

