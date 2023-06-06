"""
In this experiment, worker_noop is a simple function that does nothing. It is used to evaluate the overhead of
creating threads/processes and performing the context switch. The run_threads and run_processes functions create
the specified number of threads/processes and wait for them to complete. The measure_time function is a helper
function to measure the time taken by a function call.

The main section of the script sets up a shared counter using multiprocessing.Value and then measures the time taken
to increment the counter using each of the methods. The measurements are repeated 50 times to get a more
accurate average time. The results are printed to the console.

"""

import time
import threading
import multiprocessing as mp



NUM_WORKERS = 10
INCREMENT_TIMES = 1000000

def worker_noop():
    pass

def measure_time(func, args, repetitions=1):
    start_time = time.time()
    for _ in range(repetitions):
        func(*args)
    end_time = time.time()
    return end_time - start_time

def run_threads(target, args):
    threads = [threading.Thread(target=target, args=args) for _ in range(NUM_WORKERS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def run_processes(target, args):
    processes = [mp.Process(target=target, args=args) for _ in range(NUM_WORKERS)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

def run_experiment(method):
    print(f'Measuring overhead for {method}...')
    if method == 'threads':
        overhead_time = measure_time(run_threads, (worker_noop, ()), repetitions=50)
    else:
        overhead_time = measure_time(run_processes, (worker_noop, ()), repetitions=50)
    print(f'{method.capitalize()} overhead: {overhead_time:.4f}s')

if __name__ == '__main__':
    # Set the start method: 'fork', 'spawn', or 'forkserver'
    mp.set_start_method('spawn')
    methods = ['threads', 'processes']
    for method in methods:
        run_experiment(method)
