class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        size=[0]*(n+1)
        parent=[i for i in range(n+1)]
        def findParent(node):
            if node!=parent[node]:
                parent[node]=findParent(parent[node])
            return parent[node]
        
        def unionBySize(u,v):
            pu=findParent(u)
            pv=findParent(v)
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
            if not unionBySize(u,v):
                return [u,v]