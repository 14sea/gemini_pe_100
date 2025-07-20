"""
Solves the Project Euler Problem 8.

Question:
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

(A 1000-digit number is given)

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

Solution Idea:
The problem asks us to find the greatest product of 13 consecutive digits in a given 1000-digit number.

We can solve this using a "sliding window" approach.
1. First, combine the multi-line string of digits into a single, continuous string.
2. We will use a window of size 13 that slides across this string of digits.
3. We can loop from the start of the string up to the point where a full 13-digit window can still be formed. This means looping from index 0 to `len(string) - 13`.
4. For each position `i`, we consider the slice of 13 digits from `i` to `i + 13`.
5. We calculate the product of these 13 digits.
   - An important edge case is the presence of the digit '0'. If a '0' is in our window, the product will be 0. We can use this to optimize by skipping ahead in our main loop if we encounter a '0'.
6. We keep track of the maximum product found so far.
7. After checking all possible 13-digit windows, the value stored in our maximum product variable is the answer.

Let's refine the optimization: When we slide the window, instead of re-multiplying all 13 digits, we can divide by the digit that is leaving the window and multiply by the new digit that is entering. However, this is complicated by the presence of zeros. A simple loop that recalculates the product for each window is clear to implement and fast enough for this problem size.
"""

def solve():
    s = (
        "73167176531330624919225119674426574742355349194934"
        "96983520312774506326239578318016984801869478851843"
        "85861560789112949495459501737958331952853208805511"
        "12540698747158523863050715693290963295227443043557"
        "66896648950445244523161731856403098711121722383113"
        "62229893423380308135336276614282806444486645238749"
        "30358907296290491560440772390713810515859307960866"
        "70172427121883998797908792274921901699720888093776"
        "65727333001053367881220235421809751254540594752243"
        "52584907711670556013604839586446706324415722155397"
        "53697817977846174064955149290862569321978468622482"
        "83972241375657056057490261407972968652414535100474"
        "82166370484403199890008895243450658541227588666881"
        "16427171479924442928230863465674813919123162824586"
        "17866458359124566529476545682848912883142607690042"
        "24219022671055626321111109370544217506941658960408"
        "07198403850962455444362981230987879927244284909188"
        "84580156166097919133875499200524063689912560717606"
        "05886116467109405077541002256983155200055935729725"
        "71636269561882670428252483600823257530420752963450"
    )
    
    largest_product = 0
    num_digits = 13
    
    for i in range(len(s) - num_digits + 1):
        product = 1
        for digit in s[i:i+num_digits]:
            product *= int(digit)
        if product > largest_product:
            largest_product = product
            
    print(largest_product)

solve()