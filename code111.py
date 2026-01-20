t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0

    # Days 1 to n-1
    for i in range(n - 1):
        ans += max(0, a[i] - b[i + 1])

    # Last day
    ans += a[n - 1]

    print(ans)
#https://codeforces.com/problemset/problem/2051/A