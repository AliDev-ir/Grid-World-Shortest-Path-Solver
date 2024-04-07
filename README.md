# Grid-World-Shortest-Path-Solver
Explore Python implementations of BFS and IDFS algorithms for solving shortest path problems in grid environments. Find the optimal route through obstacles efficiently.
Sure, I can provide you with some explanations and a README file for your code. Let's start with some explanations for your code:

### BFS Algorithm:
- BFS stands for Breadth First Search, which is an algorithm for traversing or searching tree or graph data structures. It explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
- In your code, you've implemented BFS to find the shortest path from a given source cell to a destination cell in an 8x8 grid world with obstacles.
- The algorithm maintains a queue of cells to be explored, and at each step, it dequeues a cell and explores its neighbors, enqueuing them if they are valid and have not been visited yet.
- The distance from the source cell to each explored cell is maintained, and once the destination cell is found, the algorithm returns the shortest distance.

### IDFS Algorithm:
- IDFS stands for Iterative Deepening Depth First Search. It is a combination of DFS and BFS algorithms. It is used when the depth of the search tree is not known.
- Your code implements IDFS by performing DFS up to a certain depth limit, and then increasing the depth limit iteratively until the destination is found.
- It explores paths in a depth-first manner, but limits the search depth at each iteration to avoid infinite loops and ensure optimality.
- This algorithm is useful for scenarios where the search space is large and memory usage needs to be controlled, as it only stores the current path in memory.

- Sure, I can provide you with some explanations and a README file for your code. Let's start with some explanations for your code:

### BFS Algorithm:
- BFS stands for Breadth First Search, which is an algorithm for traversing or searching tree or graph data structures. It explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
- In your code, you've implemented BFS to find the shortest path from a given source cell to a destination cell in an 8x8 grid world with obstacles.
- The algorithm maintains a queue of cells to be explored, and at each step, it dequeues a cell and explores its neighbors, enqueuing them if they are valid and have not been visited yet.
- The distance from the source cell to each explored cell is maintained, and once the destination cell is found, the algorithm returns the shortest distance.

### IDFS Algorithm:
- IDFS stands for Iterative Deepening Depth First Search. It is a combination of DFS and BFS algorithms. It is used when the depth of the search tree is not known.
- Your code implements IDFS by performing DFS up to a certain depth limit, and then increasing the depth limit iteratively until the destination is found.
- It explores paths in a depth-first manner, but limits the search depth at each iteration to avoid infinite loops and ensure optimality.
- This algorithm is useful for scenarios where the search space is large and memory usage needs to be controlled, as it only stores the current path in memory.


# Shortest Path Finder

This repository contains Python implementations of BFS (Breadth First Search) and IDFS (Iterative Deepening Depth First Search) algorithms to find the shortest path in an 8x8 grid world with obstacles.

## Usage

- `bfs_shortest_path.py`: Run this script to find the shortest path using BFS algorithm.
- `idfs_shortest_path.py`: Run this script to find the shortest path using IDFS algorithm.

## Instructions

1. Clone the repository to your local machine:

```
git clone https://github.com/AliDev-ir/Grid-World-Shortest-Path-Solver.git
```

2. Navigate to the repository directory:

```
cd Grid-World-Shortest-Path-Solver
```

3. Run the desired script by providing the source and destination coordinates when prompted.

## Example

To find the shortest path using BFS:

```
python bfs_shortest_path.py
```

To find the shortest path using IDFS:

```
python idfs_shortest_path.py
```

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Connection

Email : Ali@alidev.ir
Website : AliDev.ir
Telegram : t.me/Ali_Dev_ir
Linkdin : https://lnkd.in/dDaqQE4S
Github : github.com/AliDev-ir
Instagram : instagram.com/Ali_Vaez79
```

