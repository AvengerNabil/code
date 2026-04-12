# A. Make Even — Correct Python Solution

t = int(input().strip())

for _ in range(t):
    s = input().strip()

    # Case 0: already even
    if int(s[-1]) % 2 == 0:
        print(0)
        continue

    # Check if there is any even digit
    pos = -1
    for i, ch in enumerate(s):
        if int(ch) % 2 == 0:
            pos = i
            break

    # No even digit → impossible
    if pos == -1:
        print(-1)
    else:
        # If even digit is at first position
        if pos == 0:
            print(1)
        else:
            print(2)
#https://codeforces.com/problemset/problem/1611/A