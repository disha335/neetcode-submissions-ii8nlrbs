class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glMax,glMin=nums[0],nums[0]
        total=0
        currMax,currMin=0,0

        for n in nums:
            currMax = max(currMax+n,n)
            currMin = min(currMin+n,n)
            total+=n
            glMax=max(glMax,currMax)
            glMin=min(glMin,currMin)
        
        return max(total-glMin,glMax) if glMax>0 else glMax

