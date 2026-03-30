n = int(input())

# Top half + middle
for i in range(n + 1):
    spaces = ' ' * (2 * (n - i))
    inc = list(range(i + 1))
    dec = list(range(i - 1, -1, -1))
    nums = inc + dec
    print(spaces + ' '.join(map(str, nums)))

# Bottom half
for i in range(n - 1, -1, -1):
    spaces = ' ' * (2 * (n - i))
    inc = list(range(i + 1))
    dec = list(range(i - 1, -1, -1))
    nums = inc + dec
    print(spaces + ' '.join(map(str, nums)))
#https://codeforces.com/problemset/problem/118/B