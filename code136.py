import sys
input = sys.stdin.readline

t = int(input())

targets = ["00", "25", "50", "75"]

for _ in range(t):
    s = input().strip()
    n = len(s)
    ans = float('inf')

    for t2 in targets:
        pos2 = -1
        # find second digit of target from right
        for i in range(n - 1, -1, -1):
            if s[i] == t2[1]:
                pos2 = i
                break
        if pos2 == -1:
            continue

        # find first digit of target before pos2
        for i in range(pos2 - 1, -1, -1):
            if s[i] == t2[0]:
                # deletions = digits after pos2 + digits between i and pos2
                deletions = (n - pos2 - 1) + (pos2 - i - 1)
                ans = min(ans, deletions)
                break

    print(ans)
#https://codeforces.com/problemset/problem/1593/B