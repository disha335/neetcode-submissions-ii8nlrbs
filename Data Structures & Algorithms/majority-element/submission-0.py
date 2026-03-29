class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        cnt = 0

        for num in nums:
            if cnt==0:
                res=num
            if num==res:
                cnt+=1
            else:
                cnt-=1
        return res