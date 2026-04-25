# A. Strong Password — Correct Python Solution

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    best_time = -1
    best_string = ""

    # try inserting every letter at every position
    for i in range(len(s) + 1):
        for c in "abcdefghijklmnopqrstuvwxyz":
            new_s = s[:i] + c + s[i:]

            # calculate typing time
            time = 2
            for j in range(1, len(new_s)):
                if new_s[j] == new_s[j - 1]:
                    time += 1
                else:
                    time += 2

            if time > best_time:
                best_time = time
                best_string = new_s

    print(best_string)
#https://codeforces.com/problemset/problem/1997/A