import time

from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.signal import convolve2d

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


def diffuse(grid):
    # Naive Implementation
    # time the execution
    now = time.time()
    frames = [grid]
    # 2D Laplacian kernel
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

    # Diffusion Simulation

    for timestep in range(timesteps):
        # Calculate the new state of the grid using 2D convolution
        grid = grid + D * convolve2d(grid, kernel, mode='same')
        frames.append(grid)

    # Print the execution time
    print(f"Numpy implementation took {time.time() - now} seconds for {timesteps} timesteps") # ~ 20 seconds
    return frames


frames = diffuse(grid)

# Create a figure for the plot
fig, ax = plt.subplots()

# Create a function that will do the plotting
def animate(i):
    ax.clear()
    im = ax.imshow(frames[i])
    return [im]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=16, blit=True)

ani.save("diffusion_2.mp4", writer='ffmpeg')
