class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        longest = 1
        def linearSearch(el, arr):
            for i in range(len(arr)):
                if arr[i] == el:
                    return True
            return False
        
        for i in range(n):
            x = nums[i]
            cnt = 1
            while linearSearch(x+1, nums):
                x+=1
                cnt+=1
            longest = max(longest, cnt)
        return longest