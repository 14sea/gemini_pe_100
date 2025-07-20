"""
Project Euler Problem 88: Product-sum numbers

Problem:
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers is called a product-sum number.
For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?

Solution Idea:
Instead of iterating through k and trying to find the smallest N, it's more efficient to generate numbers N by their factorizations and find which k values they can be a minimal product-sum number for.

1.  **The `k` Formula**: For any factorization of `N` into `m` factors (each > 1) with sum `S`, we can make the sum equal to the product by adding `N - S` ones. The size of this new set is `k = m + (N - S)`.

2.  **Recursive Search**: We use a recursive function (DFS) to explore all possible factorizations of numbers up to a certain limit.
    - `search(product, sum, num_factors, start_factor)`
    - The `start_factor` ensures we generate unique factorizations (e.g., {2, 3} but not {3, 2}).

3.  **Algorithm**:
    a.  Set a limit for `k` (12000) and a search limit for `N` (a safe upper bound is 2*k, so 24000).
    b.  Create an array `min_n_for_k` to store the smallest `N` found for each `k`, initialized to infinity.
    c.  Start the recursive search. For each factorization found, calculate the corresponding `k`.
    d.  If the `k` is within the limit, update `min_n_for_k[k]` with the current product if it's smaller than the existing value.
    e.  After the search is complete, the `min_n_for_k` array will hold the minimal product-sum number for each `k`.
    f.  The final answer is the sum of the unique values in this array.
"""

def solve():
    """
    Finds the sum of all the minimal product-sum numbers for 2 <= k <= 12000.
    """
    K_LIMIT = 12000
    # The minimal N for a given k is between k and 2k. So the max N to check is ~2*K_LIMIT.
    N_LIMIT = 2 * K_LIMIT
    
    # Array to store the minimal product-sum number for each k
    min_n_for_k = [float('inf')] * (K_LIMIT + 1)

    def find_sums(product, current_sum, num_factors, start_factor):
        """
        Recursively explores factorizations to find product-sum numbers.
        """
        # We need at least two factors (including the ones we will add)
        if num_factors >= 2:
            # Calculate k for the current factorization
            k = product - current_sum + num_factors
            
            if k <= K_LIMIT:
                # We found a product-sum number 'product' for set size 'k'.
                # Update the minimum if this one is smaller.
                min_n_for_k[k] = min(min_n_for_k[k], product)

        # Continue adding factors to the product
        # The next factor 'i' must be at least 'start_factor' to avoid duplicates.
        # The new product must not exceed the overall limit.
        for i in range(start_factor, (N_LIMIT // product) * 2): # A bit of margin
             if product * i > N_LIMIT + 100: # Pruning
                 break
             find_sums(product * i, current_sum + i, num_factors + 1, i)

    # Start the search. The initial state represents an empty set of factors > 1.
    find_sums(1, 0, 0, 2)
    
    # The problem asks for the sum of all *unique* minimal numbers.
    unique_minimal_numbers = set(min_n_for_k[2:])
    return sum(unique_minimal_numbers)

if __name__ == "__main__":
    print(solve())
