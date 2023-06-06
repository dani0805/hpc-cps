import numpy as np
from multiprocessing import Process, Array, Condition
from time import sleep


def write_data(arr, condition):
    arr_np = np.frombuffer(arr.get_obj())  # No copy, writes to original array
    for _ in range(2):
        with condition:
            arr_np += 1  # Increment all elements by 1
            condition.notify_all()  # Notify that the data has been updated
        sleep(1)  # Wait 1 second before next increment


def read_data(arr, condition):
    arr_np = np.frombuffer(arr.get_obj())
    last_data = arr_np.copy()
    with condition:
        while True:
            condition.wait()  # Wait for a notification that the data has been updated
            if not np.array_equal(last_data, arr_np):
                print('Data changed:', arr_np)
                last_data = arr_np.copy()


if __name__ == '__main__':
    data = np.array([1, 2, 3, 4, 5])
    arr = Array('d', data)
    condition = Condition()

    p1 = Process(target=write_data, args=(arr, condition))
    p2 = Process(target=read_data, args=(arr, condition))
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()