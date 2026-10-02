class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxi=nums[0]
        # for i in range(len(nums)):
        #     currSum=0
        #     for j in range(i,len(nums)):
        #         currSum+=nums[j]
        #         maxi=max(currSum,maxi)
        # return maxi
        maxi=nums[0]
        currSum=0
        for i in range(len(nums)):
            if currSum<0:
                currSum=0
            currSum+=nums[i]
            maxi=max(currSum,maxi)
        return maxi
