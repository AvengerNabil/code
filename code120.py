t = int(input())

for _ in range(t):
    input()  # empty line before each test case
    board = [input().strip() for _ in range(8)]

    for i in range(1, 7):
        for j in range(1, 7):
            if (board[i][j] == '#' and
                    board[i - 1][j - 1] == '#' and
                    board[i - 1][j + 1] == '#' and
                    board[i + 1][j - 1] == '#' and
                    board[i + 1][j + 1] == '#'):
                print(i + 1, j + 1)
                break
        else:
            continue
        break
#https://codeforces.com/problemset/problem/1692/C