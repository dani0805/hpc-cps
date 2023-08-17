from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Generate some data on the root process
if rank == 0:
    data = np.arange(size, dtype='i')
else:
    data = None

# Scatter the data across the processes
data = comm.scatter(data, root=0)

# Each process computes the sum of its portion of the data
local_sum = np.sum(data)

print(f"Process {rank} has the sum {local_sum}")
# Now we perform the reduction. We assume that the processes are arranged in a binary tree.
# At each step, a process sends its result to its parent in the tree.
tree_depth = int(np.log2(size))
for i in range(tree_depth):
    print(f"Tree Depth {i}")
    if (rank % (2**(i+1))) == 0:
        # We're at the node which should receive from its children and sum up the results
        if rank + 2**i < size:
            print(f"Process {rank} waiting")
            temp_sum = comm.recv(source=rank + 2**i)
            print(f"Process {rank} received {temp_sum}")
            local_sum += temp_sum

    elif (rank % 2**i) == 0:
        # We're at the node which should send the results to the parent
        comm.send(local_sum, dest=rank - 2**i)
        print(f"Process {rank} sent {local_sum}")

if rank == 0:
    print("The total sum is ", local_sum)
