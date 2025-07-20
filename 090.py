"""
Project Euler Problem 90: Cube digit pairs

Problem:
Find the number of distinct arrangements of two cubes (each with 6 unique digits from 0-9) that allow for all nine square numbers below one hundred (01, 04, 09, 16, 25, 36, 49, 64, 81) to be displayed. The digits 6 and 9 are interchangeable.

Solution Idea:
The problem is a combinatorial search. We can generate all possible pairs of cubes and check if each pair satisfies the condition.

1.  **Generate Cubes**: First, generate all unique sets of 6 digits that can be on a cube. This is a combination of choosing 6 digits from 10, which is `C(10, 6) = 210`.

2.  **Generate Pairs**: Iterate through all unique pairs of these 210 cubes.

3.  **Handle 6/9 Rule**: For each cube in a pair, if it contains a 6, we treat it as also containing a 9, and vice versa. This "extends" the set of digits available on each cube for checking.

4.  **Check Validity**: For a given pair of (extended) cubes, check if they can form all nine required two-digit square numbers. For a square `d1d2`, this means `d1` must be on one cube and `d2` on the other, or vice versa.

5.  **Count**: If a pair can form all nine squares, increment a counter. The final count is the answer.
"""
import itertools

def solve():
    """
    Finds the number of distinct arrangements of two cubes that allow for all
    square numbers to be displayed.
    """
    # The nine square numbers to be formed, represented as pairs of digits.
    # Note: 09 and 49 are handled by the 6/9 rule.
    squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]
    
    # Generate all possible unique cubes (combinations of 6 digits from 0-9)
    digits = list(range(10))
    all_cubes = list(itertools.combinations(digits, 6))
    
    valid_pairs_count = 0
    
    # Iterate through all unique pairs of cubes
    for i in range(len(all_cubes)):
        for j in range(i, len(all_cubes)):
            cube1_orig = set(all_cubes[i])
            cube2_orig = set(all_cubes[j])
            
            # Extend the cubes to handle the 6/9 rule
            cube1 = set(cube1_orig)
            if 6 in cube1: cube1.add(9)
            if 9 in cube1: cube1.add(6)
            
            cube2 = set(cube2_orig)
            if 6 in cube2: cube2.add(9)
            if 9 in cube2: cube2.add(6)
            
            is_valid_pair = True
            # Check if this pair can form all required square numbers
            for d1, d2 in squares:
                can_form = ((d1 in cube1 and d2 in cube2) or
                            (d1 in cube2 and d2 in cube1))
                
                if not can_form:
                    is_valid_pair = False
                    break
            
            if is_valid_pair:
                valid_pairs_count += 1
                
    return valid_pairs_count

if __name__ == "__main__":
    print(solve())
