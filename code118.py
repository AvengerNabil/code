from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    b.sort()
    cnt = Counter(b)

    a = []
    remaining = n

    for value in b:
        if cnt[value] == 0:
            continue

        a.append(value)
        cnt[value] -= remaining - 1
        remaining -= 1

        if remaining == 1:
            break

    # Last element (never appears as a minimum)
    a.append(a[-1])

    print(*a)
#https://codeforces.com/problemset/problem/1857/C