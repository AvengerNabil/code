t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    max1 = -1
    max2 = -1
    count_max1 = 0

    # find max1, max2, count of max1 in one pass
    for x in s:
        if x > max1:
            max2 = max1
            max1 = x
            count_max1 = 1
        elif x == max1:
            count_max1 += 1
        elif x > max2:
            max2 = x

    res = []
    for x in s:
        if x == max1 and count_max1 == 1:
            res.append(x - max2)
        else:
            res.append(x - max1)
    print(*res)
#https://codeforces.com/problemset/problem/1760/C