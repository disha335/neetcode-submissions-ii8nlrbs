class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # for i in range(len(strs[0])):
        #     for st in strs:
        #         if(i==len(st) or st[i]!=strs[0][i]):
        #             return res
        #     res+=st[i]
        # return res

        strs.sort()
        start, end = strs[0], strs[-1]
        for i in range(min(len(start), len(end))):
            if start[i]!=end[i]:
                return strs[0][:i]
        return strs[0]
