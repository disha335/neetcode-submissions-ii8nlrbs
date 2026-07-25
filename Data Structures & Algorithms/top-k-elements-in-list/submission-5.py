class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting + HashMap
        # hMap={}
        # for num in nums:
        #     hMap[num]=1+hMap.get(num,0)
        
        # sorted_freq = sorted(hMap.items(), key=lambda x: x[1], reverse=True)
        # return [num for num, cnt in sorted_freq[:k]]
        
        hMap = {}
        heap=[]
        for num in nums:
            hMap[num]=1+hMap.get(num,0)
        for num , cnt in hMap.items():
            heapq.heappush(heap, (cnt , num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for cnt, num in heap]
        


