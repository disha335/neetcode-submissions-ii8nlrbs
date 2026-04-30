class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hMap = {}
        max_k = -1
        for num in arr:
            hMap[num] = 1 + hMap.get(num, 0)
        
        for k, v in hMap.items():
            if k == v:
                max_k = max(k, max_k)
        return max_k
        
