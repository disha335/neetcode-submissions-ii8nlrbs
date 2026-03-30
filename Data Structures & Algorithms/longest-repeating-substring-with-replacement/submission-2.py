class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0 
        maxFreq = 0
        hMap = {}
        for r in range(len(s)):
            hMap[s[r]] = 1 + hMap.get(s[r], 0)
            maxFreq = max(maxFreq, hMap[s[r]])
            while (r-l+1) - maxFreq>k:
                hMap[s[l]]-=1
                l+=1
            res=max(res, r-l+1)
        return res



