class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[]for _ in range(numCourses)]
        indegree = [0]*numCourses
        topo=[]
        q=deque()
        for i,j in prerequisites:
            adj[j].append(i)
        
        for i in range(numCourses):
            for nei in adj[i]:
                indegree[nei]+=1
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if(indegree[nei]==0):
                    q.append(nei)
        
        if(len(topo)==numCourses):
            return topo
        return []
