class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        def findNSE(heights):
            st=[]
            nse=[0]*n
            for i in range(n-1,-1,-1):
                while st and heights[st[-1]]>=heights[i]:
                    st.pop()
                nse[i]=n if not st else st[-1]
                st.append(i)
            return nse
        def findPSE(heights):
            st=[]
            pse=[0]*n
            for i in range(n):
                while st and heights[st[-1]]>heights[i]:
                    st.pop()
                pse[i]=-1 if not st else st[-1]
                st.append(i)
            return pse
        
        nse=findNSE(heights)
        pse=findPSE(heights)
        maxArea=0
        for i in range(n):
            h=heights[i]
            w=nse[i]-pse[i]-1
            maxArea=max(maxArea,h*w)
        return maxArea

