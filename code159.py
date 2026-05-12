t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    ok = False
    for _ in range(4):
        if a < b and c < d and a < c and b < d:
            ok = True
            break
        # rotate clockwise
        a, b, c, d = c, a, d, b

    print("YES" if ok else "NO")
#https://codeforces.com/problemset/problem/1772/B