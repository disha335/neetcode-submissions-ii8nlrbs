class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cntMap = Counter(arr)
        li = []
        for num in arr:
            if(cntMap[num]==num):
                li.append(num)
        if(len(li)!=0):
            return max(li)
        return -1