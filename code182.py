import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print(0)
        continue

    big = max(a, b)
    small = min(a, b)

    # Must be divisible
    if big % small != 0:
        print(-1)
        continue

    ratio = big // small

    # Check if power of 2
    if ratio & (ratio - 1) != 0:
        print(-1)
        continue

    # Count exponent of 2
    k = 0
    while ratio > 1:
        ratio //= 2
        k += 1

    # Minimum operations using 8, 4, 2
    operations = k // 3
    k %= 3
    operations += k // 2
    k %= 2
    operations += k

    print(operations)
#https://codeforces.com/problemset/problem/1362/A