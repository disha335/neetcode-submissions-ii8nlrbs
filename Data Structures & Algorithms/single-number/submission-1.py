class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hs = set()
        for num in nums:
            if num in hs:
                hs.remove(num)
            else:
                hs.add(num)
        return list(hs)[0]

