class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch =='(' or ch=='{' or ch=='[':
                st.append(ch)
            elif ch==')':
                if not st or st.pop()!='(':
                    return False
            elif ch=='}':
                if not st or st.pop()!='{':
                    return False
            elif ch==']':
                if not st or st.pop()!='[':
                    return False
        return len(st)==0
            