# A. Two Frogs — Correct Python Solution

t = int(input().strip())

for _ in range(t):
    n, a, b = map(int, input().split())

    # Alice wins iff the distance between frogs is even
    if abs(a - b) % 2 == 0:
        print("YES")
    else:
        print("NO")
#https://codeforces.com/problemset/problem/2055/A