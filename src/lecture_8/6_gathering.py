import numpy as np
import matplotlib.pyplot as plt

# Assume 'people' and 'points' are numpy arrays holding the positions
# of people and gathering points, respectively.
# Each row of the array represents the (x, y) coordinates of a person/point.
# For instance:
people = np.random.rand(100, 2)  # 100 people in random positions
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])  # 4 gathering points

# Compute the squared Euclidean distance from each person to each point.
# We use '[:, np.newaxis, :]' to add an extra dimension to the arrays,
# so that broadcasting works when we subtract them.
squared_distances = np.sum((people[:, np.newaxis, :] - points[np.newaxis, :, :]) ** 2, axis=-1)

# Use argsort to find the indices of the nearest and second nearest points.
nearest_indices = np.argsort(squared_distances, axis=1)[:, :2]
# It could be done faster with 'np.argpartition', and then sorting the two nearest points.
# nearest_indices = np.argpartition(squared_distances, 2, axis=1)[:, :2]
# nearest_indices = np.sort(nearest_indices, axis=1)

# 'nearest_indices[i, j]' gives the index in 'points' of the j-th nearest point to the i-th person.
# print(nearest_indices)

# plot the points and people with a label for the nearest gathering point
plt.scatter(people[:, 0], people[:, 1], c=nearest_indices[:, 0])
plt.scatter(points[:, 0], points[:, 1], c='red')
plt.show()

# plot the points and people with a label for the second nearest gathering point
plt.scatter(people[:, 0], people[:, 1], c=nearest_indices[:, 1])
plt.scatter(points[:, 0], points[:, 1], c='red')
plt.show()
