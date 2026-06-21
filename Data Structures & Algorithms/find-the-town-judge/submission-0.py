class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dest in trust:
            incoming[dest]+=1
            outgoing[src]+=1
        
        for i in range(n+1):
            if outgoing[i]==0 and incoming[i]==n-1:
                return i
        return -1