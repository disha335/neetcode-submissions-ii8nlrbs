class Solution:
    def tribonacci(self, n: int) -> int:
        # memo={0:0,1:1,2:1}
        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = helper(i-1)+helper(i-2)+helper(i-3)
        #     return memo[i]
        # return helper(n)
        # memo={0:0,1:1,2:1}.
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        prev3=0
        prev2=1
        prev=1
        for i in range(3,n+1):
            curr = prev3+prev2+prev
            prev3=prev2
            prev2=prev
            prev=curr
        return prev