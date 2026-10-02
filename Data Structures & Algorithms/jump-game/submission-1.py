class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxInd=0
        for i in range(n):
            if i>maxInd:
                return False
            maxInd=max(maxInd,i+nums[i])
        return True