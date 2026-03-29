class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if(s==s[::-1]):
            return True

        for i in range(n):
            newS = s[:i]+s[i+1:]
            if (newS==newS[::-1]):
                return True
        return False
            