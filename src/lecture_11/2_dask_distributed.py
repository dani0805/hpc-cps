"""
To run this example, you will need to install dask distributed on your machine with pip like so:
    pip install dask[distributed]
then start a Dask distributed scheduler from the command line like so:
    dask scheduler
this will start a scheduler on your machine and print the address of the scheduler to the console.
"""
import numpy as np
from dask.distributed import Client


def collatz(n):
    chain = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n in chain:
            chain.append(-1)
            break
        else:
            chain.append(n)
    return chain[-1], len(chain)


client = Client("tcp://localhost:8786")

# Generate collatz inputs with a random number lower than 1e12 and the next 100000 numbers
inputs = np.random.randint(1, int(1e12)) + np.arange(100000)

# Using the Dask client, map the `collatz` function over the inputs
results = client.map(collatz, inputs)

# Gather the results from the workers
output = client.gather(results)

for i, val in zip(inputs, output):
    if val[0] == -1:
        raise RuntimeError(f"Found a cycle. Collatz conjecture is false for {i}")
    else:
        print(f"Collatz Chain for {i} has length {val[1]}")