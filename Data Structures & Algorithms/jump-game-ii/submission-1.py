class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,0
        cnt=0
        while r<n-1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest, nums[i]+i)
            l=r+1
            r=farthest
            cnt+=1
        return cnt