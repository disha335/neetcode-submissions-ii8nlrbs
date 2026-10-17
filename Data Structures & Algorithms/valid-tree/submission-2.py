class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=set()
        q=deque()
        q.append((0,-1)) # node, prev

        while q:
            node, prev = q.popleft()
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei==prev:
                    continue
                q.append((nei,node))
        
        return len(q)==0 and len(visit)==n
            
