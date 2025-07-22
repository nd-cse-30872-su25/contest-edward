#!/usr/bin/env python3
import sys

def short_path(grid: list, m: int, n: int) -> tuple:
    new_grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
    if m == 1:
        for col in range(1, n+1):
            new_grid[1][col] = new_grid[1][col-1]+ grid[0][col-1]
    else:
        for col in range(1,n+1):
            for row in range(1, m+1):
                if row == 1:
                    new_grid[row][col] = min(new_grid[m][col-1], new_grid[row][col-1], new_grid[row+1][col-1]) + grid[row-1][col-1]
                elif row == m:
                    new_grid[row][col] = min(new_grid[row-1][col-1], new_grid[row][col-1], new_grid[1][col-1]) + grid[row-1][col-1]
                else:
                    new_grid[row][col] = min(new_grid[row-1][col-1], new_grid[row][col-1], new_grid[row+1][col-1]) + grid[row-1][col-1]
    min_val = sys.maxsize
    row_number = 1
    for row in range(1, m+1):
        if new_grid[row][n] < min_val:
            min_val = new_grid[row][n]
            row_number = row


    return (new_grid, row_number, min_val)

def find_path(new_grid: list, grid: list, row: int, col: int)->list:
    res = []
    while col > 0:
        res.append(row)
        if row == 1:
            if new_grid[row][col] - grid[row-1][col-1] == new_grid[row][col-1]:
                row = row
            elif new_grid[row][col] - grid[len(new_grid)-2][col-1] == new_grid[row-1][col-1]:
                row = len(new_grid)-1
            elif new_grid[row][col] - grid[row-1][col-1] == new_grid[row+1][col-1]:
                row+=1
        elif row == len(new_grid)-1:
            if new_grid[row][col] - grid[row-1][col-1] == new_grid[1][col-1]:
                row = 1
            elif new_grid[row][col] - grid[row-1][col-1] == new_grid[row-1][col-1]:
                row -= 1
            elif new_grid[row][col] - grid[row-1][col-1] == new_grid[row][col-1]:
                row = row
        else:
            if new_grid[row][col] - grid[row-1][col-1] == new_grid[row-1][col-1]:
                row -= 1
            elif new_grid[row][col] - grid[row-1][col-1] == new_grid[row][col-1]:
                row = row
            elif new_grid[row][col] - grid[row-1][col-1] == new_grid[row+1][col-1]:
                row += 1
        col -=1
    res.reverse() 
    return res

def main():
    for line in sys.stdin:
        m, n = map(int, line.strip().split())
        grid = []
        count = 0
        while count < m:
            curr_line = list(map(int, sys.stdin.readline().strip().split()))
            grid.append(curr_line)
            count += 1
        new_grid, row_number, min_path = short_path(grid,m,n)
        path = find_path(new_grid, grid, row_number, n)
        path = list(map(str, path))
        print(min_path)
        print(" ".join(path))
if __name__ == "__main__":
    main()
