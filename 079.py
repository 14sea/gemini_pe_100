"""
Project Euler Problem 79: Passcode derivation

Problem:
A text file, keylog.txt, contains fifty successful login attempts. Each attempt consists of three characters from a secret passcode. The three characters are always presented in the order they appear in the passcode. Analyse the file to determine the shortest possible secret passcode.

Solution Idea:
This problem can be modeled as finding a topological sort of a directed graph. The nodes of the graph are the unique digits present in the keylog, and a directed edge from digit `A` to digit `B` means that `A` must come before `B` in the passcode.

1.  **Build the Graph**:
    - We can represent the graph using a dictionary where keys are the nodes (digits) and values are sets of the nodes they point to (their successors).
    - We also need to keep track of the "in-degree" of each node, which is the number of incoming edges. This is crucial for the topological sort.
    - We read the `keylog.txt` file line by line. Each line (e.g., "319") gives us ordering information.
        - "319" implies `3 -> 1` and `1 -> 9`.
    - We process each login attempt: for `d1 d2 d3`, we add edges `d1 -> d2` and `d2 -> d3` to our graph. We also update the in-degree counts for `d2` and `d3`.

2.  **Topological Sort (Kahn's Algorithm)**:
    - The topological sort will give us a linear ordering of the digits that respects the precedence constraints we've established. The shortest possible passcode will use each unique digit only once.
    - The algorithm works as follows:
        a.  Find all nodes with an in-degree of 0. These are the nodes with no predecessors, so they can come first in the sequence. Add them to a queue.
        b.  Initialize an empty list for the sorted result (our passcode).
        c.  While the queue is not empty:
            i.   Dequeue a node `u`.
            ii.  Append `u` to the result list.
            iii. For each neighbor `v` of `u`:
                 - Decrement the in-degree of `v`.
                 - If the in-degree of `v` becomes 0, enqueue `v`.
    - The final result list will contain the digits in the correct order, forming the shortest possible passcode.

3.  **Implementation Details**:
    - We'll use a `defaultdict(set)` for the graph and a `defaultdict(int)` for the in-degrees.
    - We first need to find all unique characters in the file to initialize our data structures.
"""
import collections

def solve():
    """
    Determines the shortest possible secret passcode from the keylog file.
    """
    try:
        with open('resources/documents/0079_keylog.txt', 'r') as f:
            login_attempts = [line.strip() for line in f]
    except FileNotFoundError:
        return "Error: keylog.txt not found. Please ensure it's in 'resources/documents/'."

    # Graph representation: successors and in-degrees
    successors = collections.defaultdict(set)
    in_degrees = collections.defaultdict(int)
    nodes = set()

    # Process the login attempts to build the graph
    for attempt in login_attempts:
        nodes.update(attempt)
        # Add edges d1 -> d2 and d2 -> d3
        if attempt[0] not in successors[attempt[1]]:
            successors[attempt[0]].add(attempt[1])
        if attempt[1] not in successors[attempt[2]]:
            successors[attempt[1]].add(attempt[2])

    # Calculate in-degrees
    for u in successors:
        for v in successors[u]:
            in_degrees[v] += 1
            
    # Find starting nodes (in-degree of 0)
    queue = collections.deque([node for node in nodes if in_degrees[node] == 0])
    
    passcode = []
    
    # Perform topological sort
    while queue:
        u = queue.popleft()
        passcode.append(u)
        
        # Use a copy for safe iteration while removing
        for v in sorted(list(successors[u])):
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                queue.append(v)
                
    return "".join(passcode)

if __name__ == "__main__":
    print(solve())
