import concurrent.futures
import threading
import time
import random

# Semaphore to limit number of threads executing simultaneously
semaphore = threading.Semaphore(3)

def fetch_data(worker_number):

    with semaphore:
        print(f"Worker {worker_number} has started fetching data.")
        # Simulate the time taken to fetch the data
        time.sleep(random.randint(2, 5))
        print(f"Worker {worker_number} has finished fetching data.")


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Creating a future for each worker
    workers = [executor.submit(fetch_data, i) for i in range(10)]

# No need to gather results as we're not returning anything