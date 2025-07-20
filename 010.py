
# Question:
# The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.
#
# Find the sum of all the primes below two million.
#
# Solution Ideas:
# This problem requires finding the sum of all prime numbers below two million.
# A common and efficient algorithm for finding all prime numbers up to a given limit is the Sieve of Eratosthenes.
#
# Algorithm for Sieve of Eratosthenes:
# 1. Create a boolean array "is_prime" of size n+1 (where n is the limit, 2 million in this case), and initialize all entries as true.
# 2. Mark 0 and 1 as not prime (false).
# 3. Iterate from p = 2 up to sqrt(n):
#    a. If is_prime[p] is true, then p is a prime number.
#    b. Mark all multiples of p (starting from p*p) as not prime. For example, if p is 2, mark 4, 6, 8, ... as not prime.
# 4. After the loop, all numbers for which is_prime[i] is true are prime numbers.
# 5. Sum all the prime numbers found.
#
# The current solution implements the Sieve of Eratosthenes correctly.
# It initializes a boolean array `is_prime` of size `n` (2 million).
# It correctly handles the base cases of 0 and 1.
# It iterates from 2 up to the square root of `n`, marking multiples as not prime.
# Finally, it iterates through the `is_prime` array and sums all numbers marked as prime.
# This approach is efficient for the given limit.

def solve():
    n = 2000000
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, n, i):
                is_prime[multiple] = False
    
    total = 0
    for i in range(n):
        if is_prime[i]:
            total += i
            
    print(total)

solve()
