class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        size=[1]*n
        def findParent(i):
            if parent[i]!=i:
                parent[i]=findParent(parent[i])
            return parent[i]
        def unionSize(u,v):
            pu=findParent(u)
            pv=findParent(v)
            if pu==pv:
                return False
            if size[pu]>size[pv]:
                parent[pv]=pu
                size[pu]+=size[pv]
            elif size[pv]>size[pu]:
                parent[pu]=pv
                size[pv]+=size[pu]
            else:
                parent[pv]=pu
                size[pu]+=size[pv]
            return True
        
        res=n
        for u, v in edges:
            if unionSize(u,v):
                res-=1
        return res
