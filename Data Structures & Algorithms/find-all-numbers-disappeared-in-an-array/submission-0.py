class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hs = set(range(1, n+1))
        for num in nums:
            hs.discard(num)
        return list(hs)
