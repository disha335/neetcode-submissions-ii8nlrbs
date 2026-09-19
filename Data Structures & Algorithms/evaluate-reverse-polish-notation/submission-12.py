class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t in {'+','-','*','/'}:
                a=st.pop()
                b=st.pop()
                if t=='+':
                    add = a+b
                    st.append(add)
                elif t=='*':
                    mul = a*b
                    st.append(mul)
                elif t=='-':
                    sub = b-a
                    st.append(sub)
                elif t=='/':
                    st.append(int(float(b)/a))
            else:
                st.append(int(t))
        return st[-1]