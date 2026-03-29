class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        largestRes = -1
        for i in range(1, len(num)-1):
            if(num[i-1]==num[i])and(num[i]==num[i+1]):
                res = num[i-1]+num[i]+num[i+1]
                res = int(res)
                largestRes = max(res, largestRes)
        if largestRes == -1:
            return ""
        if largestRes == 0:
            return "000"
        return str(largestRes)