"""

In Python, the Condition.wait() method implicitly releases the associated lock. It does this to allow other threads
to enter the block guarded by the Condition object. When Condition.wait() is called, the thread will block and will
not continue until another thread calls Condition.notify() or Condition.notify_all().

So, when the consumer thread enters the with condition: block, it indeed acquires the lock. But when it calls
condition.wait(), it releases the lock and goes to sleep, allowing the producer thread to acquire the lock and proceed.

Once the producer has finished its work and calls condition.notify(), this wakes up the consumer thread. Before the
consumer thread proceeds, it reacquires the lock. Hence, despite the lock being released during the wait,
the synchronization is still maintained.

This is the fundamental feature of a condition variable -- allowing one thread to sleep and release the lock while
waiting for a certain condition to be met, and then reacquire the lock when it wakes up. This way, we can avoid
deadlock and also unnecessary busy waiting.

"""

import threading
import time

# Shared condition variable
condition = threading.Condition()
item = None

def consumer():
    global item
    with condition:
        print("Waiting for item to be produced")
        while item is None:
            condition.wait()
        print(f"Consumed: {item}")
        item = None

def producer():
    global item
    # wait 1 second before producing the item, so the consumer thread will block
    time.sleep(1)
    with condition:
        item = "Hello"
        print("Produced: Hello")
        condition.notify()

# Creating threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()