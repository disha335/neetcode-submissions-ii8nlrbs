class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        minHeap = [] # [end, passengers]
        heapq.heapify(minHeap)
        curPass = 0

        for numPass, start, end in trips:
            while minHeap and minHeap[0][0]<=start:
                # trip not completed
                curPass-=minHeap[0][1]
                heapq.heappop(minHeap)
            curPass+=numPass
            if curPass>capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True