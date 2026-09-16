class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        memo = [[-1]*n for _ in range(n)]
        def func(i,prev):
            if i>=n:
                return 0
            if memo[i][prev]!=-1:
                return memo[i][prev]
            notTake = func(i+1,prev)
            take=float("-inf")
            if prev==-1 or nums[i]>nums[prev]:
                take=1+func(i+1,i)
            memo[i][prev] = max(take,notTake)
            return memo[i][prev]
        return func(0,-1)