class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hMap=Counter(hand)
        hand.sort()
        for num in hand:
            if hMap[num]:
                for i in range(num,num+groupSize):
                    if not hMap[i]:
                        return False
                    hMap[i]-=1
        return True
