class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateHrs(arr,k):
            totalHrs=0
            for i in range(len(arr)):
                totalHrs+=math.ceil(arr[i]/k)
            return totalHrs
        l, r = 1, max(piles)+1
        ans=float("inf")
        while l<=r:
            mid=(l+r)//2
            reqTime=calculateHrs(piles,mid)
            if reqTime<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
