class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for token in tokens:
            if token in ("+","-","*","/"):
                first=st.pop()
                second=st.pop()
                if token=='+':
                    st.append(first+second)
                elif token=='-':
                    st.append(second-first)
                elif token=='*':
                    st.append(first*second)
                elif token=='/':
                    st.append(int(second/first))
            else:
                st.append(int(token))
        return st[0]