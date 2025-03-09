# Path Finding Algorithms: BFS vs DFS Implementation

This project implements and compares two fundamental graph traversal algorithms - Breadth-First Search (BFS) and Depth-First Search (DFS) - for finding paths between nodes in a weighted graph. The implementation demonstrates pathfinding between cities/locations connected by roads with different distances.

## 🎯 Project Overview

The project consists of:

- BFS implementation for finding paths with minimum edges
- DFS implementation for finding any valid path
- Comparative analysis of both approaches
- LaTeX documentation with detailed explanations
- Interactive Jupyter notebook implementations

## 🗺️ Graph Structure

The graph represents a network of locations connected by weighted edges:

- Nodes: Locations labeled as S, A, B, C, D, E, F, G, H
- Edges: Weighted connections representing distances between locations
- Start node: S (Source)
- Goal node: G (Destination)
- Bidirectional connections with weights:
  ```
  S-A: 3, S-B: 6, S-C: 2
  A-D: 3, B-E: 2, C-E: 1
  D-F: 5, F-G: 5, E-H: 5
  H-G: 5, B-G: 9, D-B: 4
  E-F: 6
  ```

## 💻 Implementation Details

### Breadth-First Search (BFS)

- Finds path with minimum number of edges (not necessarily shortest by distance)
- Uses queue data structure (FIFO principle)
- Explores nodes level by level
- Time Complexity: O(V + E) where V is vertices and E is edges
- Space Complexity: O(V)

### Depth-First Search (DFS)

- Finds any possible path to destination
- Uses stack data structure (LIFO principle)
- Explores one path completely before backtracking
- Time Complexity: O(V + E)
- Space Complexity: O(V)

## 🔍 Key Features

- Cycle detection using visited nodes set
- Bidirectional graph implementation
- Path tracking during traversal
- Distance consideration in edge weights
- Clear path visualization in output

## 📊 Results

The algorithms find different paths:

- BFS path: `['S', 'B', 'G']` (3 nodes, total distance: 15 units)
- DFS path: `['S', 'C', 'E', 'F', 'G']` (5 nodes, total distance: 14 units)

## 📝 Documentation

The LaTeX documentation includes:

- Theoretical foundations of graph traversal algorithms
- Detailed implementation analysis
- Complexity comparisons
- Practical applications and limitations
- Visual representations of the graph

## 🚀 How to Run

1. For BFS implementation:

```bash
python BFS.py
```

2. For DFS implementation:

```bash
python DFS.py
```

For interactive exploration, use Jupyter notebooks:

- `Assignment_1_BFS.ipynb`
- `Assignment_1_DFS.ipynb`

## 👥 Author

- **Ali Hassan**
- Student ID: F22BDOCS1E02011

## 📌 Conclusions

- BFS guarantees minimum edge path but not minimum distance
- DFS provides a valid path with potentially fewer memory requirements
- Edge weights are not considered in path selection for both algorithms
- For shortest path by distance, Dijkstra's or A\* algorithms would be more appropriate

## 📚 References

- Introduction to Algorithms (CLRS)
- Data Structures and Algorithms in Python
- Graph Theory and Its Applications
