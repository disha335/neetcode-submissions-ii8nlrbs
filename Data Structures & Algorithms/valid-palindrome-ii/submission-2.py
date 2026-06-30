class Solution:
    def validPalindrome(self, s: str) -> bool:
        # abdba
        #s[0:2] s[2]
        if s==s[::-1]:
            return True
        for i in range(len(s)):
            newS = s[:i] + s[i+1:]
            if newS==newS[::-1]:
                return True
        return False