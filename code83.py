import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max(arr) - min(arr))
#https://codeforces.com/problemset/problem/1929/A