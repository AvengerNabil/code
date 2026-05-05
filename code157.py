import math

t = int(input())
for _ in range(t):
    n = int(input())

    squares = int(math.isqrt(n))
    cubes = int(n ** (1/3))
    sixth_powers = int(n ** (1/6))

    # Fix floating point inaccuracies
    while (cubes + 1) ** 3 <= n:
        cubes += 1
    while cubes ** 3 > n:
        cubes -= 1

    while (sixth_powers + 1) ** 6 <= n:
        sixth_powers += 1
    while sixth_powers ** 6 > n:
        sixth_powers -= 1

    print(squares + cubes - sixth_powers)
#https://codeforces.com/problemset/problem/1619/B