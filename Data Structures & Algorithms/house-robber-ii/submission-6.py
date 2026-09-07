class Solution:
    def rob(self, nums: List[int]) -> int:
        # def rob(i, nums):
        #     memo={0:0,1:nums[0]}
        #     if i in memo:
        #         return memo[i]
        #     pick = nums[i-1]+rob(i-2, nums)
        #     notPick = rob(i-1, nums)
        #     memo[i]= max(pick,notPick)
        #     return memo[i]
        # n=len(nums)
        # if n==1:
        #     return nums[0]
        # ans = max(rob(n-1, nums[1:]),rob(n-1, nums[:-1]))
        # return ans
        def rob(nums):
            n=len(nums)
            dp=[0]*(n+1)       
            dp[0]=0
            dp[1]=nums[0]
            for i in range(2,n+1):
                pick = nums[i-1]+dp[i-2]
                notPick = dp[i-1]
                dp[i]= max(pick,notPick)
            return dp[n]

        n=len(nums)
        if n==1:
            return nums[0]
        ans = max(rob(nums[1:]),rob(nums[:-1]))
        return ans