
# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

# Solution ideas:
# 1. Parse the input file to get the 50 Sudoku grids.
# 2. For each grid, implement a backtracking algorithm to solve it.
# 3. The backtracking algorithm will find an empty cell, try to place a valid number (1-9) in it, and recursively call itself.
# 4. If a number leads to a solution, the recursion will return True. If not, it will backtrack and try the next number.
# 5. After solving each grid, take the first three numbers from the first row, form a 3-digit number, and add it to a total sum.
# 6. Finally, print the total sum.

def solve_sudoku(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False


def valid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col

    return None

def get_puzzles(path):
    puzzles = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 10):
            puzzle = []
            for j in range(1, 10):
                puzzle.append([int(c) for c in lines[i+j].strip()])
            puzzles.append(puzzle)
    return puzzles

def main():
    puzzles = get_puzzles('resources/documents/p096_sudoku.txt')
    total_sum = 0
    for puzzle in puzzles:
        solve_sudoku(puzzle)
        total_sum += puzzle[0][0] * 100 + puzzle[0][1] * 10 + puzzle[0][2]
    print(total_sum)

if __name__ == "__main__":
    main()
