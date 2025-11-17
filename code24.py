def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

n = int(input())
primes = sieve(n)
count = 0

for x in range(1, n + 1):
    divs = 0
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            divs += 1
            while x % p == 0:
                x //= p
    if x > 1:
        divs += 1
    if divs == 2:
        count += 1

print(count)
#https://codeforces.com/problemset/problem/26/A