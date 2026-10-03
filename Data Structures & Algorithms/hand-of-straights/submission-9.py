class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hMap=Counter(hand)
        for num in hand:
            start=num
            while hMap[start-1]:
                start-=1
            while start<=num:
                while hMap[start]:
                    for i in range(start,start+groupSize):
                        if not hMap[i]:
                            return False
                        hMap[i]-=1
                start+=1
        return True