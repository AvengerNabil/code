import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    if n == 1:
        print(-1)
    else:
        print("2" + "3" * (n - 1))
#https://codeforces.com/problemset/problem/1326/A