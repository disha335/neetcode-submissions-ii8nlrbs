class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i]==nums[j] and abs(i-j)<=k:
        #             return True
        # return False
        # hMap = {}
        # for i in range(len(nums)):
        #     if nums[i] in hMap and abs(i-hMap[nums[i]])<=k:
        #         return True
        #     hMap[nums[i]]=i
        # return False
        # sliding window
        window = set()
        n = len(nums)
        l = 0
        for r in range(n):
            if (r-l)>k:
                # invalid window
                window.remove(nums[l])
                l+=1
            if nums[r] in window: 
                # we found duplicate
                return True
            window.add(nums[r])
        return False
