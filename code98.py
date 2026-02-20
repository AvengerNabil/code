def can_return_to_zero(n, angles):
    def dfs(index, current_sum):
        if index == n:
            return current_sum % 360 == 0
        # Try clockwise
        if dfs(index + 1, current_sum + angles[index]):
            return True
        # Try counterclockwise
        if dfs(index + 1, current_sum - angles[index]):
            return True
        return False

    return dfs(0, 0)

# Read input
n = int(input())
angles = [int(input()) for _ in range(n)]

if can_return_to_zero(n, angles):
    print("YES")
else:
    print("NO")
#https://codeforces.com/problemset/problem/1097/B