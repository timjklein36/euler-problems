from math import ceil


def eratosthenes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, number_is_prime) in enumerate(a):
        if number_is_prime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


def primes_gen(n):
    a = [2]
    i = 3

    while len(a) < n:
        for p in a:
            if i % p == 0:
                break
        else:
            a.append(i)

        i += 2

    return a


def primes(limit):
    return list(eratosthenes_sieve(ceil(limit)))


def is_prime(n):
    return n in primes(n + 1)


def nth_prime(n):
    return primes_gen(n)[n - 1]
