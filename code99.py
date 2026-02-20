t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # Get top 3 values and their indices for each activity
    a_top = sorted([(val, idx) for idx, val in enumerate(a)], reverse=True)[:3]
    b_top = sorted([(val, idx) for idx, val in enumerate(b)], reverse=True)[:3]
    c_top = sorted([(val, idx) for idx, val in enumerate(c)], reverse=True)[:3]

    max_total = 0

    for aval, ai in a_top:
        for bval, bi in b_top:
            if bi == ai:
                continue
            for cval, ci in c_top:
                if ci == ai or ci == bi:
                    continue
                max_total = max(max_total, aval + bval + cval)

    print(max_total)
#https://codeforces.com/problemset/problem/1914/D