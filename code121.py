from collections import Counter

t = int(input())

need = Counter({
    0: 3,
    1: 1,
    2: 2,
    3: 1,
    5: 1
})

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    have = Counter()
    answer = 0

    for i in range(n):
        have[arr[i]] += 1

        ok = True
        for d in need:
            if have[d] < need[d]:
                ok = False
                break

        if ok:
            answer = i + 1  # steps are 1-based
            break

    print(answer)
#https://codeforces.com/problemset/problem/2091/A