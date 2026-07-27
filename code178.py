t = int(input())

for _ in range(t):
    n, f, a, b = map(int, input().split())
    m = list(map(int, input().split()))

    prev = 0
    battery = f
    possible = True

    for time in m:
        gap = time - prev
        battery -= min(gap * a, b)

        if battery <= 0:
            possible = False
            break

        prev = time

    print("YES" if possible else "NO")
#https://codeforces.com/problemset/problem/1921/C