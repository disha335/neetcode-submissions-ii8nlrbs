class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        jump = 0
        n= len(nums)

        while r< n-1:
            maxReach = 0
            for i in range(l, r+1):
                 maxReach=max(maxReach, i+nums[i])

            l, r = r+1, maxReach
            jump+=1
        return jump

