class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def decode_helper(i):
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            ways = decode_helper(i+1)
            if(i+1<n and int(s[i:i+2])<=26):
                ways+=decode_helper(i+2)
            return ways
        
        return decode_helper(0)
