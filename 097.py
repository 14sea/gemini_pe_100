
# Find the last ten digits of the massive non-Mersenne prime 28433 * 2^7830457 + 1.

# Solution idea:
# To find the last ten digits of a number, we need to compute the number modulo 10^10.
# We can use modular arithmetic to handle the large numbers involved.
# The expression is (28433 * 2^7830457 + 1) mod 10^10.
# Python's built-in pow(base, exp, mod) function is perfect for this.
# It calculates (base^exp) % mod efficiently.

def main():
    mod = 10**10
    result = (28433 * pow(2, 7830457, mod) + 1) % mod
    print(result)

if __name__ == "__main__":
    main()
