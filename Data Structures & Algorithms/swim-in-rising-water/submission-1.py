class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dist = [[float("inf")] * N for _ in range(N)]
        dist[0][0] = grid[0][0]
        pq=[]
        heapq.heappush(pq,(grid[0][0],0,0))

        while pq:
            t, r, c = heapq.heappop(pq)
            if t > dist[r][c]:
                continue
            if r == N - 1 and c == N - 1:
                return t
            for i, j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=i<N and 0<=j<N:
                    newTime = max(t, grid[i][j])
                    if newTime < dist[i][j]:
                        dist[i][j] = newTime
                        heapq.heappush(pq, (newTime, i, j))