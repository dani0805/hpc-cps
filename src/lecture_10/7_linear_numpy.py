import numpy as np
import matplotlib.pyplot as plt
import time

# Function to compute best fit
def best_fit(X, Y):
    xbar = np.mean(X)
    ybar = np.mean(Y)
    n = len(X)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    m = numer / denum
    b = ybar - m * xbar

    print('Best fit line:\ny = {:.2f}x + {:.2f}'.format(m, b))
    return m, b

# Create a large dataset with 1M points
N = 1000000
X = np.random.rand(N)
Y = 3*X + 2 + np.random.normal(scale=0.1, size=N)  # predefined linear equation plus noise

m, b = None, None
for _ in range(10):
    # Calculate best fit
    start_time = time.time()
    m, b = best_fit(X, Y)
    print("Time taken:", time.time() - start_time)

# Plot the data and the best fit line
plt.scatter(X, Y, s=0.1, color='blue')
plt.plot(X, m*X + b, color='red')
plt.show()
