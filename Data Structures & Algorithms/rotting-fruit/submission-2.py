class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ROTTEN,FRESH = 2, 1
        numFresh=0
        minutes=-1
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==FRESH:
                    numFresh+=1
                if grid[i][j]==ROTTEN:
                    q.append((i, j))
        if numFresh==0:
            return 0
        while q:
            size=len(q)
            minutes+=1
            for _ in range(size):
                i, j = q.popleft()
                for r, c in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==FRESH:
                        grid[r][c]=ROTTEN
                        q.append((r,c))
                        numFresh-=1
        return minutes if numFresh==0 else -1
