import math

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    k = int(math.isqrt(n))
    if k * k != n:
        print("No")
        continue

    ok = True
    for i in range(k):
        for j in range(k):
            ch = s[i * k + j]
            if i == 0 or i == k - 1 or j == 0 or j == k - 1:
                if ch != '1':
                    ok = False
            else:
                if ch != '0':
                    ok = False

    print("Yes" if ok else "No")
#https://codeforces.com/problemset/problem/2008/B