class Solution:
    def simplifyPath(self, path: str) -> str:
        directories=path.split('/')
        st=[]
        for curr in directories:
            if curr=='.' or curr=='':
                continue
            elif curr=='..':
                if st:
                    st.pop()
            else:
                st.append(curr)
        return '/'+'/'.join(st)
