t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    s = input()
    d = str(d)
    i = 0
    while i < n and s[i] >= d:
        i += 1
    print(s[:i] + d + s[i:])
#https://codeforces.com/problemset/problem/1811/A