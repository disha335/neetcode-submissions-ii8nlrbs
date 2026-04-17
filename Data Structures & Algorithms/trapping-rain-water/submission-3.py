class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # res = 0
        # for i in range(n):
        #     leftMax = rightMax = height[i]
        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
        #     for j in range(i+1, n):
        #         rightMax = max(rightMax, height[j])
        #     res += min(leftMax, rightMax) - height[i]
        # return res
        if not height:
            return 0 
        l, r = 0, len(height)-1
        res = 0
        leftMax, rightMax = height[l], height[r]
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax-height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax-height[r]
        return res

