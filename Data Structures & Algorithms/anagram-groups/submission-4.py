class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        for st in strs:
            sorted_str = ''.join(sorted(st))
            if sorted_str in hMap:
                hMap[sorted_str].append(st)
            else:
                hMap[sorted_str]=[st]
        return list(hMap.values())
            