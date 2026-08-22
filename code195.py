import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    min10 = float('inf')
    min01 = float('inf')
    min11 = float('inf')

    for _ in range(n):
        m, s = input().split()
        m = int(m)

        if s == "10":
            min10 = min(min10, m)
        elif s == "01":
            min01 = min(min01, m)
        elif s == "11":
            min11 = min(min11, m)

    ans = min(min11, min10 + min01)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)#https://codeforces.com/problemset/problem/1829/C