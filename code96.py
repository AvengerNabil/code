import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
    else:
        print(sum(a) - (n - 1))
#https://codeforces.com/problemset/problem/2074/B