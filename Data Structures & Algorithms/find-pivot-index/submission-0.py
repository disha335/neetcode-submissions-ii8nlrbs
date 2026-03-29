class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            sumLeft = nums[:i]
            sumRight = nums[i+1:]
            if(sum(sumLeft)==sum(sumRight)):
                return i
        return -1
        