from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF, TREASURE = 2147483647, 0
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == TREASURE:
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            for r, c in [(i+1,j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0<=r<m and 0<=c<n and grid[r][c] == INF:
                    grid[r][c] = 1 + grid[i][j]
                    q.append((r,c))