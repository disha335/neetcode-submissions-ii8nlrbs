from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        numFresh = 0
        FRESH, ROTTEN = 1, 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    q.append((i, j))
                elif grid[i][j] == FRESH:
                    numFresh+=1
        
        if numFresh == 0:
            return 0

        minutes = -1

        while q:
            size = len(q)
            minutes += 1
            for _ in range(size):
                i, j = q.popleft()
                for r, c in ([(i+1, j), (i-1, j), (i, j-1), (i, j+1)]):
                    if 0<=r<m and 0<=c<n and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        numFresh-=1
                        q.append((r, c))
            
        if numFresh == 0:
            return minutes
        else:
            return -1
                