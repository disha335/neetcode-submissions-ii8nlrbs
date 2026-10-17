class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(i,nums):
            n=len(nums)
            # dp = [0]*(n+1)
            prev2=0
            prev=nums[0]
            # prev,prev2=0,0
            for i in range(2,n+1):
                pick = nums[i-1]+prev2
                noPick = prev
                curr = max(pick,noPick)
                prev2=prev
                prev=curr
            return prev
        if len(nums)==1:
            return nums[0]
        return max(helper(len(nums)-2,nums[1:]),helper(len(nums)-2,nums[:-1]))