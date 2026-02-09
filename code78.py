t = int(input())
for _ in range(t):
    n = int(input())
    log = input().strip()

    # Count time spent on each problem
    time_spent = [0] * 26  # 'A' to 'Z'
    for ch in log:
        time_spent[ord(ch) - ord('A')] += 1

    # Count problems solved
    solved = 0
    for i in range(26):
        if time_spent[i] >= i + 1:
            solved += 1

    print(solved)
#https://codeforces.com/problemset/problem/1914/A