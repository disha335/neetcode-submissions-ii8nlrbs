class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for num in nums:
            hMap[num] = 1 + hMap.get(num, 0)
        
        arr = []
        for num, cnt in hMap.items():
            arr.append([cnt, num])
        arr.sort()
        
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        