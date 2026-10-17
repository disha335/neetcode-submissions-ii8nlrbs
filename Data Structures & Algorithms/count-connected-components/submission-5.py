class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        size = [0]*(n+1)
        nc = n
        def findParent(node):
            if node!=parent[node]:
                parent[node]=findParent(parent[node])
            return parent[node]
        
        def unionBySize(u,v):
            pu, pv = findParent(u), findParent(v)
            if pu==pv:
                return False
            if size[pu]<size[pv]:
                parent[pu]=pv
                size[pv]+=size[pu]
            else:
                parent[pv]=pu
                size[pu]+=size[pv]
            return True
        
        for u, v in edges:
            if unionBySize(u,v):
                nc-=1
        return nc

            

