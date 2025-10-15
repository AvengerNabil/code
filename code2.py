import math


def solve(n):
    factors = []

    # Try to find first factor a
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            n //= i
            break

    # Try to find second factor b (≠ a)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i != factors[0]:
            factors.append(i)
            n //= i
            break

    # Now c = n (remaining part)
    if len(factors) < 2 or n in factors or n < 2:
        print("NO")
    else:
        print("YES")
        print(factors[0], factors[1], n)


t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)
    #https://codeforces.com/problemset/problem/1294/Cfff