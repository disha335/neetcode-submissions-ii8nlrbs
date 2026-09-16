class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # memo = [[-1]*n for _ in range(n)]
        # def func(i,prev):
        #     if i>=n:
        #         return 0
        #     if memo[i][prev]!=-1:
        #         return memo[i][prev]
        #     notTake = func(i+1,prev)
        #     take=float("-inf")
        #     if prev==-1 or nums[i]>nums[prev]:
        #         take=1+func(i+1,i)
        #     memo[i][prev] = max(take,notTake)
        #     return memo[i][prev]
        # return func(0,-1)
        # r - i 1 to n
        # col - prev
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for prev in range(i-1,-2,-1):
                notTake = dp[i+1][prev+1]
                take=float("-inf")
                if prev==-1 or nums[i]>nums[prev]:
                    take=1+dp[i+1][i+1]
                dp[i][prev+1]=max(take,notTake)
        return dp[0][0]



        