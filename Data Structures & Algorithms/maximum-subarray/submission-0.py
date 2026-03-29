class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        s = 0

        for num in nums:
            s+=num
            res = max(s, res)
            if s<0:
                s=0
        return res