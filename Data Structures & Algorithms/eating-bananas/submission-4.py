class Solution:
    def calcHrs(self,arr,k):
        total=0
        for i in range(len(arr)):
            total+=math.ceil(arr[i]/k)
        return total
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search on value of k
        l,r=1,max(piles)+1
        ans=float("inf")
        while l<=r:
            m=(l+r)//2
            reqTime=self.calcHrs(piles,m)
            if reqTime<=h:
                ans=m
                #search on left, eliminate right
                r=m-1
            else:
                l=m+1
        return ans