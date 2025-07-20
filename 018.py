def solve():
    """
    Solves the Project Euler Problem 18.

    Question:
    By starting at the top of the triangle below and moving to adjacent numbers
    on the row below, find the maximum total from top to bottom.

    (Triangle data is provided in the problem description)

    Solution Idea:
    A brute-force approach of trying every path is possible but inefficient. A
    much better method is dynamic programming, working from the bottom up.

    The process is as follows:
    1. Start at the second-to-last row of the triangle.
    2. For each number in this row, add the larger of its two "children" from
       the row below it.
    3. This effectively collapses the bottom row into the second-to-last row,
       where each element now represents the maximum path sum from that point.
    4. Repeat this process, moving up the triangle one row at a time, until
       we reach the top.
    5. The single number remaining at the top will be the maximum total path sum.
    """
    triangle_str = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    
    triangle = [list(map(int, line.split())) for line in triangle_str.strip().split('\n')]

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
            
    print(f"The maximum total from top to bottom is: {triangle[0][0]}")

solve()