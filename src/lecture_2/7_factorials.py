def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

#factorial = memoize(factorial)

numbers = [5, 3, 7, 4, 6, 8, 5, 9, 10]

factorial(3)

# Using map to apply factorial function to the list of numbers
factorials = list(map(factorial, numbers))

print(factorials)
