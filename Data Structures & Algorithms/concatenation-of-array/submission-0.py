class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        li = []
        i = 0
        while i<2:
            for num in nums:
                li.append(num)
            i+=1
        return li