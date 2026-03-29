from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for r, c in ([(i+1, j), (i-1, j), (i, j-1), (i, j+1)]):
                    if 0<=r<m and 0<=c<n and grid[r][c]==INF:
                        grid[r][c] = grid[i][j]+1
                        q.append((r, c))