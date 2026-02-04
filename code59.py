import math

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    length = int((-1 + math.isqrt(1 + 8 * (r - l))) // 2) + 1
    print(length)
#https://codeforces.com/problemset/problem/2008/C