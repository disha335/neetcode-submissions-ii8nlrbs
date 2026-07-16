class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                # as we are going to modify the subset later
                res.append(subset.copy())
                return
            # decision to consider including 
            subset.append(nums[i])
            dfs(i+1)
            # decision not to consider including 
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res