# Lights Out (Codeforces 275A)

# Input 3x3 grid of presses
presses = [list(map(int, input().split())) for _ in range(3)]

# Initialize all lights as ON (1)
grid = [[1 for _ in range(3)] for _ in range(3)]

# Compute final light states
for i in range(3):
    for j in range(3):
        total_presses = presses[i][j]
        if i > 0:
            total_presses += presses[i - 1][j]  # up
        if i < 2:
            total_presses += presses[i + 1][j]  # down
        if j > 0:
            total_presses += presses[i][j - 1]  # left
        if j < 2:
            total_presses += presses[i][j + 1]  # right

        # Toggle based on total_presses % 2
        if total_presses % 2 != 0:
            grid[i][j] = 0  # toggle off

# Print the final grid
for row in grid:
    print(''.join(map(str, row)))
#https://codeforces.com/problemset/problem/275/A