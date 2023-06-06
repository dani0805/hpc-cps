"""
In this code, a producer process creates a large NumPy array and shares it across multiple worker processes using
shared memory. Each worker process then works on a portion of the array, computing the square of each element.
After all worker processes complete their tasks, the producer checks the results and ensures the data has been
correctly processed. The time it takes from when the workers start until they finish is also measured and printed.
Note that in this scenario, locks are not needed because each worker is working on a separate part of the array.


"""

import numpy as np
from multiprocessing import Pool, Manager, shared_memory
import time

num_workers = 8
w = 40000
h = 10000


def worker(args):
    start_time = time.time()
    i, shm_name = args
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    np_array = np.ndarray((w, h), dtype=np.float64, buffer=existing_shm.buf)
    for idx in range(i, np_array.shape[0], num_workers):
        np_array[idx] = np.square(np_array[idx])
    existing_shm.close()
    end_time = time.time()
    print(f"worker {i} elapsed: {end_time-start_time}")


if __name__ == '__main__':
    np_array = np.random.rand(w, h)
    shm = shared_memory.SharedMemory(create=True, size=np_array.nbytes)
    np_array_shared = np.ndarray(np_array.shape, dtype=np.float64, buffer=shm.buf)
    np_array_shared[:] = np_array[:]


    with Manager() as manager, Pool(processes=num_workers) as pool:
        shm_name = manager.Value('s', shm.name)
        start_time = time.time()
        pool.map(worker, [(i, shm_name.value) for i in range(num_workers)])
        end_time = time.time()
        print("Elapsed time: ", end_time - start_time)

    existing_shm = shared_memory.SharedMemory(name=shm.name)
    np_array_result = np.ndarray(np_array.shape, dtype=np.float64, buffer=existing_shm.buf)

    assert np.allclose(np_array_result, np.square(np_array)), "Arrays are not equal"

    existing_shm.close()

