import math

def solve():
    """
    Solves the Project Euler Problem 15.

    Question:
    Starting in the top left corner of a 2x2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20x20 grid?

    Solution Idea:
    This is a classic combinatorial problem. To traverse a 20x20 grid from the
    top-left to the bottom-right corner by only moving right and down, one must
    make exactly 20 "right" moves and 20 "down" moves.

    The total number of moves is 40 (20 right + 20 down). The problem is
    equivalent to finding the number of unique sequences of these 40 moves.
    This can be calculated using the binomial coefficient C(n, k), which
    determines the number of ways to choose k items from a set of n.

    Here, n = 40 (total moves) and k = 20 (moves of one type, e.g., right).
    We need to calculate C(40, 20) = 40! / (20! * 20!).
    """
    grid_size = 20
    num_paths = math.comb(2 * grid_size, grid_size)
    print(f"For a {grid_size}x{grid_size} grid, there are {num_paths} routes.")

solve()