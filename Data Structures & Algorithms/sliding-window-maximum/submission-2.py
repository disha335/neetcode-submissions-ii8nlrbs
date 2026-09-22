from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        # for i in range(n-k+1):
        #     maxi=nums[i]
        #     for j in range(i,i+k):
        #         maxi=max(maxi,nums[j])
        #     res.append(maxi)
        # return res
        dq=deque()
        for i in range(n):
            while dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res

