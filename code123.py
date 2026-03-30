t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ok = True

    for i in range(1, n - 1):
        x = a[i - 1]
        a[i - 1] -= x  # becomes zero
        a[i] -= 2 * x
        a[i + 1] -= x

        if a[i] < 0 or a[i + 1] < 0:
            ok = False
            break

    if ok and a[n - 2] == 0 and a[n - 1] == 0:
        print("YES")
    else:
        print("NO")
#https://codeforces.com/problemset/problem/1941/B