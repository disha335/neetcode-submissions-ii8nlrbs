class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for op in operations:
            if st and op=='+' and len(st)>1:
                st.append(st[-1]+st[-2])
            elif st and op=='D':
                st.append(2*st[-1])
            elif st and op=='C':
                st.pop()
            else:
                st.append(int(op))
        return sum(st)