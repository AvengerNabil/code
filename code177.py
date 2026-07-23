import math

t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())

    A = (x + k - 1) // k
    B = (y + k - 1) // k

    if A > B:
        print(2 * A - 1)
    else:
        print(2 * B)
#https://codeforces.com/problemset/problem/2009/C