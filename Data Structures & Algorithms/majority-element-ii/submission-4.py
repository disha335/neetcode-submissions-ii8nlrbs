class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hMap = {}
        for num in nums:
            hMap[num] = 1 + hMap.get(num, 0)
        res = []
        n = len(nums)
        for k in hMap:
            if hMap[k]>n//3:
                res.append(k)
        return res