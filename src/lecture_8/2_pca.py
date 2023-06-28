import numpy as np
import cv2
import matplotlib.pyplot as plt

# Create a binary mask image.
mask = np.zeros((100, 100), dtype=np.uint8)

# draw a ellipse inclined at 30 degrees
cv2.ellipse(mask, (50, 50), (30, 20), 40, 0, 360, 255, -1)

# plot the mask
plt.imshow(mask, cmap='gray')
plt.show()


# Compute the indices of non-zero elements in the mask.
y_idx, x_idx = np.nonzero(mask)

# Compute the center of the mask.
center_y, center_x = np.mean(y_idx), np.mean(x_idx)
print("Center of the mask: ({}, {})".format(center_x, center_y))

# Perform PCA to find the major and minor axes.
# Subtract the mean.
x = x_idx - center_x
y = y_idx - center_y

# Create the covariance matrix.
cov_matrix = np.cov(x, y)

# Compute the eigenvalues and eigenvectors.
eig_val, eig_vec = np.linalg.eig(cov_matrix)

# The eigenvalues correspond to the variance along the axes.
# The eigenvectors correspond to the directions of the axes.
# Sort the eigenvalues and corresponding eigenvectors in decreasing order.
idx = np.argsort(eig_val)[::-1]
eig_val = eig_val[idx]
# eig_val[ np,array([1, 0]) ]
eig_vec = eig_vec[:, idx]

major_axis = eig_vec[:, 0]
minor_axis = eig_vec[:, 1]

# compute the angle of the major axis with the x-axis
angle = np.arctan2(major_axis[1], major_axis[0]) * 180 / np.pi
print("Angle of the major axis with the x-axis: {}".format(angle))

print("Major axis direction: {}".format(major_axis))
print("Minor axis direction: {}".format(minor_axis))

