t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(2)
    else:
        moves = (n + 2) // 3
        if (n % 3) == 1 and n != 1:
            moves += 0
        print(moves)
#https://codeforces.com/problemset/problem/1716/A