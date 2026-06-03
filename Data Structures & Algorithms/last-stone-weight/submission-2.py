class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones) # first largest -7
            second = heapq.heappop(stones) # second largest -8
            if second>first:
                heapq.heappush(stones, first-second)
        stones.append(0)
        return abs(stones[0])

