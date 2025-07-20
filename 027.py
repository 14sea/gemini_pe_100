"""
Project Euler Problem 27: Quadratic primes

Problem:
Euler discovered the remarkable quadratic formula: n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

Solution Idea:
We need to find the combination of coefficients 'a' and 'b' that generates the longest sequence of prime numbers for n = 0, 1, 2, ...

1.  **Constraints on `a` and `b`**:
    - `a` is in the range `[-999, 999]`.
    - `b` is in the range `[-1000, 1000]`.

2.  **Optimizing the search space**:
    - When `n = 0`, the formula is `0^2 + a*0 + b = b`. For this to be a prime number, `b` itself must be a prime number. This significantly reduces the number of values we need to check for `b`. Also, since primes are positive, `b` must be greater than 1. So, we only need to check prime values of `b` from 2 to 1000.
    - When `n = 1`, the formula is `1 + a + b`. This must also be prime.

3.  **Primality Test**: We need an efficient function to check if a number is prime. A standard `is_prime` function that checks for divisibility up to the square root of the number will work. We can add a cache (memoization) to this function to avoid re-calculating primality for the same number multiple times, which will speed up the process.

4.  **The Algorithm**:
    - Create a list of all prime numbers up to 1000. These are our candidates for `b`.
    - Iterate through each possible value of `a` from -999 to 999.
    - For each `a`, iterate through each prime `b` from our list.
    - For each pair `(a, b)`, start with `n = 0` and count how many consecutive prime numbers the formula `n^2 + an + b` produces.
    - Keep track of the `(a, b)` pair that produces the longest chain of primes.
    - After checking all pairs, the answer is the product of the `a` and `b` that gave the maximum length.
"""
import math

prime_cache = {}

def is_prime(n):
    """
    Checks if a number is prime with memoization.
    """
    if n in prime_cache:
        return prime_cache[n]
    
    if n < 2:
        prime_cache[n] = False
        return False
    if n == 2:
        prime_cache[n] = True
        return True
    if n % 2 == 0:
        prime_cache[n] = False
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            prime_cache[n] = False
            return False
            
    prime_cache[n] = True
    return True

def solve():
    """
    Finds the product of coefficients a and b for the quadratic expression
    that produces the maximum number of primes for consecutive values of n.
    """
    max_primes = 0
    best_a = 0
    best_b = 0

    # Optimization: b must be a prime
    primes_b = [i for i in range(2, 1001) if is_prime(i)]

    for b in primes_b:
        for a in range(-999, 1000):
            n = 0
            while True:
                result = n*n + a*n + b
                if not is_prime(result):
                    break
                n += 1
            
            if n > max_primes:
                max_primes = n
                best_a = a
                best_b = b
                
    return best_a * best_b

if __name__ == "__main__":
    print(solve())
