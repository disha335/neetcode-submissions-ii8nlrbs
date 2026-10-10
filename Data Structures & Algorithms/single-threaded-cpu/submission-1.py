class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])
        minHeap,res=[],[]
        time = tasks[0][0] # task with smallest enque time
        i=0

        while minHeap or i<len(tasks):
            # checking if time is less tha or equal to enque time
            while i<len(tasks) and time>=tasks[i][0]:
                # we only need the proc time and index 
                heapq.heappush(minHeap, [tasks[i][1],tasks[i][2]])
                i+=1
            if not minHeap:
                # if heap is empty , cpu is idle , fast - forward 
                time=tasks[i][0]
            else:
                # pop from the queue
                procTime, ind = heapq.heappop(minHeap)
                time+=procTime
                res.append(ind)
        return res
            