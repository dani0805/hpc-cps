import time

from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
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
timesteps = 100


def diffuse(grid):
    # Naive Implementation
    # time the execution
    now = time.time()
    frames = [grid]
    for timestep in range(timesteps):
        # Create a new grid to hold the next state
        new_grid = [[0.0 for _ in range(n)] for _ in range(n)]

        # Calculate the new state of each cell
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                # Use the 2D discrete diffusion equation
                new_grid[i][j] = grid[i][j] + D * (
                        grid[i - 1][j]
                        + grid[i + 1][j]
                        + grid[i][j - 1]
                        + grid[i][j + 1]
                        - 4 * grid[i][j]
                )
        frames.append(new_grid)
        # Update the grid
        grid = new_grid
    # Print the execution time
    print(f"Naive implementation took {time.time() - now} seconds for {timesteps} timesteps") # ~ 30 seconds for 100 timesteps
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

ani.save("diffusion_1.mp4", writer='ffmpeg')
