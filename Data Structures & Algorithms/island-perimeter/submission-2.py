class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        def dfs(r, c):
            if r<0 or c<0 or r==m or c==n or grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            perim = dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
            return perim
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                   return dfs(i, j)
        return 0