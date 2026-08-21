class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting + HashMap
        # hMap={}
        # for num in nums:
        #     hMap[num]=1+hMap.get(num,0)
        
        # sorted_freq = sorted(hMap.items(), key=lambda x: x[1], reverse=True)
        # return [num for num, cnt in sorted_freq[:k]]

        # MIN HEAP
        # hMap = {}
        # heap=[]
        # for num in nums:
        #     hMap[num]=1+hMap.get(num,0)
        # for num , cnt in hMap.items():
        #     heapq.heappush(heap, (cnt , num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # return [num for cnt, num in heap]
        
        # BUCKET SORT
        hMap = {}
        for num in nums:
            hMap[num]=1+hMap.get(num,0)
        # create bucket
        bucket = [[] for _ in range(len(nums)+1)]

        for num, cnt in hMap.items():
            bucket[cnt].append(num)
        
        res=[]
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res






