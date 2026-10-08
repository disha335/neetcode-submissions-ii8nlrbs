class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            currSum = 0
            subArr= 0 
            for n in nums:
                currSum+=n
                if currSum>largest:
                    subArr+=1
                    currSum = n
                    
            return subArr+1<=k

        l, r = max(nums), sum(nums)
        res = r
        while l<=r:
            mid = l + (r-l)//2
            if canSplit(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res