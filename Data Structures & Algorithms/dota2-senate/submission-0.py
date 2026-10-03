class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R,D=deque(),deque()
        senate=list(senate)
        n=len(senate)

        for i,c in enumerate(senate):
            if c=='R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            rTurn=R.popleft()
            dTurn=D.popleft()

            if rTurn<dTurn:
                R.append(dTurn+n)
            else:
                D.append(rTurn+n)
        return "Radiant" if R else "Dire"

