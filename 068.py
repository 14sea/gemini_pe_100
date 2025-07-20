"""
Project Euler Problem 68: Magic 5-gon ring

Problem:
Using the numbers 1 to 10, find the maximum 16-digit string for a "magic" 5-gon ring.

The rules for the ring are:
1. It's a 5-gon, with 5 outer nodes and 5 inner nodes.
2. The numbers 1 to 10 must be used exactly once to fill the 10 nodes.
3. Each of the 5 lines (consisting of an outer node and two adjacent inner nodes) must sum to the same total.
4. The solution string is formed by starting with the group that has the numerically lowest external node and concatenating the groups clockwise.

Solution Idea:
This is a constrained search problem. A brute-force check of all 10! permutations is too slow. We can use the properties of the ring to find the solution efficiently.

1.  **16-Digit String Constraint**:
    - A 5-gon ring has 5 lines of 3 numbers each. If all numbers were single-digit, the concatenated string would have 5 * 3 = 15 digits.
    - To get a 16-digit string, exactly one of the numbers used must be the two-digit number `10`.
    - The inner nodes are part of two lines each, while outer nodes are part of one line each. If `10` were an inner node, it would appear twice in the final string, making the string at least 17 digits long.
    - Therefore, the number `10` **must be an outer node**. This is a key constraint.

2.  **Sum Constraint**:
    - Let the sum of the inner nodes be `S_in` and the sum of the outer nodes be `S_out`. The sum of all numbers is `1 + ... + 10 = 55`.
    - When we sum all 5 lines, we sum each outer node once and each inner node twice.
    - If the magic sum for each line is `T`, then `5 * T = S_out + 2 * S_in`.
    - We also know `S_out = 55 - S_in`.
    - Substituting this gives `5 * T = (55 - S_in) + 2 * S_in = 55 + S_in`.
    - This implies that `55 + S_in` must be divisible by 5, which means `S_in` must be divisible by 5.

3.  **Search Algorithm**:
    a.  Generate all combinations of 5 numbers from `{1, ..., 9}` to be the inner nodes. The number 10 must be an outer node.
    b.  For each combination of inner nodes, check if their sum is divisible by 5. If not, discard it.
    c.  If the sum is valid, calculate the required magic total `T` and determine the set of outer nodes.
    d.  Try all permutations of the inner nodes to see if they can form a valid ring with the outer nodes.
    e.  For a given permutation of inner nodes `(i1, i2, i3, i4, i5)`, calculate the required outer nodes `e1 = T-i1-i2`, `e2 = T-i2-i3`, etc.
    f.  Check if this set of required outer nodes matches the actual set of outer nodes.
    g.  If it matches, we have found a valid solution. Format it into a string according to the rules (start with the lowest outer node, go clockwise).
    h.  Keep track of the maximum 16-digit string found.
"""
import itertools

def solve():
    """
    Finds the maximum 16-digit string for a magic 5-gon ring.
    """
    max_string = ""
    
    # The numbers 1 to 9 are candidates for the inner ring. 10 must be outer.
    nums_1_to_9 = set(range(1, 10))
    
    # 1. Choose 5 numbers for the inner ring from {1..9}
    for inner_nodes_tuple in itertools.combinations(nums_1_to_9, 5):
        inner_nodes = set(inner_nodes_tuple)
        
        # 2. Check if the sum is divisible by 5
        sum_inner = sum(inner_nodes)
        if sum_inner % 5 != 0:
            continue
            
        # 3. Determine the magic sum and the set of outer nodes
        magic_sum = (55 + sum_inner) // 5
        outer_nodes = (nums_1_to_9 - inner_nodes) | {10}
        
        # 4. Try all arrangements of the inner nodes
        for p_inner in itertools.permutations(inner_nodes):
            i1, i2, i3, i4, i5 = p_inner
            
            # 5. Calculate the required outer nodes for this arrangement
            e1 = magic_sum - i1 - i2
            e2 = magic_sum - i2 - i3
            e3 = magic_sum - i3 - i4
            e4 = magic_sum - i4 - i5
            e5 = magic_sum - i5 - i1
            
            # 6. Check if this arrangement is valid
            if {e1, e2, e3, e4, e5} == outer_nodes:
                solution_groups = [(e1, i1, i2), (e2, i2, i3), (e3, i3, i4), (e4, i4, i5), (e5, i5, i1)]
                
                # 7. Format the solution string
                min_ext_val = min(e1, e2, e3, e4, e5)
                start_index = [e1, e2, e3, e4, e5].index(min_ext_val)
                
                current_string = ""
                for i in range(5):
                    group = solution_groups[(start_index + i) % 5]
                    current_string += "".join(map(str, group))
                    
                # 8. Check length and update max
                if len(current_string) == 16:
                    if current_string > max_string:
                        max_string = current_string
                        
    return max_string

if __name__ == "__main__":
    print(solve())
