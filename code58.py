n = int(input())
t = input().strip()
res = []
i = 0
cnt = 1
while i < n:
    res.append(t[i])
    i += cnt
    cnt += 1
print("".join(res))
#https://codeforces.com/problemset/problem/1095/A