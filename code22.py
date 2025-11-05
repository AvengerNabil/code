t = int(input())
for _ in range(t):
    s = input().strip()
    year = int(s)
    root = int(year ** 0.5)
    if root * root != year:
        print(-1)
    else:
        found = False
        for a in range(root + 1):
            b = root - a
            if (a + b) ** 2 == year:
                print(a, b)
                found = True
                break
        if not found:
            print(-1)
#https://codeforces.com/problemset/problem/2114/A