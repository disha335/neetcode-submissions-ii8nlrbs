class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()

        def dfs(r,c):
            if r<0 or r==m or c<0 or c==n or grid[r][c]!=1:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            perim = dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
            return perim
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    return dfs(r,c)
        return 0