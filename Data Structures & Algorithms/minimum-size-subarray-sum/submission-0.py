class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res =  float("inf")
        n = len(nums)
        for i in range(n):
            currSum = 0
            for j in range(i, n):
                currSum += nums[j]
                if currSum >= target:
                    res = min(res, j-i+1)
                    break
        return 0 if res == float("inf") else res