class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        leftSmaller=[0]*n
        rightSmaller=[0]*n
        stack=[]
        maxArea=0

        # left smaller
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            leftSmaller[i]=0 if not stack else stack[-1]+1
            stack.append(i)
        stack.clear()
        # right smaller
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            rightSmaller[i]=n-1 if not stack else stack[-1]-1
            stack.append(i)

        for i in range(n):
            w=rightSmaller[i]-leftSmaller[i]+1
            maxArea=max(maxArea,w*heights[i])
        return maxArea
        

        
