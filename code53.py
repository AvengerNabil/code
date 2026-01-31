t = int(input())
for _ in range(t):
    n = int(input())
    h2 = n // 3
    h1 = h2 + 1
    h3 = n - h1 - h2
    print(h2, h1, h3)
#https://codeforces.com/problemset/problem/1690/A