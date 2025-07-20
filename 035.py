"""
Project Euler Problem 35: Circular primes

Problem:
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Solution Idea:
To solve this, we need an efficient way to check for primality and a method to rotate the digits of a number.

1.  **Efficient Primality Testing**: Since we need to check for primality for many numbers up to one million, the most efficient approach is to pre-compute all primes up to the limit using a **Sieve of Eratosthenes**. This will create a boolean array, say `is_prime`, where `is_prime[i]` is true if `i` is prime, and false otherwise. This allows for O(1) lookup time for primality checks.

2.  **Checking for Circular Primes**:
    - We will iterate through each number `n` from 2 up to 999,999.
    - For each `n`, we first check if it's a prime using our sieve.
    - If `n` is prime, we then need to check if all its rotations are also prime.
    - To get the rotations of `n`, we can convert it to a string. For a number like `197`, the string is `"197"`. We can generate rotations by moving the first digit to the end:
        - `"197"` -> `"971"` -> `"719"`
    - For each generated rotation, we convert it back to an integer and check its primality using our sieve.
    - If all rotations are prime, we count the original number `n` as a circular prime.

3.  **Counting**:
    - We initialize a counter to 0.
    - When we find a number that is a circular prime, we increment the counter.
    - The final value of the counter will be our answer. The problem asks for the count of such primes, so we don't need to worry about duplicates in the count (e.g., counting 197, 971, and 719 separately is correct as they are all distinct circular primes).
"""

def solve():
    """
    Finds the number of circular primes below one million.
    """
    limit = 1_000_000
    
    # Step 1: Sieve of Eratosthenes to find all primes up to the limit
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, limit, i):
                is_prime[multiple] = False

    circular_prime_count = 0
    # Step 2: Iterate through numbers and check for circular prime property
    for n in range(2, limit):
        if is_prime[n]:
            # It's a prime, now check if it's circular
            s = str(n)
            is_circular = True
            # Generate and check all rotations
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]  # Rotate the string
                rotation = int(s)
                if not is_prime[rotation]:
                    is_circular = False
                    break
            
            if is_circular:
                circular_prime_count += 1
                
    return circular_prime_count

if __name__ == "__main__":
    print(solve())
