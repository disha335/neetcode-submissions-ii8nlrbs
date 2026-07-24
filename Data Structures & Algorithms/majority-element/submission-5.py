class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hMap = {}
        # n = len(nums)
        # for num in nums:
        #     hMap[num]=1+hMap.get(num, 0)
        
        # for num in hMap:
        #     if hMap[num]>n//2:
        #         return num
        ele, cnt = 0, 0
        for num in nums:
            if cnt==0:
                ele=num
            if ele==num:
                cnt+=1
            else:
                cnt-=1
        return ele
            