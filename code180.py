import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(n * (m // 2))
#https://codeforces.com/problemset/problem/1918/A