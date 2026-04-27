class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hMap:
                return [hMap[diff], idx]
            hMap[num]=idx
        return []