"""
Project Euler Problem 81: Path sum: two ways

Problem:
Find the minimal path sum from the top left to the bottom right by only moving right and down in an 80 by 80 matrix contained in the file matrix.txt.

Solution Idea:
This is a classic dynamic programming problem. A brute-force search of all possible paths is computationally infeasible. The efficient approach is to build up a solution by finding the minimal path to each cell in the matrix.

1.  **Dynamic Programming State**: Let `dp[i][j]` be the minimum path sum to reach the cell at row `i` and column `j`. The value of the cell in the original matrix is `matrix[i][j]`.

2.  **Recurrence Relation**: To reach any cell `(i, j)`, you must have come from either the cell directly above it, `(i-1, j)`, or the cell directly to its left, `(i, j-1)`. Therefore, the minimum path sum to reach `(i, j)` is its own value plus the minimum of the path sums of its two possible predecessors.
    `dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])`

3.  **In-Place Calculation**: We can use the matrix itself to store the `dp` values, which saves space. We will modify the matrix such that each cell holds the minimum path sum to reach that cell.

4.  **Algorithm**:
    a.  Read the matrix from the file into a 2D list of integers.
    b.  Handle the base cases:
        - The top row: For each cell `matrix[0][j]` (for `j > 0`), the only way to reach it is from the left. So, `matrix[0][j] += matrix[0][j-1]`.
        - The first column: For each cell `matrix[i][0]` (for `i > 0`), the only way to reach it is from above. So, `matrix[i][0] += matrix[i-1][0]`.
    c.  Iterate through the rest of the matrix, starting from `(1, 1)`. For each cell `matrix[i][j]`, apply the recurrence relation: `matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])`.
    d.  After the loops are complete, the value in the bottom-right cell of the matrix will be the minimal path sum for the entire grid.
"""

def solve():
    """
    Finds the minimal path sum from the top left to the bottom right of the matrix.
    """
    try:
        with open('resources/documents/0081_matrix.txt', 'r') as f:
            matrix = [[int(n) for n in line.strip().split(',')] for line in f]
    except FileNotFoundError:
        return "Error: matrix.txt not found. Please ensure it's in 'resources/documents/'."

    rows = len(matrix)
    cols = len(matrix[0])

    # Handle the first row (can only be reached from the left)
    for j in range(1, cols):
        matrix[0][j] += matrix[0][j-1]

    # Handle the first column (can only be reached from above)
    for i in range(1, rows):
        matrix[i][0] += matrix[i-1][0]

    # Fill in the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
            
    # The bottom-right element now contains the minimal path sum
    return matrix[rows-1][cols-1]

if __name__ == "__main__":
    print(solve())
