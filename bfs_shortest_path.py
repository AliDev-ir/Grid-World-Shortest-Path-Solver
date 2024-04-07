from collections import deque
import sys

class Position:
    """Represents a position in the grid."""
    def __init__(self, row, col):
        self.x = row
        self.y = col

class PosAndDist:
    """Represents a position and its distance from the source."""
    def __init__(self, pt: Position, dist: int):
        self.pt = pt
        self.dist = dist

def is_valid_cell(row, col):
    """Check if a cell is within the grid boundaries."""
    return 0 <= row < 8 and 0 <= col < 8

def bfs_shortest_path(mat, src, dest):
    """Find the shortest path from source to destination using BFS."""
    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = deque()
    queue.append(PosAndDist(src, 0))
    visited[src.x][src.y] = True

    while queue:
        current_cell = queue.popleft()
        current_pos = current_cell.pt

        if current_pos.x == dest.x and current_pos.y == dest.y:
            return current_cell.dist

        for i in range(4):
            row = current_pos.x + [-1, 0, 0, 1][i]
            col = current_pos.y + [0, -1, 1, 0][i]

            if is_valid_cell(row, col) and mat[row][col] == 1 and not visited[row][col]:
                visited[row][col] = True
                adj_cell = PosAndDist(Position(row, col), current_cell.dist + 1)
                queue.append(adj_cell)

    return -1

if __name__ == "__main__":
    mat = [[1, 0, 1, 1, 1, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 0],
           [1, 0, 1, 0, 1, 1, 0, 1],
           [1, 1, 1, 0, 1, 1, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 0],
           [1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 1, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1]]

    try:
        x1 = int(input("Enter the row number of source (0-7): "))
        x2 = int(input("Enter the column number of source (0-7): "))
        y1 = int(input("Enter the row number of destination (0-7): "))
        y2 = int(input("Enter the column number of destination (0-7): "))
    except ValueError:
        print("Invalid input. Please enter integers.")
        sys.exit()

    source = Position(x1, x2)
    dest = Position(y1, y2)

    if not is_valid_cell(source.x, source.y) or not is_valid_cell(dest.x, dest.y) or mat[source.x][source.y] != 1 or mat[dest.x][dest.y] != 1:
        print("Invalid Source or Destination point")
        sys.exit()

    shortest_distance = bfs_shortest_path(mat, source, dest)

    if shortest_distance == -1:
        print("There is no path from source to destination")
    else:
        print("Shortest path =", shortest_distance)
