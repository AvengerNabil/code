t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    a = max(1, n - k + 1)
    b = n

    total_leaves = (a + b) * (b - a + 1) // 2

    if total_leaves % 2 == 0:
        print("YES")
    else:
        print("NO")
#https://codeforces.com/problemset/problem/2014/B