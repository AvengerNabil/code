t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip().lower()
    pattern = "meow"
    idx = 0
    valid = True
    i = 0
    while i < n:
        if s[i] not in pattern:
            valid = False
            break
        if s[i] != pattern[idx]:
            if idx < 3 and s[i] == pattern[idx+1]:
                idx += 1
                if s[i] != pattern[idx]:
                    valid = False
                    break
            else:
                valid = False
                break
        i += 1
    if idx != 3:
        valid = False
    print("YES" if valid else "NO")
#https://codeforces.com/problemset/problem/1800/A