# D. Pair of Topics — Correct Python Solution

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Compute differences
d = [a[i] - b[i] for i in range(n)]
d.sort()

ans = 0
l = 0
r = n - 1

# Two-pointer technique
while l < r:
    if d[l] + d[r] > 0:
        ans += (r - l)
        r -= 1
    else:
        l += 1

print(ans)
#https://codeforces.com/problemset/problem/1324/D