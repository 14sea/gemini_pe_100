"""
Project Euler Problem 67: Maximum path sum II

Problem:
By starting at the top of the triangle in triangle.txt (a 15K text file containing a triangle with one-hundred rows) and moving to adjacent numbers on the row below, find the maximum total from top to bottom.

Solution Idea:
This problem is a classic example of dynamic programming. A brute-force approach of trying every possible path is computationally infeasible (2^99 paths). The efficient solution involves working from the bottom of the triangle up to the top.

1.  **Parse the Triangle**: First, we need to read the `triangle.txt` file and parse it into a 2D list or array of integers.

2.  **Dynamic Programming Approach**:
    - Let the triangle be represented by `T[i][j]`, where `i` is the row and `j` is the column.
    - We can start from the second-to-last row and move upwards.
    - For each number `T[i][j]` in a given row, the maximum path sum starting from that number can only go through one of two adjacent numbers in the row below it: `T[i+1][j]` or `T[i+1][j+1]`.
    - We can update the value of `T[i][j]` to be the sum of itself and the larger of its two children in the row below.
    - The update rule is: `T[i][j] = T[i][j] + max(T[i+1][j], T[i+1][j+1])`.

3.  **Algorithm**:
    a.  Read the triangle data from the file into a 2D list of integers.
    b.  Iterate through the rows of the triangle in reverse order, starting from the second-to-last row (`i = num_rows - 2`) up to the top row (`i = 0`).
    c.  In an inner loop, iterate through each element `j` in the current row `i`.
    d.  Apply the update rule: add the maximum of the two adjacent numbers from the row below to the current element.
    e.  After the loops complete, the top element of the triangle (`T[0][0]`) will contain the maximum possible path sum from the top to the bottom.

This method is highly efficient because it avoids re-calculating path sums. Each number in the triangle is visited only once.
"""

def solve():
    """
    Finds the maximum total from top to bottom in the triangle from triangle.txt.
    """
    try:
        with open('resources/documents/0067_triangle.txt', 'r') as f:
            triangle = [[int(n) for n in line.strip().split(' ')] for line in f]
    except FileNotFoundError:
        return "Error: triangle.txt not found. Please ensure it's in 'resources/documents/'."

    # Iterate from the second-to-last row up to the top
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Add the maximum of the two children in the row below
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            
    # The top element now contains the maximum path sum
    return triangle[0][0]

if __name__ == "__main__":
    print(solve())
