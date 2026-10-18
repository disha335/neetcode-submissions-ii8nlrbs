class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[[-1]*(n+1) for _ in range(n)]
        def func(i,prev):
            if i>=n:
                return 0
            if memo[i][prev]!=-1:
                return memo[i][prev]
            notTake=func(i+1,prev)
            take=0
            if prev==-1 or nums[prev]<nums[i]:
                take=1+func(i+1,i)
            memo[i][prev]= max(take,notTake)
            return memo[i][prev]
        return func(0,-1)