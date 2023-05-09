import time
import numpy as np
from math import sin, log

numbers = list(range(10000000))
# numbers = [float(x) for x in range(10000000)]
f = lambda x: log(1 - sin(x)/(x+1)**2)

start_time = time.time()

squares = []
for number in numbers:
    squares.append(f(number))
#print(squares[100:110])
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken for loop: {elapsed_time:.2f} seconds")

# numbers = [float(x) for x in range(10000000)]
start_time = time.time()

squares = list(f(x) for x in numbers)
#print(squares[100:110])
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken for list generator: {elapsed_time:.2f} seconds")

#numbers = [float(x) for x in range(10000000)]
start_time = time.time()

squares = [f(x) for x in numbers]
#print(squares[100:110])
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken for list comprehension: {elapsed_time:.2f} seconds")

#numbers = [float(x) for x in range(10000000)]
start_time = time.time()

squares = list(map(lambda x: f(x), numbers))
#print(squares[100:110])
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken for map: {elapsed_time:.2f} seconds")

numbers = np.arange(10000000)

start_time = time.time()

squares = np.log( 1 -  np.sin(numbers)/(numbers + 1)**2)

#print(squares[100:110])

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken for numpy: {elapsed_time:.2f} seconds")