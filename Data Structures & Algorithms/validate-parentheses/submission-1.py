class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for ch in s:
            if ch == '(' or ch == '[' or ch=='{':
                stck.append(ch)
            elif ch==')':
                if not stck or stck.pop()!='(':
                    return False
            elif ch==']':
                if not stck or stck.pop()!='[':
                    return False
            elif ch=='}':
                if not stck or stck.pop()!='{':
                    return False
        return len(stck)==0