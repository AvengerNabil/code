import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    found = False

    for i in range(1, n - 1):
        if s[i] in (s[:i] + s[i + 1:]):
            found = True
            break

    if found:
        print("Yes")
    else:
        print("No")#https://codeforces.com/problemset/problem/2121/B