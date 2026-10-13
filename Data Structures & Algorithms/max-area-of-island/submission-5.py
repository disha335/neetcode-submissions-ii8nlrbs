class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        maxArea=0
        area=0
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]==0:
                return 0
            else:
                grid[r][c]=0
                area = 1+dfs(r-1,c) +dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)
                return area
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    maxArea=max(maxArea,dfs(i,j))
        return maxArea