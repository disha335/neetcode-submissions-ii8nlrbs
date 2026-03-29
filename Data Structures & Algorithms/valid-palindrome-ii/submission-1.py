class Solution:
    def validPalindrome(self, s: str) -> bool:
        # n = len(s)
        # if(s==s[::-1]):
        #     return True

        # for i in range(n):
        #     newS = s[:i]+s[i+1:]
        #     if (newS==newS[::-1]):
        #         return True
        # return False

        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                # check for s[l+1..r]
                skipLeft = s[l+1:r+1]
                # check for s[l..r+1]
                skipRight = s[l:r]
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            l+=1
            r-=1
        return True
        

            