class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0, len(nums)-1
        ans=float("inf")
        while l<=r:
            m=(l+r)//2
            if nums[l]<=nums[m]:
                ans=min(ans,nums[l])
                #eliminate left , check in right
                l=m+1
            else:
                ans=min(ans,nums[m])
                r=m-1
        return ans