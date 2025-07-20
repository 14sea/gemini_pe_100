"""
Project Euler Problem 31: Coin sums

Problem:
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

Solution Idea:
This is a classic "coin change" problem, which can be solved efficiently using dynamic programming. We want to find the number of ways to make a target amount (200p) using a given set of coins.

1.  **Define the State**: Let `ways[i]` be the number of ways to make the amount `i`. We want to find `ways[200]`.

2.  **Initialization**:
    - We create a list or array called `ways` of size `target + 1` (i.e., 201).
    - We initialize `ways[0]` to 1. This is our base case: there is exactly one way to make the amount 0 (by using no coins). All other elements `ways[i]` are initialized to 0.

3.  **Iteration**:
    - We iterate through each `coin` in our list of coins: `[1, 2, 5, 10, 20, 50, 100, 200]`.
    - For each `coin`, we then iterate through all amounts `j` from the value of the `coin` up to our target of 200.
    - For each amount `j`, we can form it by adding the current `coin` to a previously formed amount `j - coin`. So, we update our `ways` array by adding the number of ways to make the remaining amount (`j - coin`) to the current amount `j`.
    - The update rule is: `ways[j] = ways[j] + ways[j - coin]`.

4.  **Result**: After iterating through all the coins, the value at `ways[200]` will hold the total number of different combinations to make 200p. The order of the loops (coins on the outside, amounts on the inside) is crucial to ensure we count combinations, not permutations.
"""

def solve():
    """
    Calculates the number of different ways to make £2 (200p) using any number of coins.
    """
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    # Initialize a list to store the number of ways to make each amount
    ways = [0] * (target + 1)
    
    # Base case: There is one way to make 0 (using no coins)
    ways[0] = 1
    
    # Iterate through each coin
    for coin in coins:
        # Update the ways array for amounts from the coin value up to the target
        for j in range(coin, target + 1):
            ways[j] += ways[j - coin]
            
    return ways[target]

if __name__ == "__main__":
    print(solve())
