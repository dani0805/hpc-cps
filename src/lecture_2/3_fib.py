
def fib(n):
    # print(n)
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fib(n - 1) + fib(n - 2)

    return result

n = 100
print(f"fib({n}) = {fib(n)}")
