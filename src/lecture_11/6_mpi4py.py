from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Create an array of numbers on each process
data = np.array([rank]*10, dtype='i')

# Create a container to hold the sum of the arrays of all processes
sum = np.zeros(10, dtype='i')

# Use MPI to get the sum of the arrays of all processes
comm.Reduce(data, sum, op=MPI.SUM, root=0)

# Only print the result in process 0
if rank == 0:
    print(sum)
