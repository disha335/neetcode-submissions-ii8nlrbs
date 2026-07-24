class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}
        for ch in s:
            sMap[ch]=1+sMap.get(ch, 0)
        for ch in t:
            tMap[ch]=1+tMap.get(ch, 0)
        return sMap==tMap
        