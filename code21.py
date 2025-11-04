t = int(input())
for _ in range(t):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    fav_val = a[f-1]

    sorted_a = sorted(a, reverse=True)
    removed = sorted_a[:k]

    if fav_val > removed[-1]:
        print("YES")
    elif fav_val < removed[-1]:
        print("NO")
    else:
        # fav_val == removed[-1]
        if fav_val in removed and fav_val in sorted_a[k:]:
            print("MAYBE")
        elif fav_val in removed:
            print("YES")
        else:
            print("NO")
#https://codeforces.com/problemset/problem/1980/B