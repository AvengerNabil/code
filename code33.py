import sys
data=list(map(int,sys.stdin.read().split()))
t=data[0]; idx=1
out=[]
for _ in range(t):
    n=data[idx]; idx+=1
    s=str(n)
    out.append(str(9*(len(s)-1)+int(s[0])))
print("\n".join(out))
#https://codeforces.com/problemset/problem/1766/A