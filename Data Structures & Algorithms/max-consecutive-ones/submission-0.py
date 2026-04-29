class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0
        for ele in nums:
            if ele == 1:
                cnt+=1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0
        return max_cnt