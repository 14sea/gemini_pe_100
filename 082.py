"""
Project Euler Problem 82: Path sum: three ways

Problem:
Find the minimal path sum from any cell in the left column to any cell in the right column of an 80x80 matrix (in matrix.txt), by only moving up, down, and right.

Solution Idea:
This is a variation of the shortest path problem on a grid. Unlike Problem 81, we can move up and down within a column before moving right. This makes a simple left-to-right DP propagation insufficient.

The key insight is to solve the problem column by column. For each cell in a given column `j`, we want to find the minimum path sum to reach it from the left column.

1.  **Dynamic Programming State**: Let `min_sums[i]` be the minimum path sum to reach the cell `(i, j)` from the left column. We will calculate this for each column `j` from left to right.

2.  **Column-by-Column Calculation**:
    - We start with the first column (`j=0`). The `min_sums` for this column are just the values of the cells themselves, as this is our starting point.
    - Now, to calculate the `min_sums` for the next column `j+1`, we consider that to reach any cell `(i, j+1)`, we must have come from a cell in column `j`.
    - For a given cell `(i, j+1)`, the path could have come from `(i, j)` directly to the right. Or, it could have come from another cell `(k, j)` and then moved up or down within column `j` to `(i, j)` before moving right.

3.  **Algorithm**:
    a.  Read the matrix from the file.
    b.  Initialize a `min_path_sums` array with the values of the first column of the matrix. This represents the minimum cost to reach each cell in the first column.
    c.  Loop through the columns `j` from 1 to the end of the matrix.
        i.   For each column `j`, we need to calculate the new `min_path_sums` for this column.
        ii.  First, consider the path coming directly from the left. The initial guess for the minimum path to `(i, j)` is `min_path_sums[i] + matrix[i][j]`. Let's call this `new_sums[i]`.
        iii. Now, we must account for moving up and down within column `j`.
             - **Downward pass**: Iterate `i` from 1 to the bottom row. A shorter path to `(i, j)` might exist by coming from the cell above it, `(i-1, j)`. So, we update: `new_sums[i] = min(new_sums[i], new_sums[i-1] + matrix[i][j])`.
             - **Upward pass**: Iterate `i` from the second-to-last row up to the top. A shorter path might exist by coming from the cell below. Update: `new_sums[i] = min(new_sums[i], new_sums[i+1] + matrix[i][j])`.
        iv.  After these two passes, `new_sums` will contain the true minimum path sums to reach each cell in column `j`. Update `min_path_sums = new_sums`.
    d.  After iterating through all the columns, the `min_path_sums` array will hold the minimum path sums to reach each cell in the final column. The answer is the minimum value in this final array.
"""

def solve():
    """
    Finds the minimal path sum from the left column to the right column.
    """
    try:
        with open('resources/documents/0082_matrix.txt', 'r') as f:
            matrix = [[int(n) for n in line.strip().split(',')] for line in f]
    except FileNotFoundError:
        return "Error: matrix.txt not found. Please ensure it's in 'resources/documents/'."

    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize min_path_sums with the first column
    min_path_sums = [matrix[i][0] for i in range(rows)]

    # Iterate through the remaining columns
    for j in range(1, cols):
        # Path coming directly from the left
        temp_sums = [min_path_sums[i] + matrix[i][j] for i in range(rows)]
        
        # Downward pass: check for paths coming from above
        for i in range(1, rows):
            temp_sums[i] = min(temp_sums[i], temp_sums[i-1] + matrix[i][j])
            
        # Upward pass: check for paths coming from below
        for i in range(rows - 2, -1, -1):
            temp_sums[i] = min(temp_sums[i], temp_sums[i+1] + matrix[i][j])
            
        min_path_sums = temp_sums

    # The result is the minimum of the final column's path sums
    return min(min_path_sums)

if __name__ == "__main__":
    print(solve())
