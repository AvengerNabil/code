t = int(input())
for _ in range(t):
    n = int(input())
    nails = [tuple(map(int, input().split())) for _ in range(n)]

    # Sort by height
    nails.sort()

    # Compute (a - b) values
    vals = [a - b for a, b in nails]
    vals.sort(reverse=True)  # Start removing from biggest a-b

    cuts = 0
    while vals and vals[0] > 0:
        vals.pop(0)
        cuts += 1

    print(cuts)
#https://codeforces.com/problemset/problem/1846/A