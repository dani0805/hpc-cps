import time

from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tensorflow as tf

# Problem Setup

# set the random seed
np.random.seed(42)

# Size of the grid
n = 1000

# Initialize grid
grid = [[0.0 for _ in range(n)] for _ in range(n)]

# Initial substance is randomly distributed in 50 cells
for _ in range(50):
    i = np.random.randint(1, n - 1)
    j = np.random.randint(1, n - 1)
    grid[i][j] = 1.0

# Diffusion coefficient
D = 0.2

# Timesteps
timesteps = 1000


@tf.function
def diffuse(grid):
    # Naive Implementation
    frames = [grid]
    # 2D Laplacian kernel
    kernel = tf.constant([[0.0, 1.0, 0.0], [1.0, -4.0, 1.0], [0.0, 1.0, 0.0]])
    kernel = tf.reshape(kernel, [3, 3, 1, 1])

    # Diffusion Simulation

    for timestep in range(timesteps):
        # Expand dimensions of the grid for convolution
        grid_expanded = tf.expand_dims(tf.expand_dims(grid, axis=-1), axis=0)

        # Calculate the new state of the grid using 2D convolution
        grid = grid + D * tf.nn.conv2d(grid_expanded, kernel, strides=[1, 1, 1, 1], padding='SAME')[0, :, :, 0]
        frames.append(grid)

    return frames
for _ in range(10):
    # time the execution
    now = time.time()
    frames = diffuse(tf.constant(grid))
    # Print the execution time
    print(f"Tensorflow implementation took {time.time() - now} seconds for {timesteps} timesteps")

# Create a figure for the plot
fig, ax = plt.subplots()

# Create a function that will do the plotting
def animate(i):
    ax.clear()
    im = ax.imshow(frames[i].numpy())
    return [im]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=16, blit=True)

ani.save("diffusion_4.mp4", writer='ffmpeg') # ~ 0.3 seconds
