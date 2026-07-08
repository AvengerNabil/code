t = int(input().strip())

for _ in range(t):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)

    if total > s:
        print("NO")
    elif x == 0:
        print("YES" if total == s else "NO")
    else:
        print("YES" if (s - total) % x == 0 else "NO")
#https://codeforces.com/problemset/problem/2193/A