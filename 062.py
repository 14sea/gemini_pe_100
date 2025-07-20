"""
Project Euler Problem 62: Cubic permutations

Problem:
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

Solution Idea:
We are looking for the smallest cube that is a member of a 5-member "permutation family" of cubes. A direct approach of generating cubes and then finding all their permutations to check for other cubes would be very inefficient.

A much better approach is to use a "canonical representation" for the permutations. For any number, we can find its canonical form by sorting its digits. For example, the canonical form of `41063625` is `'01234566'`. Any number that is a permutation of `41063625` will have the same canonical form.

1.  **Algorithm**:
    a.  We can use a dictionary to group cubes by their canonical digit representation. The keys of the dictionary will be the sorted digit strings (the canonical form), and the values will be a list of the cubes that have that canonical form.
    b.  We will iterate through integers `n = 1, 2, 3, ...` and calculate their cubes, `c = n^3`.
    c.  For each cube `c`, we find its canonical form by sorting its digits.
    d.  We then add the cube `c` to the list associated with its canonical form in our dictionary.
    e.  After adding a cube, we check the length of the list for its canonical form. If the length is exactly 5, we have found a family of five cubic permutations.
    f.  Because we are iterating `n` in increasing order, the first time we find a family of 5, the smallest cube in that family will be the smallest cube that satisfies the condition. We can then find the minimum value in that list and return it as the answer.

2.  **Search Range**: We don't know the upper limit for `n`, but we can start iterating and stop as soon as we find the first family of 5. This is guaranteed to give us the smallest such cube.
"""
import collections

def solve():
    """
    Finds the smallest cube for which exactly five permutations of its digits are cube.
    """
    cubes_by_permutation = collections.defaultdict(list)
    n = 1
    
    while True:
        cube = n**3
        
        # Create a canonical representation of the digits
        canonical_form = "".join(sorted(str(cube)))
        
        # Add the cube to the list for its canonical form
        cubes_by_permutation[canonical_form].append(cube)
        
        # Check if we have found a family of 5
        if len(cubes_by_permutation[canonical_form]) == 5:
            # Since we are iterating n upwards, the first family of 5 we find
            # must contain the smallest such cube.
            return min(cubes_by_permutation[canonical_form])
            
        n += 1

if __name__ == "__main__":
    print(solve())
