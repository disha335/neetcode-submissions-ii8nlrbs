from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()

        # Initialize the queue with all treasure chest cells
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        # Perform BFS
        while q:
            i, j = q.popleft()
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 2147483647:
                    grid[r][c] = grid[i][j] + 1
                    q.append((r, c))