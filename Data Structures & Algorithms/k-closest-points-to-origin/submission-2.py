class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []
        res = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            dist_list.append((dist,x,y))
        dist_list.sort()
        for dist,x,y in dist_list[:k]:
            res.append([x,y])
        return res