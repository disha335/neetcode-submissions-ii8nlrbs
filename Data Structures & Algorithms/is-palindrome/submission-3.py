class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join([ch for ch in s if ch.isalnum()])
        l, r = 0, len(ss)-1
        while l<=r:
            if ss[l].lower()!=ss[r].lower():
                return False
            l+=1
            r-=1
        return True