import threading

# A shared variable
shared_variable = 0

def increment():
    global shared_variable
    for _ in range(1000000):
        shared_variable += 1

def decrement():
    global shared_variable
    for _ in range(1000000):

        shared_variable -= 1

# Creating threads
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print(f"Final value of shared variable: {shared_variable}")