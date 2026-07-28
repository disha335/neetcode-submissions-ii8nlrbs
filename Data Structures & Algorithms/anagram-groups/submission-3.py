class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        for st in strs:
            sorted_word = ''.join(sorted(st))
            if sorted_word in hMap:
                hMap[sorted_word].append(st)
            else:
                hMap[sorted_word]=[st]
        return list(hMap.values())

