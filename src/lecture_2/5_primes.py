
def primes(n):
    if n < 2:
        return []
    elif n == 2:
        return [2]
    else:
        ps = primes(n - 1)
        for p in ps:
            if n % p == 0:
                return ps
        return ps + [n]


print(primes(500))
