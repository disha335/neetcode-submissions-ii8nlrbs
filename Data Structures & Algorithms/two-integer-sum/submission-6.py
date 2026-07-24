class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if nums[i] in hMap:
                return[hMap[nums[i]], i]
            hMap[diff]=i
        return []