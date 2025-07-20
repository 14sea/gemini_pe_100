"""
Project Euler Problem 78: Coin partitions

Problem:
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
Find the least value of n for which p(n) is divisible by one million.

Solution Idea:
This problem asks for the partition function `p(n)`. A direct dynamic programming approach like in Problem 76 would be too slow and memory-intensive, as `n` could be very large.

A more advanced and efficient method uses Euler's Pentagonal Number Theorem. The theorem provides a recurrence relation for `p(n)`:
`p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-11) + p(n-12) - ...`

The general formula is:
`p(n) = sum_{k=1 to infinity} [ (-1)^(k-1) * (p(n - k(3k-1)/2) + p(n - k(3k+1)/2)) ]`

The numbers `k(3k-1)/2` and `k(3k+1)/2` are the generalized pentagonal numbers. The sequence of these numbers is 1, 2, 5, 7, 12, 15, 22, 26, ...

1.  **Pentagonal Numbers**: We need a way to generate the generalized pentagonal numbers `g_k = k(3k-1)/2` for `k = 1, -1, 2, -2, 3, -3, ...`.

2.  **Recurrence with Modulo**: We are looking for `p(n)` that is divisible by one million, which means `p(n) % 1,000,000 == 0`. We can apply the modulo operation at each step of the calculation to keep the numbers manageable. The recurrence relation holds true under modular arithmetic.

3.  **Algorithm**:
    a.  Set `mod = 1,000,000`.
    b.  Create a list `partitions` to store the values of `p(i) % mod`. Initialize `partitions[0] = 1`.
    c.  Start a loop for `n` from 1 upwards.
    d.  Inside the loop, calculate `p(n)` using the recurrence relation and the previously computed values in the `partitions` list.
        i.   Initialize `p_n = 0`.
        ii.  Loop `k` from 1 upwards.
        iii. Calculate the two generalized pentagonal numbers for `k`.
        iv.  If these pentagonal numbers are greater than `n`, we can stop the inner loop.
        v.   Add or subtract the corresponding `p(n - g_k)` terms to `p_n` based on the `(-1)^(k-1)` sign.
        vi.  Remember to take the modulo at each step.
    e.  Store the result: `partitions.append(p_n % mod)`.
    f.  Check if `p_n % mod == 0`. If it is, then `n` is our answer.
"""

def solve():
    """
    Finds the least value of n for which p(n) is divisible by one million.
    """
    mod = 1_000_000
    partitions = [1]
    n = 0
    
    while True:
        n += 1
        p_n = 0
        k = 1
        
        while True:
            # Calculate generalized pentagonal numbers
            pent1 = k * (3 * k - 1) // 2
            pent2 = k * (3 * k + 1) // 2
            
            term1_val = 0
            if n >= pent1:
                term1_val = partitions[n - pent1]
            
            term2_val = 0
            if n >= pent2:
                term2_val = partitions[n - pent2]
            
            # The sum of terms for this k
            total_term = term1_val + term2_val
            
            # Stop if we've gone past n
            if total_term == 0:
                break
            
            # Apply the sign based on k
            if k % 2 == 1: # k is odd
                p_n += total_term
            else: # k is even
                p_n -= total_term
            
            k += 1
            
        # Store the result modulo 1,000,000
        p_n %= mod
        partitions.append(p_n)
        
        # Check for the condition
        if p_n == 0:
            return n

if __name__ == "__main__":
    print(solve())
