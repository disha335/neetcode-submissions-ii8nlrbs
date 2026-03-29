class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, taken, prevH):
            if ((r,c) in taken or  r<0 or c<0 or r>=m or c>=n or prevH > heights[r][c]):
                return
            taken.add((r,c))
            dfs(r-1, c, taken, heights[r][c])
            dfs(r+1, c, taken, heights[r][c])
            dfs(r, c-1, taken, heights[r][c])
            dfs(r, c+1, taken, heights[r][c])

        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n-1, atl, heights[r][n-1])

        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m-1, c, atl, heights[m-1][c])

        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res