# B. The Cake Is a Lie — Correct Python Solution

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())

    # Minimum cost path:
    # Move right (m-1) times with cost 1..1 = (m-1)*1
    # Move down (n-1) times with cost m each time = (n-1)*m
    min_cost = (m - 1) + (n - 1) * m

    # Maximum cost path:
    # Move down (n-1) times with cost 1..1 = (n-1)*1
    # Move right (m-1) times with cost n each time = (m-1)*n
    max_cost = (n - 1) + (m - 1) * n

    if min_cost <= k <= max_cost and (k - min_cost) % 2 == 0:
        print("YES")
    else:
        print("NO")
#https://codeforces.com/problemset/problem/1519/B