"""
Project Euler Problem 83: Path sum: four ways

Problem:
Find the minimal path sum from the top left to the bottom right of an 80x80 matrix (in matrix.txt), by moving left, right, up, and down.

Solution Idea:
This problem is equivalent to finding the shortest path in a weighted directed graph. The cells of the matrix are the nodes, and the "weights" of the nodes are the values in the cells. An edge exists between any two adjacent cells (up, down, left, right). The cost of traversing a path is the sum of the values of all cells on the path.

Dijkstra's algorithm is the perfect tool for this.

1.  **Graph Representation**:
    - The matrix itself can be thought of as the graph.
    - We need a way to keep track of the minimum distance (path sum) from the start node to every other node. We can use a 2D array, `distances`, initialized to infinity for all cells.

2.  **Dijkstra's Algorithm**:
    a.  Initialize a `distances` matrix of the same size as the input matrix, with all values set to infinity, except for the starting cell (top-left, `(0,0)`), which is set to its own value from the input matrix.
    b.  Create a priority queue. A priority queue is essential for Dijkstra's as it allows us to always explore the node with the smallest current distance. We'll store tuples of `(distance, row, col)` in the queue.
    c.  Add the starting node to the priority queue: `(matrix[0][0], 0, 0)`.
    d.  While the priority queue is not empty:
        i.   Pop the element with the smallest distance. Let this be `(dist, r, c)`.
        ii.  If this `dist` is greater than the already known shortest distance to `(r, c)` in our `distances` matrix, it means we've found a better path to this node already, so we can skip it.
        iii. For each neighbor `(nr, nc)` of the current cell `(r, c)` (up, down, left, right):
             - Calculate the new potential distance to this neighbor: `new_dist = dist + matrix[nr][nc]`.
             - If `new_dist` is smaller than the current recorded distance to the neighbor (`distances[nr][nc]`), it means we've found a shorter path.
             - Update `distances[nr][nc] = new_dist`.
             - Push the neighbor onto the priority queue: `(new_dist, nr, nc)`.
    e.  The algorithm terminates when the priority queue is empty. The value in the bottom-right cell of our `distances` matrix (`distances[rows-1][cols-1]`) will be the minimal path sum.
"""
import heapq

def solve():
    """
    Finds the minimal path sum from the top left to the bottom right,
    allowing movement in all four directions.
    """
    try:
        with open('resources/documents/0083_matrix.txt', 'r') as f:
            matrix = [[int(n) for n in line.strip().split(',')] for line in f]
    except FileNotFoundError:
        return "Error: matrix.txt not found. Please ensure it's in 'resources/documents/'."

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize distances with infinity
    distances = [[float('inf')] * cols for _ in range(rows)]
    
    # Start node distance is its own value
    distances[0][0] = matrix[0][0]
    
    # Priority queue for Dijkstra's algorithm: (distance, row, col)
    pq = [(matrix[0][0], 0, 0)]
    
    while pq:
        dist, r, c = heapq.heappop(pq)
        
        # If we've found a shorter path already, skip
        if dist > distances[r][c]:
            continue
        
        # Check all four neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            # Check if the neighbor is within bounds
            if 0 <= nr < rows and 0 <= nc < cols:
                new_dist = dist + matrix[nr][nc]
                
                # If we found a shorter path to the neighbor
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))
                    
    # The result is the distance to the bottom-right cell
    return distances[rows-1][cols-1]

if __name__ == "__main__":
    print(solve())
