t = int(input())

for _ in range(t):
    n = int(input())
    k = n // 2
    ans = 8 * (k * (k + 1) * (2 * k + 1) // 6)
    print(ans)
#https://codeforces.com/problemset/problem/1353/C