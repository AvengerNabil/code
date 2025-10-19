t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    total_sum = a + 2 * b
    if total_sum % 2 != 0:
        print("No")
        continue
    if total_sum == 0:
        print("Yes")
        continue
    half_sum = total_sum // 2
    if half_sum <= 2 * b:
        print("Yes")
    else:
        needed_ones = half_sum - 2 * b
        if needed_ones <= a:
            print("Yes")
        else:
            print("No")
#https://codeforces.com/problemset/problem/2008/A