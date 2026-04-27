# C. Minimum Varied Number — Correct Python Solution

t = int(input().strip())

for _ in range(t):
    s = int(input().strip())

    digits = []
    cur = 9

    while s > 0 and cur > 0:
        if s >= cur:
            digits.append(cur)
            s -= cur
        cur -= 1

    # digits were taken from largest to smallest,
    # reverse to form the minimum number
    digits.reverse()

    print(''.join(map(str, digits)))
#https://codeforces.com/problemset/problem/1714/C