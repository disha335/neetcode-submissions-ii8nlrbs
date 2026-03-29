class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st in hMap:
                hMap[sorted_st].append(st)
            else:
                hMap[sorted_st] = [st]
        return list(hMap.values())