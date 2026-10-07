class Solution:
    def calculateDays(self,weights,cap):
        n=len(weights)
        load=0
        days=1
        for i in range(n):
            if load+weights[i]>cap:
                days+=1
                load=weights[i]
            else:
                load+=weights[i]
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap=max(weights)
        maxCap=sum(weights)
        # for cap in range(minCap,maxCap+1):
        #     daysReq=self.calculateDays(weights,cap)
        #     if daysReq<=days:
        #         return cap
        # return -1
        l,r=minCap,maxCap
        ans=float("inf")
        while l<=r:
            mid=(l+r)//2
            daysReq=self.calculateDays(weights,mid)
            if daysReq<=days:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans