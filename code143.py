# B. AND 0, Sum Big — Correct Python Solution

MOD = 10**9 + 7

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    print(pow(n, k, MOD))
#https://codeforces.com/problemset/problem/1514/B