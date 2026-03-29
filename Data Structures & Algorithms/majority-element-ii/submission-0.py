class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hMap = {}
        res = []
        for num in nums:
            hMap[num] = 1 + hMap.get(num, 0)
        
        for k, v in hMap.items():
            if v>len(nums)/3:
                res.append(k)
        return res

        