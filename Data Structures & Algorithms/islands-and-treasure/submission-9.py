class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        m,n=len(grid),len(grid[0])
        INF = 2147483647

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
        

        while q:
            r,c=q.popleft()
            for i,j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=i<m and 0<=j<n and grid[i][j]==INF:
                    grid[i][j]=1+grid[r][c]
                    q.append((i,j))



