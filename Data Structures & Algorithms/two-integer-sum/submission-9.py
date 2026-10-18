class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        hMap={}
        for i in range(n):
            diff=target-nums[i]
            if nums[i] in hMap:
                return [hMap[nums[i]],i]
            hMap[diff]=i
        return []