class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten=0,0
        twenty=0
        n=len(bills)
        for i in range(n):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five:
                    ten+=1
                    five-=1
                else:
                    return False
            elif bills[i]==20:
                if five and ten:
                    twenty+=1
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
