class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        n=len(height)
        leftMax=[0]*n
        if not height:
            return 0
        leftMax[0] = height[0]
        
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1], height[i])
        rightMax=[0]*n
        rightMax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1], height[i])

        for i in range(n):
            lMax = leftMax[i]
            rMax = rightMax[i]
            if height[i]<lMax and height[i]<rMax:
                total+=min(lMax, rMax)-height[i]
        return total

