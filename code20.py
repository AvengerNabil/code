t = int(input())
for _ in range(t):
    n = int(input())
    layers = (n - 1) // 2
    ans = 0
    for k in range(1, layers + 1):
        ans += 8 * k * k
    print(ans)
#https://codeforces.com/problemset/problem/1353/C