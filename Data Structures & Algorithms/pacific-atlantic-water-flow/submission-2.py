class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        def dfs(r, c, visit, prevHeight):
            if(r<0 or c<0 or r>=m or c>=n or (r,c) in visit or prevHeight>heights[r][c]):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(n):
            # top row - starting from pacific ocean 
            dfs(0, c, pac, heights[0][c])
            # bottom row - starting from atlantic ocean 
            dfs(m-1, c, atl, heights[m-1][c])
        
        for r in range(m):
            # left col - starting from pacific ocean 
            dfs(r, 0, pac, heights[r][0])
            # right col - starting from atl ocean 
            dfs(r, n-1, atl, heights[r][n-1])

        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res