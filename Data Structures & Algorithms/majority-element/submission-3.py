class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hMap = {}
        # n = len(nums)
        # for num in nums:
        #     hMap[num] = 1+hMap.get(num, 0)
        
        # for k in hMap:
        #     if hMap[k]>n//2:
        #         return k
        res = cnt = 0
        for n in nums:
            if cnt==0:
                res=n
            if res == n:
                cnt+=1
            else:
                cnt-=1
        return res


