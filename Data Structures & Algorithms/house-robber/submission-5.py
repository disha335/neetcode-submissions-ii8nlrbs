class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo = [-1]*n
        def helper(i):
            if i==0:
                # not picked up ind=1
                return nums[i]
            if i<=0:
                return 0
            if memo[i]!=-1:
                return memo[i]
            pick = nums[i]+helper(i-2)
            notPick = helper(i-1)
            memo[i] = max(pick,notPick)
            return memo[i]
        return helper(n-1)