class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        fresh=0
        time=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        
        while q and fresh>0:
            q_len=len(q)
            for i in range(q_len):
                r,c = q.popleft()
                for i,j in [(r,c-1),(r,c+1),(r+1,c),(r-1,c)]:
                    if 0<=i<m and 0<=j<n and grid[i][j]==1:
                        grid[i][j]=2
                        q.append((i,j))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
            
