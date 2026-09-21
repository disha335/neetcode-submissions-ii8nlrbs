class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #nge
        n=len(temperatures)
        res=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            res[i]=st[-1]-i if st else 0
            st.append(i)
        return res
            