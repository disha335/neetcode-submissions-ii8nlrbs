class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # n = len(edges)
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(i):
            if parent[i]!=i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            return 1
        ans = n
        for n1, n2 in edges:
            ans-=union(n1, n2)

        return ans
        

