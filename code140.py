# B. Remove Prefix — Correct Python Solution

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    seen = set()
    ans = n  # default: remove all

    # traverse from right to left
    for i in range(n - 1, -1, -1):
        if a[i] in seen:
            ans = i + 1
            break
        seen.add(a[i])
    else:
        ans = 0

    print(ans)
#https://codeforces.com/problemset/problem/1714/B