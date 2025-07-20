"""
Project Euler Problem 75: Singular integer right triangles

Problem:
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way. In contrast, some lengths, like 120 cm, can form more than one.

Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?

Solution Idea:
The problem is to find how many perimeters `L` correspond to exactly one Pythagorean triple `(a, b, c)`.

1.  **Generating Pythagorean Triples**: The most efficient way to generate all Pythagorean triples is using Euclid's formula. A triple `(a, b, c)` can be generated from two integers `m > n > 0` where `m` and `n` are coprime and not both odd.
    - `a = k * (m^2 - n^2)`
    - `b = k * (2mn)`
    - `c = k * (m^2 + n^2)`
    The triple is "primitive" when `k=1`. All other triples are multiples of a primitive one.

2.  **Perimeter Formula**: The perimeter `L` is `a + b + c`. Using the formulas above:
    `L = k * (m^2 - n^2 + 2mn + m^2 + n^2) = k * (2m^2 + 2mn) = k * 2m(m + n)`

3.  **Strategy**: Instead of checking each `L` and trying to find its triples, we can generate all possible triples and count how many times each perimeter `L` occurs.
    a.  We can create an array `counts` of size `1,500,001` to store the number of solutions for each perimeter length.
    b.  We first generate all *primitive* perimeters by setting `k=1`. We can do this by iterating through `m` and `n` under certain limits.
    c.  The perimeter `L = 2m(m + n)` must be `<= 1,500,000`. Since `n < m`, we have `L > 2m(m+m) = 4m^2`. This gives an upper bound for `m`: `m < sqrt(1,500,000 / 2)`, which is roughly 866.
    d.  We iterate `m` from 2 up to this limit. For each `m`, we iterate `n` from 1 to `m-1`, ensuring `m` and `n` are coprime and one is even (which is equivalent to `(m-n)` being odd).
    e.  For each primitive perimeter `p` found, we know that all its multiples (`p, 2p, 3p, ...`) are also valid perimeters. We can iterate through these multiples up to the limit and increment the count for each one in our `counts` array.

4.  **Final Count**: After the generation process is complete, we simply iterate through our `counts` array and count how many entries have a value of exactly 1.
"""
import math

def solve():
    """
    Finds the number of values of L <= 1,500,000 for which exactly one
    integer sided right angle triangle can be formed.
    """
    limit = 1_500_000
    perimeters = [0] * (limit + 1)
    
    # Determine the upper limit for m
    m_limit = int((limit / 2)**0.5)
    
    for m in range(2, m_limit + 1):
        for n in range(1, m):
            # Conditions for a primitive triple: m, n are coprime and one is even
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                # Calculate the perimeter of the primitive triple
                p = 2 * m * (m + n)
                
                # If the primitive perimeter is already over the limit,
                # no need to check larger n for this m.
                if p > limit:
                    break
                
                # Increment the count for this primitive and all its multiples
                for k in range(p, limit + 1, p):
                    perimeters[k] += 1
                    
    # Count how many perimeters have exactly one solution
    count = perimeters.count(1)
    return count

if __name__ == "__main__":
    print(solve())
