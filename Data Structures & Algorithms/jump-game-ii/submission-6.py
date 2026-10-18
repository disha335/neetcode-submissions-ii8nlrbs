class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        # def helper(i):
        #     memo=[-1]*n
        #     mini=float("inf")
        #     if i>=n-1:
        #         return 0
        #     if memo[i]!=-1:
        #         return memo[i]
        #     for ind in range(1,nums[i]+1):
        #         mini=min(mini,1+helper(i+ind))
        #     memo[i]=mini
        #     return memo[i]
        # return helper(0)
        l,r=0,0
        jump=0
        farthest=0
        while r<n-1:
            
            for i in range(l,r+1):
                farthest=max(farthest,nums[i]+i)
            l=r+1
            r=farthest
            jump+=1
        return jump