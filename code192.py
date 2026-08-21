import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, x = map(int, input().split())

    row = (x - 1) % n
    col = (x - 1) // n

    ans = row * m + col + 1
    print(ans)#https://codeforces.com/problemset/problem/1506/A