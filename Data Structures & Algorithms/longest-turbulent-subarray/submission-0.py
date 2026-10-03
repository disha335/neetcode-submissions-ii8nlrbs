class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        res=1
        prev=""
        l,r=0,1

        while r<n:
            if arr[r-1]>arr[r] and prev!=">":
                res=max(res,r-l+1)
                r+=1
                prev=">"
            elif arr[r-1]<arr[r] and prev!="<":
                res=max(res,r-l+1)
                r+=1
                prev="<"
            else:
                prev=""
                r=r+1 if arr[r-1]==arr[r] else r
                l=r-1
        return res

