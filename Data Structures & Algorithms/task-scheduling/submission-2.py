class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cntMap = Counter(tasks)
        maxHeap=[-cnt for cnt in cntMap.values()]
        heapq.heapify(maxHeap)
        q=deque()
        time=0

        while maxHeap or q:
            time+=1
            if maxHeap:
                taskCnt = 1 + heapq.heappop(maxHeap)
                if taskCnt!=0:
                    q.append((taskCnt,time+n))
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
