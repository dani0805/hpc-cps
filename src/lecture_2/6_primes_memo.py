from collections import deque
from math import sqrt


def is_prime(n, memo):
    if n < 2:
        return False
    if n in memo:
        return memo[n]

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            memo[n] = False
            return False
    memo[n] = True
    return True


def bfs_prime_numbers(n):
    memo = {}
    primes = []
    queue = deque([2])

    while len(primes) < n:
        number = queue.popleft()

        if is_prime(number, memo):
            primes.append(number)

        queue.append(number + 1)

    return primes


n = 1000  # Number of prime numbers to find
print(bfs_prime_numbers(n))
