# Read input values
n, m = map(int, input().split())

# If m is not divisible by n, it's impossible
if m % n != 0:
    print(-1)
else:
    ratio = m // n
    moves = 0

    # Count how many times 2 divides the ratio
    while ratio % 2 == 0:
        ratio //= 2
        moves += 1

    # Count how many times 3 divides the ratio
    while ratio % 3 == 0:
        ratio //= 3
        moves += 1

    # If ratio becomes 1, it's possible; otherwise impossible
    if ratio == 1:
        print(moves)
    else:
        print(-1)
#https://codeforces.com/problemset/problem/1141/A