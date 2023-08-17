from mpi4py import MPI
import numpy as np


def mpi_leader_election():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Generate a random number in each process
    num = np.array([np.random.randint(100)])
    print(f"Process {rank} generated {num[0]}")

    # Initialize an array to gather all the numbers
    gather_nums = None
    if rank == 0:
        gather_nums = np.empty([size], dtype=int)

    # Gather all numbers to process 0
    comm.Gather(num, gather_nums, root=0)

    # Process 0 elects the leader and broadcasts the result
    leader = 0
    if rank == 0:
        leader = np.argmax(gather_nums)
        print(f"Process {leader} is the leader with the highest number {gather_nums[leader]}")

    # Broadcast leader's rank
    leader = comm.bcast(leader, root=0)

    return leader


if __name__ == "__main__":
    mpi_leader_election()
