class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hMap={}
        for h in hand:
            hMap[h]=1+hMap.get(h,0)
        
        for num in hand:
            start=num
            while hMap.get(start-1,0):
                start-=1
            while start<=num:
                while hMap[start]:
                    for i in range(start,start+groupSize):
                        if not hMap.get(i,0):
                            return False
                        hMap[i]-=1
                start+=1
        return True