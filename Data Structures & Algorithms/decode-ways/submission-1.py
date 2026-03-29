class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def decode_helper(i):
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            if i in memo:
                return memo[i]
            memo[i] = decode_helper(i+1)
            if(i+1<n and int(s[i:i+2])<=26):
                memo[i]+=decode_helper(i+2)
            return memo[i]
        
        return decode_helper(0)
