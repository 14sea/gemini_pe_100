"""
Project Euler Problem 61: Cyclical figurate numbers

Problem:
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type from triangle (3) to octagonal (8) is represented by a different number in the set.

Solution Idea:
This problem can be modeled as finding a specific cycle in a directed graph. The nodes of the graph are the 4-digit polygonal numbers, and a directed edge exists from number A to number B if the last two digits of A are the first two digits of B. We are looking for a cycle of length 6 where each node in the cycle belongs to a different polygonal type.

1.  **Generate Polygonal Numbers**:
    - First, we need to generate all 4-digit numbers (1000-9999) for each of the six polygonal types (Triangle, Square, ..., Octagonal).
    - We can store these numbers in a data structure, for example, a dictionary where keys are the polygonal type (3 to 8) and values are lists of the corresponding 4-digit numbers.

2.  **Structure for Efficient Search**:
    - To make the search for the next number in a cycle efficient, it's helpful to group the generated numbers by their first two digits.
    - We can create a dictionary where keys are the polygonal types, and the values are another dictionary mapping a 2-digit prefix (e.g., '81') to a list of numbers of that type starting with that prefix (e.g., `[8128]`).

3.  **Depth-First Search (DFS)**:
    - A recursive depth-first search is a natural fit for this problem. We will try to build the cycle step by step.
    - We can define a function `find_cycle(chain, used_types)` where `chain` is the list of numbers found so far and `used_types` is a set of the polygonal types used.
    - The search starts by picking a number from one of the polygonal sets (e.g., an octagonal number, as it's the most constrained set) to be the first number in our chain.
    - In each recursive step, we take the last number in the chain, get its last two digits, and use that as the prefix to search for the next number.
    - We search through the remaining unused polygonal types to find a number that starts with this prefix.
    - If we find a candidate, we add it to the chain and recurse. If the recursion returns a valid solution, we propagate it up. If not, we backtrack and try the next candidate.

4.  **Base Case and Termination**:
    - The base case for the recursion is when the chain has 6 numbers.
    - At this point, we must check if the last number is cyclic with the first number. If it is, we have found the unique solution.
    - Since the problem guarantees a unique solution, the first complete cycle we find will be the answer. We can then stop the search and sum the numbers in the cycle.
"""
import collections

def generate_polygonal_numbers():
    """
    Generates all 4-digit polygonal numbers for types 3 through 8.
    """
    polygonal_map = collections.defaultdict(list)
    
    formulas = {
        3: lambda n: n * (n + 1) // 2,
        4: lambda n: n * n,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2),
    }
    
    for p_type, formula in formulas.items():
        n = 1
        while True:
            num = formula(n)
            if num >= 10000:
                break
            if num >= 1000:
                polygonal_map[p_type].append(num)
            n += 1
    return polygonal_map

def find_cycle(chain, used_types, polygonal_numbers, all_types):
    """
    Recursively searches for the 6-number cyclic set.
    """
    # Base case: if we have a chain of 6, check if it's a valid cycle
    if len(chain) == 6:
        if str(chain[-1])[2:] == str(chain[0])[:2]:
            return chain
        else:
            return None

    last_num_suffix = str(chain[-1])[2:]
    available_types = all_types - used_types
    
    for p_type in available_types:
        for num in polygonal_numbers[p_type]:
            if str(num).startswith(last_num_suffix):
                new_chain = chain + [num]
                new_used_types = used_types | {p_type}
                
                result = find_cycle(new_chain, new_used_types, polygonal_numbers, all_types)
                if result:
                    return result
    return None

def solve():
    """
    Finds the sum of the only ordered set of six cyclic 4-digit numbers
    where each polygonal type is represented.
    """
    polygonal_numbers = generate_polygonal_numbers()
    all_types = set(range(3, 9))
    
    # Start the search with the octagonal numbers (P8), as it's the smallest set.
    p8_numbers = polygonal_numbers[8]
    
    for start_num in p8_numbers:
        chain = [start_num]
        used_types = {8}
        
        solution = find_cycle(chain, used_types, polygonal_numbers, all_types)
        if solution:
            return sum(solution)
            
    return "Solution not found."

if __name__ == "__main__":
    print(solve())
