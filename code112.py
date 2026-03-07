s = input().strip()
n = len(s)

answer = 0

for i in range(n):
    if s[i] == 'A':
        q_left = s[:i].count('Q')
        q_right = s[i+1:].count('Q')
        answer += q_left * q_right

print(answer)
#https://codeforces.com/problemset/problem/894/A