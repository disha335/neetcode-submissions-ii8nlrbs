class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        # memo=[[-1]*(n+1) for _ in range(n)]
        # def func(i,prev):
        #     if i>=n:
        #         return 0
        #     if memo[i][prev]!=-1:
        #         return memo[i][prev]
        #     notTake=func(i+1,prev)
        #     take=0
        #     if prev==-1 or nums[prev]<nums[i]:
        #         take=1+func(i+1,i)
        #     memo[i][prev]= max(take,notTake)
        #     return memo[i][prev]
        # return func(0,-1)
        # dp=[[0]*(n+1) for _ in range(n+1)]
        # for i in range(n-1,-1,-1):
        #     for prev in range(i-1,-2,-1):
        #         notTake=dp[i+1][prev+1]
        #         take=0
        #         if prev==-1 or nums[prev]<nums[i]:
        #             take=1+dp[i+1][i+1]
        #         dp[i][prev+1]=max(take,notTake)
        # return dp[0][0]

        temp = []
        temp.append(nums[0])
        def lb(arr,target):
            l,r=0, len(arr)-1
            ans=len(arr)
            while l<=r:
                mid=(l+r)//2
                if arr[mid]>=target:
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
            return ans

        for i in range(len(nums)):
            if temp[-1]<nums[i]:
                temp.append(nums[i])
            else:
                ind=lb(temp,nums[i])
                temp[ind]=nums[i]
        return len(temp)
