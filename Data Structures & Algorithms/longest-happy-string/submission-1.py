class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cntMap = {'a':a,'b':b,'c':c}
        maxHeap = [[-cnt,ch] for ch,cnt in cntMap.items() if cnt>0]
        heapq.heapify(maxHeap)
        res = []
        prev = None

        while maxHeap:
            cnt,ch = heapq.heappop(maxHeap)
            if len(res)>1 and res[-1]==res[-2]==ch:
                if not maxHeap:
                    break
                cnt2,ch2=heapq.heappop(maxHeap)
                res+=ch2
                cnt2+=1
                if cnt2:
                    heapq.heappush(maxHeap,[cnt2,ch2])
                heapq.heappush(maxHeap,[cnt,ch])
            else:
                res+=ch
                cnt+=1
                if cnt:
                    heapq.heappush(maxHeap,[cnt,ch])
        return "".join(res)