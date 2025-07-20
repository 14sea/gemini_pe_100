
# Question:
# A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
# $a^2 + b^2 = c^2.$
#
# For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
#
# There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.
# Find the product $abc$.
#
# Solution Ideas:
# We are looking for three natural numbers a, b, c such that a < b < c, a^2 + b^2 = c^2, and a + b + c = 1000.
# From a + b + c = 1000, we can write c = 1000 - a - b.
# Substitute c into the Pythagorean equation: a^2 + b^2 = (1000 - a - b)^2.
# Expand and simplify this equation to find a relationship between a and b.
# Since a, b, c are natural numbers, a, b, c > 0.
# Also, a < b < c.
# From a + b + c = 1000, and a < b < c, we know:
# a < b < 1000 - a - b
# 2b < 1000 - a
# 3a < 1000 (since a < b < c, 3a < a+b+c = 1000)
# So, a must be less than 1000/3, i.e., a <= 333.
# Also, b must be less than 1000/2, i.e., b <= 499 (since a >= 1, b < c, a+b+c = 1000 => 2b < 1000-a => b < (1000-a)/2).
# We can iterate through possible values of 'a' and 'b' and check if 'c' is an integer and satisfies the conditions.
# The current solution iterates through 'a' and 'b' and calculates 'c'. It then checks if c > b and if a^2 + b^2 == c^2.
# This approach seems correct and efficient enough given the constraints.

def solve():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if c > b and a**2 + b**2 == c**2:
                print(a * b * c)
                return

solve()
