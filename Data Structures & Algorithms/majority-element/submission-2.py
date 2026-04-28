class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hMap = {}
        n = len(nums)
        for num in nums:
            hMap[num] = 1+hMap.get(num, 0)
        
        for k in hMap:
            if hMap[k]>n//2:
                return k
