t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    lo = 1
    hi = max(a) + x  # maximum possible height

    while lo < hi:
        mid = (lo + hi + 1) // 2
        water_needed = sum(max(0, mid - ai) for ai in a)

        if water_needed <= x:
            lo = mid
        else:
            hi = mid - 1
    print(lo)
#https://codeforces.com/problemset/problem/1873/E