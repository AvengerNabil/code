import sys

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    import math
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            for j in range(start, limit + 1, step):
                is_prime[j] = False
    return is_prime

LIMIT = 200000
is_prime = sieve(LIMIT)

input_data = sys.stdin.read().strip().split()
t = int(input_data[0])
res = []
idx = 1
for _ in range(t):
    d = int(input_data[idx]); idx += 1

    # find smallest prime p >= d+1
    p = d + 1
    while p <= LIMIT and not is_prime[p]:
        p += 1

    # find smallest prime q >= p + d
    q = p + d
    while q <= LIMIT and not is_prime[q]:
        q += 1

    res.append(str(p * q))

print("\n".join(res))
#https://codeforces.com/problemset/problem/1474/B