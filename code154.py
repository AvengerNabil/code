t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    p = [-1] * n
    i = 0
    ok = True

    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1

        # group size
        cnt = j - i

        if cnt == 1:
            ok = False
            break

        # rotate inside the group
        for k in range(i, j):
            if k + 1 < j:
                p[k] = k + 2
            else:
                p[k] = i + 1

        i = j

    if not ok:
        print(-1)
    else:
        print(*p)
#https://codeforces.com/problemset/problem/1691/B