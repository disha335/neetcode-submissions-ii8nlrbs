class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u,v,wt in flights:
            adj[u].append((v,wt))
        
        q = deque()
        q.append((0,src,0))

        dist = [float("inf")]*n
        dist[src]=0

        while q:
            stops,node,cost = q.popleft()
            if stops>k:
                continue
            for nei,wt in adj[node]:
                if cost+wt<dist[nei] and stops<=k:
                    dist[nei]=cost+wt
                    q.append((stops+1,nei,dist[nei]))
        if dist[dst]==float("inf"):
            return -1
        return dist[dst]
