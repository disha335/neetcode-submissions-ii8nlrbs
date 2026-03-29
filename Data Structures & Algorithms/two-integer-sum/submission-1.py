class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        li = []
        for i in range(n):
            for j in range(i+1, n):
                if(nums[i]+nums[j]==target):
                    li.append(i)
                    li.append(j)
        return li