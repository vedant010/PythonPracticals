def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

grid = [[" " for _ in range(3)] for _ in range(3)]


grid[0][0] = "X"
grid[1][1] = "O"
grid[2][2] = "X"

display_grid(grid)
