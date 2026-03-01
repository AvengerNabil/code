import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    # Smallest multiple of k >= n
    m = (n + k - 1) // k  # ceil(n/k)

    # Minimum maximum element
    x = (m * k + n - 1) // n  # ceil(m*k / n)

    print(x)
#https://codeforces.com/problemset/problem/1476/A