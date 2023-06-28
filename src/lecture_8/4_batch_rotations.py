import numpy as np
import matplotlib.pyplot as plt

# Set the batch size and number of points
batch_size = 1000
num_points = 100

# Create a batch of 3D point clouds
# Shape: (batch size, number of points, 3 coordinates)
points = np.random.rand(batch_size, num_points, 3)

# Create a batch of 3D rotation matrices
# Shape: (batch size, 3 rows, 3 columns)
# yaw is the rotation around the z-axis between -pi and pi
yaw = np.random.rand(batch_size) * 2 * np.pi - np.pi
# pitch is the rotation around the y-axis between -pi/2 and pi/2
# the probability of a rotation should be proportional to the cosine of the angle
pitch = np.arccos(np.random.rand(batch_size) * 2 - 1) - np.pi / 2
# plot the histogram of the pitch angles
plt.hist(pitch, bins=20)
plt.show()
# roll is the rotation around the x-axis between -pi and pi
roll = np.random.rand(batch_size) * 2 * np.pi - np.pi
# Create the rotation matrices
yaw_matrix = np.array([[np.cos(yaw), -np.sin(yaw), np.zeros_like(yaw)],
                          [np.sin(yaw), np.cos(yaw), np.zeros_like(yaw)],
                            [np.zeros_like(yaw), np.zeros_like(yaw), np.ones_like(yaw)]])
pitch_matrix = np.array([[np.cos(pitch), np.zeros_like(pitch), np.sin(pitch)],
                            [np.zeros_like(pitch), np.ones_like(pitch), np.zeros_like(pitch)],
                            [-np.sin(pitch), np.zeros_like(pitch), np.cos(pitch)]])
roll_matrix = np.array([[np.ones_like(roll), np.zeros_like(roll), np.zeros_like(roll)],
                            [np.zeros_like(roll), np.cos(roll), -np.sin(roll)],
                            [np.zeros_like(roll), np.sin(roll), np.cos(roll)]])

print(yaw_matrix.shape)
# transpose the matrices to have the batch dimension as the first dimension
yaw_matrix = np.transpose(yaw_matrix, (2, 0, 1))
pitch_matrix = np.transpose(pitch_matrix, (2, 0, 1))
roll_matrix = np.transpose(roll_matrix, (2, 0, 1))

# Combine the rotation matrices with yaw, pitch and roll, i.e. not aeroplane style
# this way the pitch is the only rotation that needs a non uniform distribution
rotations = np.einsum('bij,bjk,bkl->bil', roll_matrix, pitch_matrix, yaw_matrix)

# Use np.einsum to apply the batch of 3D rotation matrices to the batch of 3D point clouds
# The 'bij,bkj->bki' means that for each batch (b) and each point (k),
# we want to multiply the rotation matrix indexed by i and j
# with the point cloud point indexed by j, resulting in the rotated point indexed by i
rotated_points = np.einsum('bij,bkj->bki', rotations, points)

# Check the shape of the output
print(rotated_points.shape)  # Should be (batch_size, num_points, 3)
