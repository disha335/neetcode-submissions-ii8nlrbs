class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        hs1 = set()
        hs2 = set(range(1, n*n+1))
        grid_arr = []
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] in hs1:
                    res.append(grid[i][j])
                hs1.add(grid[i][j])
                grid_arr.append(grid[i][j])
        
        for ele in hs2:
            if ele not in grid_arr:
                res.append(ele)

        return res