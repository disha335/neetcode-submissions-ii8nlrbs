class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        q=deque()
        res=[]
        for u,v in prerequisites:
            adj[v].append(u)
        
        for i in range(numCourses):
            for nei in adj[i]:
                indegree[nei]+=1

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return len(res)==numCourses