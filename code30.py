t = int(input())
for _ in range(t):
    m = int(input())
    length = len(str(m))
    round_number = 10 ** (length - 1)
    print(m - round_number)
#https://codeforces.com/problemset/problem/1702/A