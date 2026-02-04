n = input().strip()
# For very large n, just treat it as string and build palindrome
half = str(n)
palindrome = half + half[::-1]
print(palindrome)
#https://codeforces.com/problemset/problem/688/B