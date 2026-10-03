class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hMap={}
        for h in hand:
            hMap[h]=1+hMap.get(h,0)
        hand.sort()
        for num in hand:
            if hMap[num]:
                for i in range(num, num + groupSize):
                    if not hMap.get(i,0):
                        return False
                    hMap[i] -= 1
        return True