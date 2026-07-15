class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        start, end = strs[0], strs[-1]
        for i in range(min(len(start), len(end))):
            if start[i]!=end[i]:
                return strs[0][:i]
        return strs[0]