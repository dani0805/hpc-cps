import threading
import queue
# A thread-safe queue
q = queue.Queue()
def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")
def consumer():
    while True:
        try:
            item = q.get(block=False)
        except queue.Empty:
            break
        print(f"Consumed: {item}")
# Creating threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
# Start threads
t1.start()
t2.start()
# Wait for both threads to finish
t1.join()
t2.join()