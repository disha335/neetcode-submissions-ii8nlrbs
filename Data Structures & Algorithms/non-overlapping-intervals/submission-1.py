class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        prev = float("-inf")
        for i in intervals:
            if i[0]>=prev:
                prev = i[1]
            else:
                cnt+=1
                prev = min(prev, i[1])
        return cnt