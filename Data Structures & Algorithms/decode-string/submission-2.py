class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        res=""
        for ch in s:
            if ch!=']':
                st.append(ch)
            else:
                currStr=""
                while st[-1]!='[':
                    currStr=st.pop()+currStr
                st.pop()
                k=""
                while st and st[-1].isdigit():
                    k=st.pop()+k
                st.append(int(k)*currStr)
        return "".join(st)

