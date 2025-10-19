t = int(input())
for _ in range(t):
    keyboard = input()
    s = input()
    pos = {ch: i for i, ch in enumerate(keyboard)}
    time = 0
    for i in range(len(s) - 1):
        time += abs(pos[s[i]] - pos[s[i+1]])
    print(time)
#https://codeforces.com/problemset/problem/1607/A