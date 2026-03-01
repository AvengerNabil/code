t = int(input())
for _ in range(t):
    n = int(input())
    size = 2 * n

    for i in range(size):
        row = ""
        for j in range(size):
            if (i // 2 + j // 2) % 2 == 0:
                row += "#"
            else:
                row += "."
        print(row)
#https://codeforces.com/problemset/problem/1950/B