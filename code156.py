# 1. Palindrome Game (easy version) — Correct Python Solution

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    zeros = s.count('0')

    # Special case: only one zero
    if zeros == 1:
        print("BOB")
    else:
        # If length is odd and the middle character is '0'
        if n % 2 == 1 and s[n // 2] == '0':
            print("ALICE")
        else:
            print("BOB")
#https://codeforces.com/problemset/problem/1527/B1