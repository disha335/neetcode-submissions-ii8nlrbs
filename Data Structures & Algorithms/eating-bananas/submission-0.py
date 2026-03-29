class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l<=r:
            hours = 0
            k = (l+r)//2
            for p in piles:
                hours+=math.ceil(float(p)/k)
            if hours<=h:
                res = min(k, res)
                r = k-1
            else:
                l = k+1
        return res 