"""
Project Euler Problem 39: Integer right triangles

Problem:
If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?

Solution Idea:
We need to find the number of unique integer sets {a, b, c} that form a right-angle triangle for each perimeter `p` up to 1000. A brute-force approach of iterating through all possible side lengths `a` and `b` is possible, but a more efficient method uses Euclid's formula for generating Pythagorean triples.

1.  **Euclid's Formula**: All *primitive* Pythagorean triples (where a, b, and c have no common divisors) can be generated from two integers `m` and `k` where `m > k > 0`, `m` and `k` are coprime, and one of them is even. The sides are given by:
    - `a = m^2 - k^2`
    - `b = 2mk`
    - `c = m^2 + k^2`

2.  **Perimeter of Primitive Triples**: The perimeter `p_primitive` for such a triple is:
    `p_primitive = a + b + c = (m^2 - k^2) + 2mk + (m^2 + k^2) = 2m^2 + 2mk = 2m(m + k)`

3.  **Generating All Triples**: Any non-primitive triple is simply a multiple of a primitive one. For example, {6, 8, 10} is 2 * {3, 4, 5}. This means that the perimeter of any right-angle triangle will be a multiple of the perimeter of a primitive one.
    `p = d * p_primitive` for some integer `d >= 1`.

4.  **Algorithm**:
    - We can create an array `counts` of size 1001 to store the number of solutions for each perimeter.
    - We iterate through possible values of `m` and `k` that satisfy the conditions.
    - The perimeter `p = 2m(m+k)` must be less than or equal to 1000. Since `k < m`, `2m(m+m) > p`, which means `4m^2 > p`. A loose upper bound for `m` is `sqrt(1000/2)`, so `m` only needs to go up to about 22.
    - For each pair `(m, k)` that generates a primitive triple, we calculate `p_primitive`.
    - We then iterate through all multiples of `p_primitive` (i.e., `p_primitive, 2*p_primitive, 3*p_primitive, ...`) that are less than or equal to 1000 and increment the count for each of these perimeters in our `counts` array.
    - Finally, we find the index (the perimeter `p`) in the `counts` array that has the highest value.
"""
import math

def solve():
    """
    Finds the perimeter p <= 1000 for which the number of right-angle triangle solutions is maximised.
    """
    limit = 1000
    counts = [0] * (limit + 1)
    
    # Iterate through m and k to generate primitive triples
    m_limit = int((limit / 2)**0.5)
    for m in range(2, m_limit + 1):
        for k in range(1, m):
            # Conditions for a primitive triple: m, k are coprime and one is even
            if (m - k) % 2 == 1 and math.gcd(m, k) == 1:
                # Calculate the perimeter of the primitive triple
                p_primitive = 2 * m * (m + k)
                
                # Add counts for this primitive and all its multiples up to the limit
                p = p_primitive
                while p <= limit:
                    counts[p] += 1
                    p += p_primitive
                    
    # Find the perimeter with the maximum number of solutions
    max_solutions = 0
    result_p = 0
    for p in range(1, limit + 1):
        if counts[p] > max_solutions:
            max_solutions = counts[p]
            result_p = p
            
    return result_p

if __name__ == "__main__":
    print(solve())
