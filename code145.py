# A. DZY Loves Chessboard — Correct Python Solution

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

for i in range(n):
    row = []
    for j in range(m):
        if grid[i][j] == '-':
            row.append('-')
        else:
            # Chessboard coloring
            if (i + j) % 2 == 0:
                row.append('B')
            else:
                row.append('W')
    print(''.join(row))
#https://codeforces.com/problemset/problem/445/A