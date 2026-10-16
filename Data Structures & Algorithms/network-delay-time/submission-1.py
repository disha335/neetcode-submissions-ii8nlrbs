class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u,v,t in times:
            adj[u].append((v,t))

        dist = [float("inf")]*(n+1)
        dist[k]=0

        pq=[]
        heapq.heappush(pq,(0,k))

        while pq:
            time,node = heapq.heappop(pq)
            for nei,t in adj[node]:
                if time+t<dist[nei]:
                    dist[nei]=time+t
                    heapq.heappush(pq,(dist[nei],nei))
        return max(dist[1:]) if max(dist[1:])!=float("inf") else -1