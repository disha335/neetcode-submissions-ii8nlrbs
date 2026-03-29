class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        hs = set()

        for trip in triplets:
            if trip[0]>target[0] or trip[1]>target[1] or trip[2]>target[2]:
                continue
            for i, v in enumerate(trip):
                if v==target[i]:
                    hs.add(i)
        return len(hs)==3