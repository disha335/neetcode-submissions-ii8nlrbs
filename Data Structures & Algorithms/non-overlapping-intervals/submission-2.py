class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n=len(intervals)
        cnt,freeTime=1,intervals[0][1]

        for i in range(1,n):
            if intervals[i][0]>=freeTime:
                cnt+=1
                freeTime=intervals[i][1]
        return n-cnt

