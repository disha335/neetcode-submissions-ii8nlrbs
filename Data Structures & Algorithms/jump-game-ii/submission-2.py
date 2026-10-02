class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        # l,r=0,0
        # cnt=0
        # while r<n-1:
        #     farthest=0
        #     for i in range(l,r+1):
        #         farthest=max(farthest, nums[i]+i)
        #     l=r+1
        #     r=farthest
        #     cnt+=1
        # return cnt
        memo=[-1]*n
        def func(ind):
            if ind>=n-1:
                return 0
            if memo[ind]!=-1:
                return memo[ind]
            mini=float("inf")
            for i in range(1,nums[ind]+1):
                mini=min(mini,1+func(ind+i))
            memo[ind]=mini
            return memo[ind]
        return func(0)