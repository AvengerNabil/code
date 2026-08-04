import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    current_sum = arr[0]
    answer = arr[0]

    for i in range(1, n):
        # Check if parity alternates
        if (arr[i] % 2) != (arr[i - 1] % 2):
            current_sum = max(arr[i], current_sum + arr[i])
        else:
            current_sum = arr[i]

        answer = max(answer, current_sum)

    print(answer)
#https://codeforces.com/problemset/problem/1899/C