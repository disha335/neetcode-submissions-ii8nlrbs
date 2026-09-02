class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights), len(heights[0])
        dist = [[float("inf")]*n for _ in range(m)]
        dist[0][0]=0
        pq=[]
        heapq.heappush(pq,(0,0,0)) # dist,r,c

        while pq:
            dis,r,c=heapq.heappop(pq)
            if r==m-1 and c==n-1:
                return dis
            for i, j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=i<m and 0<=j<n:
                    diff = abs(heights[i][j]-heights[r][c])
                    newEffort = max(diff, dis)
                    if newEffort<dist[i][j]:
                        dist[i][j]=newEffort
                        heapq.heappush(pq,(newEffort,i,j))
        return 0


