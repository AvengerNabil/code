t = int(input())
for _ in range(t):
    x = int(input())
    if x > 45:
        print(-1)
        continue
    digits = []
    for d in range(9, 0, -1):
        if x >= d:
            digits.append(d)
            x -= d
    print("".join(map(str, sorted(digits))))
#https://codeforces.com/problemset/problem/1462/C