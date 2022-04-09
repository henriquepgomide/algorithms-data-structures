"""
CLOSEST CARROT

Write a function, closest_carrot, that takes in a grid, a starting row, and a
starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's
are carrots. The function should return a number representing the length of
the shortest path from the starting position to a carrot. You may move up,
down, left, or right, but cannot pass through walls (X). If there is no
possible path to a carrot, then return -1.
"""

from collections import deque


def closest_carrot(grid, starting_row, starting_col):
    """
    Returns the length of the shortest path from the starting position to a
    carrot.
    """
    visited = set((starting_row, starting_col))
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == "C":
            return distance

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            delta_row, delta_col = delta

            neighbor_row = row + delta_row
            neighbor_col = col + delta_col

            row_inbounds = 0 <= neighbor_row < len(grid)
            col_inbounts = 0 <= neighbor_col < len(grid[0])

            pos = (neighbor_row, neighbor_col)
            if (
                row_inbounds
                and col_inbounts
                and grid[neighbor_row][neighbor_col] != "X"
                and pos not in visited
            ):
                queue.append((neighbor_row, neighbor_col, distance + 1))
                visited.add(pos)

    return -1


if __name__ == "__main__":
    grid = [
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['O', 'X', 'C', 'O', 'O'],
        ['O', 'X', 'X', 'O', 'O'],
        ['C', 'O', 'O', 'O', 'O'],
    ]
    print(closest_carrot(grid, 1, 2))
