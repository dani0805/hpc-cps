from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# The total length of the array
N = 100

# This process's segment of the array
segment_size = N // size
if rank < N % size:
    segment_size += 1
segment = np.random.rand(segment_size)
if rank <= 1:
    print(f"Rank {rank}: {segment}")
# Create new empty array to hold the result
new_segment = np.empty_like(segment)

# Get the rank of the left and right neighbors
left_rank = (rank - 1) if rank > 0 else MPI.PROC_NULL
right_rank = (rank + 1) if rank < size - 1 else MPI.PROC_NULL

# Send and receive boundary data with neighbors
send_data = segment[0]
recv_data = np.empty(1)
comm.Sendrecv(send_data, dest=right_rank, recvbuf=recv_data, source=left_rank)
left_boundary = recv_data[0]

send_data = segment[-1]
recv_data = np.empty(1)
comm.Sendrecv(send_data, dest=left_rank, recvbuf=recv_data, source=right_rank)
right_boundary = recv_data[0]

# Perform the averaging
new_segment[0] = (left_boundary + segment[0] + segment[1]) / 3
new_segment[1:-1] = (segment[:-2] + segment[1:-1] + segment[2:]) / 3
new_segment[-1] = (segment[-2] + segment[-1] + right_boundary) / 3
if rank == 0:
    print(f"Average on Rank {rank}: {new_segment}")
#print(f"Rank {rank}: {new_segment}")
